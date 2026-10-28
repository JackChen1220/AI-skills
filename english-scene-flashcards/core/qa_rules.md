# Core QA Rules

## Hard QA dimensions
### Data QA
- exact English string;
- exact IPA when supplied;
- exact Chinese gloss;
- correct curriculum identity/sense;
- no duplicated/missing target.

### Semantic QA
- scene communicates intended textbook sense;
- target object/action/state is present and distinguishable;
- no misleading substitute.

### Mapping QA
- connector/no-connector behavior matches mapping mode;
- endpoint lands on the semantic target or relation/action zone;
- context words are not forced onto random objects.

### Layout QA
- labels readable and inside safe area;
- no label covers faces, hands, key actions or target objects;
- adequate padding and spacing;
- no avoidable long connector geometry;
- target count is appropriate for the layout template.

### Connector QA
- token is `connector.v3.light`;
- lines are pale, thin and low-salience;
- no red/orange/yellow beads;
- no avoidable crossings;
- platform-specific hard length thresholds pass.

### Style QA
- batch style is coherent;
- no instructional pseudo-text or misleading readable signage; incidental microtexture is assessed by its impact below;
- no rendering-family drift;
- no edge artifacts, blur blobs or unexplained shapes.

### Provenance QA
- Stage 08 teaching text came from authoritative data;
- active Skill version and Adapter recorded;
- final filename/card ID unique.
- reviewed artifacts have current hashes; a base, content or layout change invalidates the corresponding prior visual/data approval.
- actual base and composed view were inspected; `humanReviewed=false` for Agent vision, with evidence and truthful scope. Do not infer visual approval from file existence or data-only checks.

## Hard failures versus cosmetic warnings
Wrong teaching text/IPA/sense, missing targets, misleading scenes, unreadable cards, material face/hand/action occlusion and major style drift block approval. Generated teaching typography in the base always fails.

Harmless paper texture, small seams or similar non-instructional details may be `WARN` with an explicit acceptance reason when consistent with the user's requested detail level. Do not call them perfect or encode a new ad-hoc check enum: use the schema's `WARN`, notes and evidence. A warning cannot excuse instructional pseudo-text or a misleading label. A minor edge overlap that leaves the target and action clear is not automatically a hard failure.

Review the base and composed view once, using a combined board if helpful. Enlarge a region only for a concrete concern; do not repeatedly search an otherwise accepted image for microscopic defects. Prefer content/layout repairs over regeneration. Once required checks pass, stop that card's routine repair loop and finish the batch.

For `app_bundle`, also check vocabulary/learning consistency, per-term example/exercise coverage, in-bounds layout, dimensions and current hashes. Run the target application's real data validator. Required checks passing is distinct from publishing the material.

## Standard error codes
`SOURCE_DATA_AMBIGUOUS`
`COVERAGE_ERROR`
`SCENE_GROUP_WEAK`
`BASE_TEXT_CONTAMINATION`
`TARGET_MISSING`
`TEXT_ERROR`
`LINE_MAPPING_ERROR`
`LAYOUT_COLLISION`
`STYLE_FAIL_CONNECTOR_V3`
`STYLE_DRIFT`
`COMPOSER_UNAVAILABLE`

Platform Adapters may add codes but may not weaken these gates.
