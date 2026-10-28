# Scene Brief Rules

Every term must have exactly one `target_spec`.

## Mapping modes
### `direct_anchor`
Concrete visible object/person/body part/place.
Default connector: `required`.

### `action_anchor`
Meaning is expressed by an action zone.
Default connector: `optional`.
Point to the action evidence, not a convenient face.

### `scene_state`
Global state/attribute of a subject or scene.
Default connector: `none`.

### `dialogue_phrase`
Function/discourse/degree word or phrase requiring language context.
Default connector: `none`.

### `timeline_segment`
Temporal meaning best represented by sequence/duration.
Default connector: `none`.

### `comparison_zone`
Change/difference/choice meaning represented by A/B comparison.
Default connector: `none`.

### `relation_anchor`
Spatial/directional/ownership relation.
Default connector: `optional`.
Anchor the relation zone, not an arbitrary endpoint.

## Scene Brief Gate
Before Stage 05:
1. every term has one mapping mode;
2. every term has one connector policy;
3. abstract/function words are not forced onto arbitrary physical targets;
4. composition leaves usable label space;
5. base illustration can be generated with zero teaching text.

In the declared Speak Replay context-card profile, connector policy is `none` for every term while mapping modes still describe the teaching mechanism. Abstract terms must be supported by scene context and natural example sentences; do not fabricate physical anchors.
