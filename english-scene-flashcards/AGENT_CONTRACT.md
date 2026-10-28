# Agent Contract 1.1

## 1. Purpose
This contract defines what **any Agent** must read, produce, validate, and preserve to execute the flashcard Skill without relying on previous conversation history.

Current user instructions and platform constraints govern the task. Package defaults do not override them. The 1.1 contract adds `app_bundle` delivery while retaining `composed_png`; existing artifacts need not be rewritten merely to adopt this version.

The Agent may use any LLM, image generator, renderer, workflow engine, or file system, provided the observable inputs/outputs conform to this contract.

## 2. Required Capability Interface

An Adapter declares these capabilities:

| Capability | Required | Purpose |
|---|---:|---|
| `structured_reasoning` | yes | parse/group/plan/QA decisions |
| `read_files` | yes | source vocab + references |
| `write_files` | yes | JSON/PNG/reports/manifests |
| `image_generate` | yes for Stage 07 | produce base illustration |
| `image_inspect` | yes | semantic/style QA |
| `deterministic_compose` | strongly required | exact labels/connectors |
| `image_edit` | optional | targeted illustration repair |

If `deterministic_compose` is unavailable, the Agent MUST stop before production approval or hand off Stage 08 to an external renderer. It may create mockups, but MUST NOT mark them `APPROVED`.

## 3. Canonical Stage Contract

### Stage 01 — Parse Vocabulary
Input: curriculum source.
Output: `VocabularyMaster` conforming to `schemas/vocabulary_master.schema.json` (each item conforms to `schemas/vocabulary.schema.json`).

### Stage 02 — Validate Vocabulary
Input: `VocabularyMaster[]`.
Output: validation report + review flags. Curriculum data may be flagged but not silently rewritten.

### Stage 03 — Group / Review Gate
Input: validated vocabulary.
Output: `CardPlanSet` conforming to `schemas/card_plan_set.schema.json` (each item conforms to `schemas/card_plan.schema.json`).
Gate: every curriculum item assigned exactly once by curriculum identity key unless explicitly deferred.

### Stage 04 — Scene Brief
Input: approved card plan item.
Output: `SceneBrief` conforming to `schemas/scene_brief.schema.json`.
Gate: one target spec per vocabulary term.

### Stage 05 — Layout Spec
Input: SceneBrief.
Output: `LayoutSpec` conforming to `schemas/layout_spec.schema.json`.
Gate: explicit label zones and connector policies.

### Stage 06 — Prompt Compile
Input: SceneBrief + LayoutSpec + visual rules.
Output: `CompiledPrompt` conforming to `schemas/compiled_prompt.schema.json`.
Gate: prompt explicitly forbids instructional typography.

### Stage 07 — Base Illustration
Input: CompiledPrompt.
Output: one base illustration image + metadata conforming to `schemas/base_asset.schema.json`.
Hard rule: zero instructional English / IPA / Chinese / label cards / connector graphics.

### Stage 08 — Deterministic Compose
Input: base illustration + authoritative VocabularyMaster + LayoutSpec + design tokens.
Output: deterministic composed image for `composed_png`; for `app_bundle`, separate authoritative content/layout/assets plus an actual deterministic review rendering.
Hard rule: teaching text is rendered from the curriculum facts, never copied from generated pixels.

### Stage 09 — QA
Input: current base + composed card/review rendering + all provenance; for `app_bundle`, include learning-data and target-application schema validation.
Output: `QAReport` conforming to `schemas/qa_report.schema.json`.
Hard failure blocks approval.

### Stage 10 — Targeted Repair
Input: failed QA report.
Output: revised smallest affected layer + repair record conforming to `schemas/repair_action.schema.json`.
Examples: text-only recompose, connector reroute, layout move, illustration regenerate.

### Stage 11 — Approved Export
Input: all hard gates pass.
Output: requested image/application bundle + manifest conforming to `schemas/manifest.schema.json` + scene brief + layout spec + QA report. An application's import formats must separately pass its actual schema; a product-native file is not automatically a Core-schema artifact.
State becomes `APPROVED`.

## 4. Lifecycle
Allowed card states:
`DRAFT -> PLANNED -> BRIEF_READY -> LAYOUT_READY -> PROMPT_READY -> GENERATED -> COMPOSED`, followed by the QA/repair transitions defined in `engine/state_machine.md`.

No transition may skip a hard-gate prerequisite.

## 5. Mapping Modes
Every term uses exactly one mode:
- `direct_anchor`
- `action_anchor`
- `scene_state`
- `dialogue_phrase`
- `timeline_segment`
- `comparison_zone`
- `relation_anchor`

Connector defaults:
- direct_anchor -> required
- action_anchor -> optional
- relation_anchor -> optional
- scene_state -> none
- dialogue_phrase -> none
- timeline_segment -> none
- comparison_zone -> none

The declared Speak Replay context-card profile may set all connector policies to `none`, including visible-object words; mapping modes remain in SceneBrief. Record this profile instead of silently changing the general direct-anchor default.

## 6. Error Semantics
Adapters must return explicit failure states instead of silently improvising.

Minimum standard error codes:
- `SOURCE_DATA_AMBIGUOUS`
- `COVERAGE_ERROR`
- `SCENE_GROUP_WEAK`
- `BASE_TEXT_CONTAMINATION`
- `TARGET_MISSING`
- `TEXT_ERROR`
- `LINE_MAPPING_ERROR`
- `LAYOUT_COLLISION`
- `STYLE_FAIL_CONNECTOR_V3`
- `STYLE_DRIFT`
- `COMPOSER_UNAVAILABLE`

## 7. Determinism Boundary
The following must be deterministic for production approval (source corrections retain original values and evidence):
- exact English string
- exact IPA string when supplied
- exact Chinese gloss
- card ID / vocabulary identity
- label/connector style token selection
- lifecycle status
- output manifest

## 8. Portability Rule
Adapters MAY change:
- API calls
- filesystem paths
- image model
- orchestration framework
- renderer implementation

Adapters MUST NOT change:
- curriculum facts
- stage semantics
- schemas without version bump
- visual/connector tokens within the active spec
- QA hard gates


## 9. Platform Adapter Resolution
At the start of each production run, the orchestration layer MUST identify the execution platform and load exactly one tested platform Adapter in addition to the Core rules.

Within the package, the resolution order is:
1. Agent Contract
2. Core Skill
3. Active Platform Adapter
4. Current Task Configuration / declared product profile

This order resolves skill defaults; it does not supersede current user instructions or platform constraints.

Supported adapters in this package include:
- OpenAI: `adapters/openai/ADAPTER.md`
- Doubao Work: `adapters/doubao_work/ADAPTER.md`
- Qwen Office: `adapters/qwen_office/ADAPTER.md`

Platform-specific corrective rules MUST NOT be indiscriminately merged across platforms. An Adapter may tighten thresholds but may not weaken curriculum facts, hard QA gates, lifecycle semantics, or active visual tokens.

The active platform + adapter path MUST be recorded in the run manifest for auditability. Stage 08 also MUST load `core/design_tokens.json`.
