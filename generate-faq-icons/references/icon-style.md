# FAQ Icon Style Tokens

Use these tokens to reproduce the icon system found in `assets/source-icons/`.

## Source Set Summary

- Source count: 44 PNG files.
- Standard canvas: 30 icons at `108x108`.
- Legacy canvases: eight at `111x108`, three at `110x110`, one at `96x96`, one at `100x100`, and one large source at `980x963`.
- New default export: `108x108` transparent PNG.
- Circle coverage: source icons cluster around `77%` to `80%` visible pixels, matching a full-bleed circle inside a square canvas.
- Source exceptions: `Foreexchange.png` is a high-resolution legacy export; `OnlineService.png` and `Webull Premium.png` are smaller legacy canvases. Do not use these sizes for new assets unless the user requests exact legacy matching.

## Canvas And Geometry

| Token | Value | Notes |
| --- | --- | --- |
| `canvas.size` | `108px x 108px` | Transparent outside the circular badge. |
| `badge.shape` | circle | Full-bleed, tangent to all four canvas edges. |
| `badge.diameter` | `108px` | Use `110px` only for flag legacy matching. |
| `badge.center` | `54px,54px` | Optical center for standard icons. |
| `badge.radius` | `54px` | Anti-aliased edge, no stroke. |
| `foreground.safe_area` | `x=24..84`, `y=24..84` | Default pictogram zone. |
| `foreground.compact_size` | `46..56px` | Wallet, shield, clipboard, gift, lock, chart. |
| `foreground.wide_size` | `68..76px` wide | Text marks such as `IPO`, `ISA`, `IRA`, `FX`, and membership marks. |
| `foreground.oversize` | up to circle edge | Flags and Webull Premium only. |
| `corner.radius.small` | `3..5px` | Inner card, receipt, chart bars. |
| `corner.radius.medium` | `6..10px` | Wallets, cards, documents, locks. |
| `gap.minimum` | `3..4px` | Interior negative spaces and separated symbol parts. |
| `gap.comfort` | `5..8px` | Between coin/arrow, chart/bar, card/link elements. |
| `edge.antialias` | `1..2px` | Keep soft bitmap antialiasing; avoid jagged hard masks. |

## Palette Tokens

Use one saturated badge color per icon, with subtle same-family variation for antialiasing, highlight, or depth.

| Token | Core hex | Use for |
| --- | --- | --- |
| `blue.brand.deep` | `#0B4EF3`, `#0447EC` | Webull brand, about, membership. |
| `blue.account` | `#308CFF` | Account, login, retirement, general account surfaces. |
| `blue.nav` | `#3B69FF` | Navigation, bonds, structured account documents. |
| `blue.info` | `#0E88DF` | Info/help meanings. |
| `cyan.transfer` | `#30C2FF`, `#3EC5FF` | Bank transfer, options, margin, money movement. |
| `cyan.fx` | `#1E91F3` to `#4FBFF9` | FX text or market data wave motifs. |
| `teal.secure` | `#0EDFD7` | Password/login, fractional shares, unlocked/secure utility. |
| `orange.trading` | `#FD774A`, `#FF7538`, `#FF8539` | Trading, documents, fees, rules, bank card binding, wealth. |
| `orange.crypto` | `#FF8C16` | Crypto and bitcoin. |
| `yellow.money` | `#FFB517` | Fixed investment, recurring deposit, ISA, market analysis. |
| `purple.transfer` | `#6D59FF`, `#8B59FF` | Asset transfer, P/L, promotions, short, foreign exchange. |
| `red.market` | `#FF3939`, `#FF5966` | China/HK markets, account opening emphasis. |
| `green.esg` | `#58B437` | Green bond and sustainability finance. |
| `white.foreground` | `#FFFFFF` | Primary pictogram fill. |

## Tint Tokens

Use tints as inner shadows, lower layers, or secondary planes. Keep them subtle and attached to the main symbol.

| Family | Tint examples |
| --- | --- |
| Blue | `#D1E5FF`, `#DCE4FF`, `#EEF2FF`, `#F5F9FF` |
| Cyan | `#C0ECFF`, `#DFF5FF`, `#EFFAFF` |
| Teal | `#B0FFFC`, `#C0FFFD`, `#D0FFFD` |
| Orange | `#FEE2D0`, `#FFE6DB`, `#FFECE5`, `#FFF3EE` |
| Yellow | `#FFE6B0`, `#FFEBC0`, `#FFF0D0`, `#FFF5E0` |
| Purple | `#CBB5FF`, `#D2BFFF`, `#DED0FF`, `#ECE4FF` |
| Green | `#D5F0CB`, `#DBF2D3`, `#E4F5DD` |
| Red | `#FFD1D5`, `#FFDFE2`, `#FFF0F1`, `#FFA1A1` |

## Shape Grammar

- Use filled geometric pictograms, not stroked line icons.
- Build symbols from rounded rectangles, circles, pills, triangles, and simple arrows.
- Keep the icon readable at `24x24` display size; remove detail before reducing foreground scale.
- Use one main symbol plus at most one supporting symbol. Examples: card plus link, coin plus arrow, chart plus leaf.
- Keep white foreground mass around `10%` to `18%` of the canvas for normal icons.
- Make foreground accents same-hue tints rather than gray shadows.
- Do not place shadows outside the badge. Depth appears only as internal tint layers or overlapping white/tint shapes.
- Align visually, not mechanically. The source set often shifts icons 1 to 3 px to balance arrows, text, or asymmetric symbols.

## Semantic Color Mapping

- Account/access: `blue.account`, or `red.market` for account opening.
- Support/info: `blue.info` or `blue.brand.deep`.
- Transfers/money movement: `cyan.transfer`, `purple.transfer`, or orange for card binding.
- Trading/investing: `orange.trading` or `yellow.money`.
- Crypto: `orange.crypto`.
- Market or country stock categories: flag circle when a country/region is named; otherwise use chart motifs.
- Security/fraud/password: `orange.trading` for fraud shield, `teal.secure` for password/login.
- Promotion/membership/premium: `purple.transfer` for promotions, `blue.brand.deep` for membership, premium artwork for premium.
- ESG or green finance: `green.esg`.

## Export Rules

- Prefer PNG for bitmap parity with the source set.
- Keep transparent pixels outside the circle.
- Avoid visible padding around the circle. The circle should touch the canvas bounds.
- Name files with clear category names. Preserve user-provided category wording unless they ask for normalization.
- If generating SVG, keep the same 108 viewBox, circle, fills, and safe areas; then rasterize to inspect parity if the final target is PNG.

## Pixel QA Targets

Run `scripts/audit_png.py` on outputs and compare:

- `size`: ideally `[108, 108]`.
- `visible coverage`: target `77%..80%`.
- `visible bbox`: should be the full canvas or within 1 px of it.
- `dominant colors`: first color should match the selected badge token.
- `transparent margins`: `0,0,0,0` for standard full-bleed circles.

If an icon fails only because it is a requested flag, brand, or legacy-size match, document the exception instead of forcing it into normal pictogram rules.
