#!/usr/bin/env python3
"""Report pixel-level stats for FAQ icon PNG files."""

from __future__ import annotations

import json
import math
import sys
from collections import Counter
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required: python3 -m pip install pillow") from exc


def quantize_channel(value: int) -> int:
    return max(0, min(255, round(value / 16) * 16))


def inspect(path: Path) -> dict:
    image = Image.open(path).convert("RGBA")
    width, height = image.size
    if hasattr(image, "get_flattened_data"):
        pixels = list(image.get_flattened_data())
    else:
        pixels = list(image.getdata())

    xs: list[int] = []
    ys: list[int] = []
    color_bins: Counter[tuple[int, int, int]] = Counter()

    for index, (red, green, blue, alpha) in enumerate(pixels):
        if alpha > 10:
            xs.append(index % width)
            ys.append(index // width)
        if alpha > 40:
            color_bins[
                (
                    quantize_channel(red),
                    quantize_channel(green),
                    quantize_channel(blue),
                )
            ] += 1

    if xs:
        bbox = [min(xs), min(ys), max(xs) + 1, max(ys) + 1]
        coverage = len(xs) / (width * height) * 100
        margins = [bbox[0], bbox[1], width - bbox[2], height - bbox[3]]
    else:
        bbox = [0, 0, 0, 0]
        coverage = 0
        margins = [width, height, width, height]

    visible_color_count = sum(color_bins.values()) or 1
    colors = []
    for (red, green, blue), count in color_bins.most_common(8):
        colors.append(
            {
                "hex": f"#{red:02X}{green:02X}{blue:02X}",
                "pct_visible": round(count / visible_color_count, 4),
            }
        )

    return {
        "file": str(path),
        "size": [width, height],
        "visible_bbox": bbox,
        "transparent_margins": margins,
        "visible_coverage_pct": round(coverage, 2),
        "dominant_colors": colors,
        "circle_coverage_delta_from_pi_over_4": round(coverage - (math.pi / 4 * 100), 2),
    }


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: audit_png.py <icon.png> [more-icons.png ...]", file=sys.stderr)
        return 2

    results = [inspect(Path(arg)) for arg in argv[1:]]
    payload = results[0] if len(results) == 1 else results
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
