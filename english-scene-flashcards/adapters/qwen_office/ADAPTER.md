# Qwen Office Adapter — compatible with Skill V2.2.2

## Purpose
Adapt the Agent-Agnostic flashcard production protocol to observed **Qwen Office / 千问办公** behavior.

Qwen Office is generally stronger than the observed Doubao Work output in label readability, layout cleanliness, and concrete-object rendering. However, the observed production batch shows recurring failure modes that require platform-specific execution rules:

- labels are often pinned to fixed perimeter/corner positions even when the target is far away;
- connector lines become unnecessarily long because layout is label-first rather than target-first;
- abstract, relational, possessive, discourse, and degree words are forced into ordinary object-identification cards;
- heterogeneous word groups are placed in one scene even when they use different visual teaching mechanisms;
- some connector endpoints land near a target rather than on the semantically correct feature;
- multi-region/cutaway scenes create long vertical lines and crowded perimeter labels;
- visually similar same-category objects are insufficiently differentiated (for example multiple school books);
- some cards contain excessive empty space while targets remain small;
- context labels can be visually remote from the character/action they explain;
- edge blur, residual artifacts, or incidental pseudo-text can remain in otherwise clean output.

The Core Skill remains authoritative. This adapter may tighten routing, grouping, layout, connector, and QA thresholds, but MUST NOT weaken Core hard gates.

---

## 1. Mandatory Production Architecture

Qwen Office MUST follow the Core two-layer architecture:

1. **Stage 07 — Base Illustration Only**
   - no English teaching text
   - no IPA
   - no Chinese gloss
   - no label cards
   - no connector lines or dots

2. **Stage 08 — Deterministic Compose**
   - authoritative English / IPA / Chinese from curriculum source
   - label cards from design tokens
   - connector geometry from LayoutSpec + `connector.v3.light`

If deterministic Stage 08 composition is unavailable, the output state is `MOCKUP_ONLY` and MUST NOT become `APPROVED`.

---

## 2. Qwen Card-Type Router — Required Before Scene Brief

Observed Qwen failure: it can draw a visually pleasant scene even when the vocabulary group is pedagogically incompatible. Therefore every planned card MUST be routed to a card type before Stage 04.

### Q1 — Object / Place Card
Use for concrete nouns and places that can be visually identified directly.

Examples:
- classroom
- blackboard
- computer
- fridge
- soup
- hat
- glasses

Preferred mapping:
- mostly `direct_anchor`
- 3–4 targets preferred
- 5 targets allowed only when the scene remains uncluttered

### Q2 — Action Card
Use for verbs/actions whose meaning is visible in a single action.

Examples:
- clean
- help
- find
- play
- buy
- swim

Preferred mapping:
- `action_anchor`
- point to the action zone, not merely the actor's face

### Q3 — Relation / Possession Card
Use for relationship, ownership, spatial, or pronoun concepts.

Examples:
- near
- his
- her
- them

Preferred mapping:
- `relation_anchor` or `dialogue_phrase`
- avoid ordinary object-pointer treatment
- design the relation explicitly into the scene

### Q4 — Choice / Contrast / Judgment Card
Use for functional words or evaluative concepts that require alternatives or a decision.

Examples:
- or
- right
- wrong
- different

Preferred mapping:
- `comparison_zone` or `dialogue_phrase`
- use A/B contrast, choice, or question-answer context
- no arbitrary object connector

### Q5 — Dialogue / Discourse / Degree Card
Use for discourse markers, degree words, exclamations, and words whose meaning depends on a sentence or utterance.

Examples:
- really
- wow
- so much
- because
- then
- if

Preferred mapping:
- `dialogue_phrase`
- no ordinary connector
- use a short micro-dialogue/context zone during deterministic composition when product rules permit

### Q6 — Narrative Micro-Story Card
Use when terms form a short event chain.

Examples:
- lost / find / them
- clean / help
- visit / grandparent

Preferred mapping:
- mix of `action_anchor`, `scene_state`, `dialogue_phrase`, or `relation_anchor`
- one coherent event, not a category poster

### Q7 — Spatial / Cutaway Card
Use for multiple rooms, regions, or fixed spatial zones.

Examples:
- bedroom / study / living room / kitchen / bathroom

Rules:
- use local labels placed close to each region;
- do not force all labels to the outermost perimeter;
- prefer 3–4 regions per card;
- for 5+ regions, split the card or use embedded/local-label layout with no long connector lines.

---

## 3. Grouping Guardrail — Semantic Mechanism Consistency

Before Stage 04, a card must pass BOTH tests:

### A. Single-scene plausibility
Can all targets appear naturally in one coherent frame without contrivance?

