# Connector System V3 — `connector.v3.light`

## Purpose
Connectors are a low-salience teaching aid, not decoration.

## Token
- line color: `#B7C6D8` pale gray-blue;
- visual width: approximately 2–3 px on a 1536 px-wide canvas, scale proportionally;
- opacity: approximately 78%;
- endpoint dot: 6–8 px cool gray-blue, optional 1 px white outline;
- default: no start dot at the label edge;
- no shadow, glow or gradient;
- prohibit red/orange/yellow anchor beads.

## Presence policy
- `direct_anchor`: required by default;
- `action_anchor`: optional;
- `relation_anchor`: optional;
- `scene_state`: none;
- `dialogue_phrase`: none;
- `timeline_segment`: none;
- `comparison_zone`: none.

The declared Speak Replay context-card profile sets all policies to `none`; retain each term's mapping mode in SceneBrief and record the profile. Connector styling/geometry checks are `N/A` when no connectors are used, not fabricated passes. The general defaults above remain unchanged for other runs.

## Routing
- choose the shortest clear path;
- originate from the nearest label edge;
- do not cross faces, hands, other labels or unrelated target objects;
- avoid connector crossings;
- if the line is long, move the label before accepting a long line;
- platform Adapters may impose stricter normalized length ceilings.
