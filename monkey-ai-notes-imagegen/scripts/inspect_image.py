#!/usr/bin/env python3
"""Read-only geometry/color/grid diagnostics. Never scores aesthetic similarity."""
import argparse
import json
import math
import sys
from pathlib import Path

try:
    import numpy as np
    from PIL import Image, ImageOps
except ImportError as exc:
    print(f'Missing dependency: {exc.name}. Install with: python3 -m pip install Pillow numpy', file=sys.stderr)
    sys.exit(2)

PROFILES = ['editorial-bold', 'screenshot-editorial', 'early-playful']


def color_hex(rgb):
    return '#' + ''.join(f'{int(c):02X}' for c in rgb)


def color_stats(pixels):
    f = pixels.astype(np.float32) / 255
    maximum, minimum = f.max(axis=1), f.min(axis=1)
    saturation = np.divide(maximum - minimum, maximum, out=np.zeros_like(maximum), where=maximum != 0)
    luma = f @ np.array([.2126, .7152, .0722], dtype=np.float32)
    ids = (pixels[:, 0].astype(np.int32) // 8 * 1024
           + pixels[:, 1].astype(np.int32) // 8 * 32 + pixels[:, 2].astype(np.int32) // 8)
    counts = np.bincount(ids, minlength=32768)
    palette = []
    for index in np.argsort(-counts, kind='stable')[:6]:
        if not counts[index]:
            continue
        palette.append({'rgb_candidate': color_hex(np.median(pixels[ids == index], axis=0).astype(np.uint8)),
                        'bin_share': round(float(counts[index] / len(pixels)), 6)})
    return {'dark_pixel_share': round(float((luma < .25).mean()), 6),
            'bright_low_saturation_share': round(float(((maximum >= .85) & (saturation <= .12)).mean()), 6),
            'mean_srgb_luma': round(float(luma.mean()), 6),
            'mean_saturation': round(float(saturation.mean()), 6),
            'palette_candidates': palette}


def estimate_grid(a):
    """Detect repeated vertical dark line peaks in visually blank top strips only."""
    h, w = a.shape[:2]
    rejected = []
    for start, end in [(.006, .028), (.03, .048)]:
        y0, y1 = max(0, int(h * start)), max(1, int(h * end))
        x0, x1 = int(w * .02), int(w * .98)
        band = a[y0:y1, x0:x1].astype(np.float32)
        luma = band @ np.array([.2126, .7152, .0722], dtype=np.float32)
        dark_share = float((luma < 190).mean())
        if dark_share > .01:
            rejected.append(f'Top band {start:.3f}–{end:.3f}H contains dark content ({dark_share:.2%}); not treated as blank.')
            continue
        darkness = np.median(255 - luma, axis=0)
        baseline = float(np.median(darkness))
        mad = float(np.median(np.abs(darkness - baseline)))
        threshold = baseline + max(1.5, 4 * mad)
        above = np.flatnonzero(darkness > threshold)
        if not len(above):
            rejected.append('No column peak exceeds the blank-band noise threshold.')
            continue
        # JPEG ringing around a single line should not produce multiple peaks.
        groups = np.split(above, np.where(np.diff(above) > max(3, round(w * .012)))[0] + 1)
        centers, contrasts = [], []
        for group in groups:
            if len(group) == 0 or group[-1] - group[0] > w * .022:
                continue
            weights = np.maximum(0, darkness[group] - baseline)
            centers.append(float(np.average(group, weights=weights)) + x0)
            contrasts.append(float(darkness[group].max() - baseline))
        if len(centers) < 4:
            rejected.append(f'Only {len(centers)} narrow candidate peaks; insufficient repetition.')
            continue
        gaps = np.diff(centers)
        period = float(np.median(gaps))
        cv = float(np.std(gaps) / np.mean(gaps))
        contrast = float(np.median(contrasts))
        if not (.025 * w <= period <= .20 * w) or cv > .12 or contrast < 1.5:
            rejected.append(f'Candidate repetition is unreliable (gap CV {cv:.3f}, median contrast {contrast:.2f}/255).')
            continue
        confidence = 'high' if len(centers) >= 6 and cv <= .06 and contrast >= 2 else 'medium'
        return {'status': 'estimated', 'confidence': confidence,
                'vertical_line_period_px': round(period, 2),
                'vertical_line_period_fraction_of_width': round(period / w, 6),
                'blank_band_y_px': [y0, y1], 'search_x_px': [x0, x1],
                'candidate_line_centers_x_px': [round(v, 2) for v in centers],
                'candidate_count': len(centers), 'gap_coefficient_of_variation': round(cv, 4),
                'median_peak_contrast_0_255': round(contrast, 2),
                'qualification': 'Heuristic evidence for vertical repeated lines only. Does not establish a square grid or horizontal spacing; not a calibrated probability.'}
    return {'status': 'unknown', 'confidence': 'unknown', 'vertical_line_period_px': None,
            'reasons': rejected, 'qualification': 'Unknown does not mean a grid is absent; it means these top strips do not provide reliable evidence.'}


def inspect(path):
    with Image.open(path) as opened:
        source_size, format_name, mode = list(opened.size), opened.format, opened.mode
        alpha = 'A' in opened.getbands() or 'transparency' in opened.info
        frame_count = int(getattr(opened, 'n_frames', 1))
        opened.load()
        image = ImageOps.exif_transpose(opened).convert('RGB')
        a = np.asarray(image)
    h, w = a.shape[:2]
    step = max(1, math.ceil(math.sqrt(w * h / 262144)))
    sampled = a[::step, ::step]
    sh, sw = sampled.shape[:2]
    ch, cw = max(1, sh // 10), max(1, sw // 10)
    corners = np.concatenate([sampled[:ch, :cw].reshape(-1, 3), sampled[:ch, -cw:].reshape(-1, 3),
                              sampled[-ch:, :cw].reshape(-1, 3), sampled[-ch:, -cw:].reshape(-1, 3)])
    corner_stats = color_stats(corners)
    ratio = w / h
    ratio_close = abs(ratio / .75 - 1) <= .01
    reminders = []
    if not ratio_close:
        reminders.append('Aspect differs by more than 1% from 3:4. This is a soft reminder; original corpus includes one 2:3 image.')
    if alpha:
        reminders.append('Input has transparency. RGB diagnostics use stored RGB values without compositing; appearance depends on the eventual background.')
    if frame_count > 1:
        reminders.append(f'Input has {frame_count} frames; diagnostics use the first frame only.')
    return {'path': str(path.resolve()), 'decodable': True, 'format': format_name, 'source_mode': mode,
            'source_dimensions_px': source_size, 'exif_corrected_dimensions_px': [w, h],
            'aspect_width_over_height': round(ratio, 6), 'approximately_3_to_4': ratio_close,
            'file_bytes': path.stat().st_size, 'frame_count': frame_count, 'has_transparency': alpha,
            'sampling': {'step': step, 'sample_pixels': int(sampled.shape[0] * sampled.shape[1]),
                         'method': 'Original RGB pixels [::step, ::step], no resizing/interpolation; step=ceil(sqrt(width*height/262144)).'},
            'colors': color_stats(sampled.reshape(-1, 3)),
            'corner_background_candidates': corner_stats['palette_candidates'][:3],
            'corner_qualification': 'Candidates from four 10%-by-10% corners only. Illustration, shadows and decorations at corners can dominate; not a definitive background token.',
            'grid': estimate_grid(a), 'reminders': reminders}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('image', type=Path)
    parser.add_argument('--reference', type=Path)
    parser.add_argument('--profile', choices=PROFILES, default='editorial-bold')
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    report = {'schema_version': 1, 'profile': args.profile,
              'profile_role': 'Records the intended profile for human review; profile is not inferred and does not change measurement thresholds.',
              'method_notes': ['Dark means sRGB weighted luma <0.25; bright/low-saturation means HSV V>=0.85 and S<=0.12.',
                               'Palette uses RGB bins of width 8/255 per channel, reporting median observed RGB per bin; compressed pixels do not reveal original fill tokens.',
                               'There is no comprehensive style score, SSIM or full-image difference score. Text accuracy, layout, line weight and aesthetics need visual review.']}
    exit_status = 0
    try:
        report['image'] = inspect(args.image)
        if args.reference:
            report['reference'] = inspect(args.reference)
            difference = {}
            for key in ['dark_pixel_share', 'bright_low_saturation_share', 'mean_srgb_luma', 'mean_saturation']:
                difference[key] = round(report['image']['colors'][key] - report['reference']['colors'][key], 6)
            report['reference_comparison'] = {
                'image_minus_reference': difference,
                'aspect_width_over_height_difference': round(report['image']['aspect_width_over_height'] - report['reference']['aspect_width_over_height'], 6),
                'qualification': 'Descriptive measurements only. Different content can legitimately change every metric; no aesthetic similarity conclusion follows from these differences.'}
    except Exception as exc:
        report['error'] = {'type': type(exc).__name__, 'message': str(exc)}
        if 'image' not in report:
            report['image'] = {'path': str(args.image.resolve()), 'decodable': False}
        exit_status = 2
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    if exit_status:
        print(f"Inspection failed: {report['error']['message']}", file=sys.stderr)
    else:
        result = report['image']
        w, h = result['exif_corrected_dimensions_px']
        c = result['colors']
        grid = result['grid']
        grid_text = f"{grid['vertical_line_period_px']} px ({grid['confidence']})" if grid['status'] == 'estimated' else 'unknown'
        print(f"Readable {result['format']}: {w} x {h}; aspect {result['aspect_width_over_height']:.6f}; approximately 3:4: {result['approximately_3_to_4']}.")
        print(f"Sampled dark {c['dark_pixel_share']:.2%}; bright/low-saturation {c['bright_low_saturation_share']:.2%}; grid period: {grid_text}.")
        print('RGB candidates: ' + ', '.join(v['rgb_candidate'] for v in c['palette_candidates']))
        for message in result['reminders']:
            print('Reminder: ' + message)
        if args.reference:
            print('Reference descriptive differences are included; no style-similarity score is computed.')
        if args.out:
            print(f'Report: {args.out.resolve()}')
    return exit_status


if __name__ == '__main__':
    sys.exit(main())