### B. Teaching-mechanism compatibility
Do the targets use compatible visual teaching mechanisms?

A card should normally contain terms from one dominant mechanism:
- concrete object identification;
- action/event;
- relation/possession;
- contrast/choice;
- discourse/dialogue;
- timeline/narrative.

### Split or reroute when mechanisms conflict
Observed weak combinations include patterns like:
- `wall / fan / floor / near` — concrete objects + relation word;
- `clean / help / really` — two actions + degree/discourse word;
- `lost / wow / cute / so much` — event state + exclamation + adjective + degree phrase;
- `his / her / or / right` — possession + conjunction + judgment.

The model MUST NOT preserve a weak group simply to hit a target word count.

---

## 4. Target Count

Qwen can visually fit many labels, but pedagogical density becomes weak before visual density does.

Recommended:
- **3–4 targets per card**: preferred
- **5 targets**: allowed only when all are strongly coherent and spatially distinct
- **6+ targets**: split unless using a purpose-built category/spatial template

Special exception:
- food/table cards or clearly separated object arrays may use 5 when connectors remain short and targets are distinct.

---

## 5. Label Card Scale — Qwen Guidance

Observed Qwen labels are generally more readable than Doubao labels. Do NOT blindly enlarge them. Instead use density-adaptive sizing and protect scene area.

For a 1536 × 2048 portrait canvas, recommended ranges:

### English
- preferred: 60–76 px
- hard minimum: 54 px

### IPA
- preferred: 32–40 px
- hard minimum: 28 px

### Chinese
- preferred: 32–40 px
- hard minimum: 28 px

### Label width
- short word: 270–350 px
- normal word: 320–420 px
- long phrase: 420–620 px

Long phrases MUST expand/wrap the card rather than shrinking all typography.

### Density rule
If label cards cover more than approximately 28% of the usable scene area, first:
1. reduce target count;
2. move to a special layout;
3. split the card;

Do not simply make the scene smaller.

---

## 6. Connector V3 — Qwen Geometry Override

Use Core `connector.v3.light`:
- line color: `#B7C6D8`
- line width: 2–3 px on 1536×2048 reference canvas
- opacity: ~78%
- endpoint dot: 6–8 px cool gray-blue
- no red/orange/yellow bead
- no start dot by default

### Qwen-specific connector length targets
Qwen often creates long lines because labels remain at fixed corners.

Normalized thresholds:
- **preferred**: <= 0.24 × canvas width
- **warning**: > 0.30 × canvas width
- **hard fail**: > 0.42 × canvas width

For 1536 px width, approximately:
- preferred <= 370 px
- warning > 460 px
- hard fail > 645 px

If a line exceeds warning level, attempt label relocation before approval.
If a line exceeds hard max, layout MUST be repaired.

### Connector-first placement
For every connector-bearing target:
1. locate semantic target anchor;
2. calculate nearest safe label zone;
3. place label near the target;
4. calculate route length;
5. reroute or relocate until within threshold;
6. only then finalize other labels.

Do NOT start from fixed top-left / top-right / bottom-left / bottom-right slots.

---

## 7. Connector Semantic Endpoint Rule

Observed Qwen issue: some lines terminate in empty space, on a face, or near rather than on the intended semantic feature.

Endpoints MUST land on the semantic target feature:
- `hat` -> hat body/brim, not air above the head;
- `glasses` -> eyeglass frame, not hair/forehead;
- `shoe` -> shoe body;
- `fan` -> fan body;
- `picture` -> picture/frame;
- `teacher's desk` -> desk body, not arbitrary foreground area;
- action verbs -> hand/tool/action region where possible.

`scene_state`, `dialogue_phrase`, `timeline_segment`, and `comparison_zone` default to **no connector**.

---

## 8. Context-Label Proximity Rule

Words such as personality adjectives, state words, or discourse words often need no connector, but the label still must be clearly associated with the correct subject/context.

For no-line contextual labels:
- place the label near the relevant character or context zone;
- avoid placing a label at the opposite edge of the card from its semantic subject;
- if two characters could plausibly match the adjective, use stronger pose/action cues or move the label closer.

Examples:
- `strong`: place near the flexing/strength-demonstrating character; no face connector.
- `friendly`: place near the greeting/helping character.
- `quiet`: place near the reading/shushing character.

---

## 9. Abstract / Function Word Guard

The following classes MUST NOT be treated as normal object labels:
- conjunctions: `or`, `because`, `if`, `then`
- degree/discourse: `really`, `so much`, `wow`
- possession/pronoun relations: `his`, `her`, `them`
- judgment: `right` when meaning correct
- relational terms: `near`

