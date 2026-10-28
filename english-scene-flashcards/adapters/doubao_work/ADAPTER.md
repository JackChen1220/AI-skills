# Doubao Work Adapter — compatible with Skill V2.2.2

## Purpose
Adapt the Agent-Agnostic flashcard production protocol to observed Doubao Work behavior.

This adapter exists because Doubao Work tends to:
- shrink label cards and teaching text too aggressively;
- place labels on extreme canvas edges, producing very long connector lines;
- render connector paths across large parts of the illustration;
- introduce arbitrary red/blue accent bars on label cards;
- generate incidental or garbled signage/text in the scene;
- drift between watercolor, chibi, semi-3D, and anime-like illustration styles;
- anchor abstract/action words to arbitrary faces or objects;
- prefer semantic-category grouping over plausible single-scene co-occurrence.

The Core Skill rules remain authoritative. This adapter only changes execution and layout thresholds for Doubao Work.

---

## 1. Production Architecture — Mandatory

Doubao Work MUST follow the same two-layer architecture:

1. Stage 07: generate **base illustration only**.
2. Stage 08: deterministic composition of word / IPA / Chinese / label card / connector.

The final teaching text MUST NOT be trusted to the image generator.

If Doubao Work cannot perform deterministic Stage 08 composition, output state is `MOCKUP_ONLY` and MUST NOT be marked `APPROVED`.

---

## 2. Canvas

Observed Doubao output: `1536 × 2048`, portrait 3:4.

This adapter supports that canvas directly. Do not shrink the teaching UI simply because the canvas is large.

Safe margin:
- horizontal: at least 46 px (3% of width)
- vertical: at least 50 px (2.5% of height)

No label card may touch or visually merge with the canvas edge.

---

## 3. Label Card Scale — Doubao Override

Doubao's default label cards are too small. Stage 08 MUST use the following minimum visual scale.

### English word
- preferred: 60–76 px on 1536×2048
- hard minimum: 54 px
- bold, deep navy
- do not shrink below minimum to fit long words

### IPA
- preferred: 34–42 px
- hard minimum: 30 px

### Chinese gloss
- preferred: 34–42 px
- hard minimum: 30 px

### Card dimensions
Choose by density rather than one fixed size:
- short word: width 280–360 px, height 155–205 px
- normal word: width 330–430 px, height 165–220 px
- long phrase/proper noun: width 420–600 px, height 175–245 px

For long English terms, enlarge or wrap the card. Never solve fit by making all typography tiny.

### Padding
- horizontal internal padding: >= 28 px
- vertical internal padding: >= 22 px

---

## 4. Label Visual Style

Use the Core V2 label system:
- white / warm-white rounded rectangle
- soft shadow
- no heavy border
- deep navy English
- subordinate IPA and Chinese

### Accent-bar override
Observed Doubao output adds random blue/red vertical bars.

Default: **disable accent bars entirely**.

If the platform template cannot disable them:
- use ONE uniform low-saturation blue-gray accent only;
- color: approximately `#B7C6D8`;
- max width: 4 px;
- never use red/orange/yellow category bars unless the curriculum explicitly defines a semantic code.

---

## 5. Connector V3 — Doubao Geometry Override

Use `connector.v3.light`:
- line color: `#B7C6D8`
- width: 2–3 px
- opacity: ~78%
- target endpoint dot: 6–8 px cool gray-blue
- no red/orange/yellow beads
- no start dot at label edge by default

### Critical Doubao rule: line length ceiling
The observed problem is not mainly line color; it is excessive geometry.

For 1536×2048:
- ideal connector length: <= 420 px
- soft warning: > 420 px
- hard fail: > 600 px

Equivalent normalized rule:
- ideal <= 0.27 × canvas width
- hard max <= 0.39 × canvas width

If a connector would exceed the hard max:
1. move the label closer to the target;
2. choose a nearer label zone;
3. reduce target count / redesign scene if necessary;
4. NEVER solve the problem by drawing a longer line.

### Connector routing
- use shortest visually clear path;
- originate from nearest label-card edge;
- terminate on the semantic target feature;
- do not pass through faces, hands, or unrelated vocabulary targets;
- avoid crossing another connector;
- no connector should traverse the full height of the card.

---

## 6. Label Placement Strategy — Connector-First

