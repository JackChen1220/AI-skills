---
name: generate-faq-icons
description: Generate, prompt, edit, or QA Webull-style FAQ and help-center category icons from short category names or semantic briefs. Use when Codex needs FAQ icon PNG or SVG assets matching the provided 108px circular finance/support icon system, including account, login, trading, investing, stock-market, transfer, tax, security, crypto, bond, premium, membership, promotion, support, and info categories.
---

# Generate FAQ Icons

## Core workflow

1. Read `references/icon-style.md` before creating or reviewing an icon.
2. Read `references/icon-inventory.md` when mapping a category name to an existing motif or choosing the closest precedent.
3. Use `assets/reference-contact-sheet.png`, `assets/reference-zoom-grid.png`, and `assets/source-icons/` as visual references when prompt-writing, redrawing, or checking a generated bitmap.
4. Create one icon per requested category unless the user asks for a set.
5. Export a transparent PNG at `108x108` by default. Produce SVG only when the user explicitly asks for vector output.
6. Run `scripts/audit_png.py <icon.png>` on finished PNGs and compare the result to the style tokens.

## Generation rules

- Interpret the category name first. Use the simplest literal motif that explains the FAQ category at small size.
- Keep the circular badge as the dominant object: a full-bleed colored circle on a transparent square canvas.
- Keep foreground symbols flat, mostly white, with one or two soft tint layers from the same hue family as the badge.
- Avoid photorealism, 3D, thin outline icons, dense detail, long labels, shadows outside the circle, and decorative backgrounds.
- Use text only for established financial abbreviations or category marks already present in the system, such as `IPO`, `ISA`, `IRA`, `FX`, and crypto glyphs.
- Treat flag icons, Webull Premium, and known membership marks as special cases that may fill the circle with brand or flag artwork rather than the normal white pictogram grammar.

## Prompt pattern

Use this compact pattern for raster image generation:

```text
Create a Webull FAQ category icon for "[category]": 108x108 transparent PNG, full-bleed circular badge, [palette token] background, centered [motif] pictogram, flat white foreground with subtle same-hue tint accents, simple rounded geometric shapes, crisp app-icon antialiasing, no outer shadow, no text except [allowed text if any].
```

For multiple icons, keep the camera, scale, circle size, foreground weight, and antialiasing identical across the set.

## QA checklist

- Canvas is `108x108` unless matching a legacy source asset exactly.
- Visible circle coverage is about `78%` to `80%` of the canvas.
- The badge touches all four canvas edges optically.
- Main foreground motif stays inside the central `24..84px` safe area unless it is a flag, abbreviation, or brand exception.
- Palette matches the semantic token in `references/icon-style.md`.
- Filename and visual metaphor match the FAQ category.