Required action:
- reroute to appropriate card type;
- use `dialogue_phrase`, `comparison_zone`, or `relation_anchor`;
- default to no connector unless a real visual relation exists.

---

## 10. Same-Category Object Differentiation

When several targets are visually similar members of one category, each must be identifiable without relying only on its label.

Example: school books.
- `maths book`: geometry/numbers/ruler motif;
- `English book`: ABC/letters/world-language motif;
- `Chinese book`: Chinese-cultural/character-learning visual motif, but no generated readable characters unless added deterministically;
- `storybook`: story/fairy-tale character or castle motif.

Rules:
- vary cover color + icon language + silhouette when possible;
- direct connector to the target book body/cover center;
- Stage 09 must verify the object is recognizable without depending solely on its label.

---

## 11. Multi-Region / Cutaway Layout

Observed issue: house cutaway scenes create long lines from corner labels to distant rooms.

For `Spatial / Cutaway` cards:
- use local labels adjacent to each room/region;
- local label cards may be smaller than standard perimeter cards only if typography minimums remain satisfied;
- no connector longer than one region height;
- prefer connector-free local labels when room boundary itself is unambiguous;
- maximum 4 regions per standard card;
- 5+ regions -> split or dedicated map-style layout.

Do not use a normal perimeter-label template for a cutaway map.

---

## 12. Scene Scale / Empty-Space Guard

Observed Qwen output is clean but can devote too much space to empty wall/floor/background while vocabulary targets remain small.

Stage 05/07 requirements:
- primary teaching targets should occupy a meaningful portion of the frame;
- reduce non-instructional empty wall/floor when it causes long connector geometry;
- zoom/crop closer for small target sets;
- reserve negative space intentionally for labels, not as uncontrolled blank area.

Warning if more than ~40% of the scene is visually empty AND connector-bearing targets remain small/distant.

---

## 13. Generated Text / Artifact Guard

Base illustration negative constraints MUST include:
- no readable signs;
- no readable book titles;
- no classroom poster text;
- no pseudo-text;
- no decorative letters/numbers unless deterministically overlaid later.

Stage 09 must also check:
- edge blur or unmotivated smudges;
- residual image-generation artifacts near corners;
- labels cut off by edge;
- connector extending outside safe area;
- duplicate or orphan connector endpoint dots.

---

## 14. Qwen-Specific QA Codes

Add these to Stage 09.

### `QWEN_FORCED_OBJECT_MAPPING`
Fail when an abstract/functional/relational term is treated as a concrete object target.

### `QWEN_CONNECTOR_TOO_LONG`
Warn > 0.30×canvas width. Fail > 0.42×canvas width.

### `QWEN_CONNECTOR_ENDPOINT_MISS`
Fail when line endpoint is in empty space or on the wrong semantic feature.

### `QWEN_CONTEXT_LABEL_TOO_REMOTE`
Fail/warn when a no-line adjective/state/context label is too far from the subject it explains and causes ambiguity.

### `QWEN_SEMANTIC_GROUP_MIX`
Fail when one card combines incompatible teaching mechanisms without a special narrative/contrast template.

### `QWEN_OBJECT_DIFFERENTIATION_WEAK`
Fail when same-category targets cannot be visually distinguished without reading the labels.

### `QWEN_CUTAWAY_OVERLOAD`
Fail when a standard perimeter-label layout is used for too many spatial regions, producing long lines/crowding.

### `QWEN_SCENE_EMPTYSPACE_OVERLOAD`
Warn/fail when excessive unused background reduces target scale or causes avoidable long connectors.

### `QWEN_LABEL_DENSITY_OVERLOAD`
Fail when target count/label area makes the teaching scene subordinate to UI.

### `QWEN_BASE_TEXT_CONTAMINATION`
Fail/warn on generated readable or pseudo-readable text in Stage 07 base illustration.

---

## 15. Recommended Qwen Office Workflow

`Core Stage 01–02`
→ Stage 03 grouping
→ **Qwen card-type routing + teaching-mechanism consistency gate**
→ Stage 04 Scene Brief
→ Stage 05 connector-first/local-label layout
→ Stage 06 prompt compile
→ Stage 07 one clean base illustration per card
→ verify no generated text + sufficient object differentiation
→ Stage 08 deterministic composition
→ Stage 09 Core QA + Qwen QA codes
→ Stage 10 smallest-layer repair
→ Stage 11 Approved export

---

## 16. Priority of Rules

When running Qwen Office:

1. `AGENT_CONTRACT.md`
2. Core Skill rules
3. `adapters/qwen_office/ADAPTER.md`
4. current task/card instructions

The Qwen adapter may tighten execution rules but may not override curriculum facts, Core hard gates, or active design tokens.