Doubao tends to pin all cards to the top/bottom perimeter. Replace this with **connector-first placement**.

For each target:
1. locate semantic anchor;
2. choose the nearest safe label zone;
3. test connector length;
4. move the card inward if needed;
5. only then finalize layout.

Direct/action labels may float nearer the subject instead of staying at extreme corners.

Context labels (`scene_state`, `dialogue_phrase`, `timeline_segment`, `comparison_zone`) use no connector and may occupy a clean context band.

---

## 7. Mapping Rules — Strict

Observed Doubao failure: labels sometimes point to a face because it is visually convenient rather than semantically correct.

Apply Core mapping modes strictly:
- `direct_anchor`: point to the visible object/body part/person
- `action_anchor`: point to the action zone (hand + tool + movement), not the actor's face by default
- `scene_state`: no connector
- `dialogue_phrase`: no connector
- `timeline_segment`: no connector
- `comparison_zone`: no connector
- `relation_anchor`: point to the relation zone, not an arbitrary endpoint

Examples:
- `clean`: do not point to the child's face; show cleaning action/state
- `strong`: do not point to a cheek; use action/body evidence or context card
- `Chinese`: do not point to a bookshelf; use a language/context representation
- `photo`: point to an actual photo/frame if used as a direct target

---

## 8. Base Illustration Text Contamination

Doubao frequently invents store signs, posters, labels, license plates, and book-cover text.

Stage 07 negative constraints MUST explicitly include:
- no readable signage
- no readable posters
- no readable product packaging
- no readable book titles
- no readable license plates
- no decorative pseudo-text
- blank signs/posters where needed

Any garbled text-like pixels near an instructional target are a Stage 09 style/data contamination warning.

---

## 9. Style Lock

Observed style drift across a single batch is unacceptable.

Every Stage 07 prompt MUST repeat an immutable style block:
- warm 2D children's storybook/textbook illustration
- soft texture
- rounded anatomy
- controlled saturation
- clean silhouettes
- no 3D rendering
- no semi-realistic anime
- no glossy toy look

When Doubao Work supports reference images, attach the same Golden Style Reference to every card in the batch.

Hard fail if one batch mixes substantially different rendering families.

---

## 10. Grouping Guardrail

Doubao may group words because they share a semantic category rather than because they form a natural scene.

Before Stage 04, require a single-scene plausibility check:
- Can all targets appear naturally in one frame?
- Are targets simultaneously visible without contrivance?
- Does the scene communicate the textbook sense of each term?

If not, split or use a special comparison/category template.

Examples observed as weak/forced:
- unrelated occupations placed together simply because all are jobs;
- personality adjective + body-part combinations without a story;
- abstract attributes mapped onto arbitrary portraits.

---

## 11. Doubao-Specific QA Gates

Add these checks to Stage 09:

### `DOUBAO_LABEL_TOO_SMALL`
Fail when:
- English < 54 px on 1536×2048;
- IPA or Chinese < 30 px;
- card padding is visibly cramped.

### `DOUBAO_CONNECTOR_TOO_LONG`
Fail when connector > 600 px or > 0.39×canvas width.
Warn when > 420 px.

### `DOUBAO_LABEL_EDGE_PINNING`
Fail when an edge-pinned label creates an avoidable long connector.

### `DOUBAO_RANDOM_ACCENT_COLOR`
Fail when red/orange/blue accent bars vary without defined semantic meaning.

### `DOUBAO_BASE_TEXT_CONTAMINATION`
Fail/warn on invented readable or pseudo-readable signage in the base illustration.

### `DOUBAO_STYLE_DRIFT`
Fail if the batch mixes 2D storybook, 3D, semi-realistic anime, or materially different character systems.

### `DOUBAO_ANCHOR_SEMANTIC_ERROR`
Fail when a connector terminates on a visually convenient but semantically wrong feature.

---

## 12. Recommended Doubao Work Workflow

`Core Stage 01–06`
→ Stage 07: one card / one image generation, base illustration only
→ validate zero-text + style lock
→ Stage 08: deterministic overlay with enlarged Doubao label scale
→ run connector-first layout with hard length ceiling
→ Stage 09: Core QA + Doubao QA overrides
→ Stage 10: repair smallest failing layer
→ Stage 11: approve only after all hard gates pass
