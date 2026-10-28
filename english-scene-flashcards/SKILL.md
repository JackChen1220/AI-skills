---
name: english-scene-flashcards
description: "制作或更新教材、自建词表的英语场景闪卡，适用于小学至高中及主题词汇；支持纯场景底图、独立教学层、例句练习和 Speak Replay 学习包交付。"
metadata:
  version: "2.3.1"
  protocol: agent-agnostic
  contract_version: "1.1.0"
---

# Mission
Convert a curriculum or user vocabulary source into a visually consistent flashcard set or application learning bundle, preserving source facts. The skill applies across learner ages and grades.

# Non-Negotiable Architecture
Separate:
- **Generative layer**: scene illustration, characters, environments, poses, props.
- **Deterministic layer**: English, IPA, Chinese gloss, label cards, connector graphics, IDs, manifests, status.
- **Application content/layout**: vocabulary and learning content are separate from positions/styles; new layouts reference stable `wordId` values rather than copying teaching text.

An image generator MUST NOT be the authoritative source for teaching text.

# Governing Documents
Read the shared contract and Core first:
1. `AGENT_CONTRACT.md`
2. `core/workflow.md`
3. `core/source_truth.md`
4. `core/grouping_rules.md`
5. `core/scene_brief_rules.md`
6. `core/visual_spec.md`
7. `core/connector_system_v3.md`
8. `core/design_tokens.json`
9. `core/qa_rules.md`
10. `ADAPTER_ROUTING.md` and exactly one adapter for the current platform.

Read the relevant Engine contract and Schema when producing or changing its artifact; do not load every platform or unrelated example. For Speak Replay or a request to reuse the established textbook learning-bundle method, also read `profiles/speak_replay.md`.

# Choose the Deliverable
- `composed_png`: printable/shared flashcard with deterministic labels/connectors and its source artifacts.
- `app_bundle`: pure base + separate vocabulary, learning content and layout, plus a deterministic review rendering. A flattened teaching image is review evidence, not the application's content source.

Record the mode, profile, canvas, character/style reference, cover policy and source precedence in the run configuration. Reuse an existing run's decisions. Resolve ordinary choices autonomously; an internal review gate does not by itself require a user approval round.

# Fixed Pipeline
`01 Parse -> 02 Validate -> 03 Group -> 03 Review Gate -> 04 Scene Brief -> 05 Layout -> 06 Prompt Compile -> 07 Base Illustration -> 08 Deterministic Compose -> 09 QA -> 10 Targeted Repair -> 11 Approved Export`

# Hard Rules
- Curriculum source is authoritative for spelling, IPA, gloss, unit and intended sense.
- Retain raw source values and stable identities; reconcile PDF/table counts and spelling variants before generation. Corrections need explicit provenance; missing or partial phrase IPA must not be invented as complete source IPA.
- Every source term must be assigned or explicitly deferred with reason.
- Every visualized target must have a mapping mode.
- Not every word gets a connector.
- Base illustration must contain zero instructional typography.
- Stage 08 must use authoritative vocabulary data, not OCR or generated text.
- Hard QA failure blocks `APPROVED`.
- Repair the smallest failing layer when possible.
- Inspect the actual base and composed view before visual approval. Data/schema validation alone cannot prove visual QA.
- Prioritize source accuracy, full coverage, scene meaning, readable cards and unobstructed faces/hands/actions. When these pass, stop routine cosmetic repair; record harmless microtexture as `WARN` with a reason when accepted within the user's scope.

# Resume and Batch Execution
Read existing manifest/progress and inspect the affected artifacts before resuming. Preserve finished work; initialization scripts must not overwrite approved content. A changed base, vocabulary, learning file or layout invalidates its previous QA until the affected checks run again.

Track planned, generated, reviewed/ready and published counts separately. Report the current count and any concrete blocker. A failed image call is not a generated card; preserve its error and retry outcome. Do not silently switch an explicitly selected image tool/provider.

# Active Visual System
- `Flashcard Visual Spec V2`
- `connector.v3.light`
- age-appropriate warm 2D illustration; stable characters, palette and rendering family within a batch
- white/light-warm rounded label cards
- deep navy English word
- subordinate IPA and Chinese
- pale gray-blue connectors only when instructionally useful; the Speak Replay context-card profile uses no connectors

# Completion
A batch is complete only when:
1. source coverage is complete;
2. all approved cards pass hard QA;
3. every final card has provenance and manifest;
4. final filenames/IDs are unique;
5. outputs are checked against `assets/golden_set/` when a Golden reference is provided for the product line.

For `app_bundle`, also require complete learning data, a successful deterministic review render and validation against the target application's current schema. Bind approval to actual artifact hashes. Agent visual inspection remains `humanReviewed=false`. Completion of local materials does not imply import, deployment or publication.


# Platform Adapters
- OpenAI: `adapters/openai/ADAPTER.md`
- Doubao Work: `adapters/doubao_work/ADAPTER.md`
- Qwen Office: `adapters/qwen_office/ADAPTER.md`

Platform adapters may tighten execution thresholds (for example label size and connector-length limits) but may not weaken Core hard gates.


# Adapter Selection Rule
At run start, identify the actual execution platform and load exactly one active platform adapter in addition to Core.

User instructions and platform constraints take precedence over skill defaults. Within the package, use `Agent Contract -> Core -> Active Platform Adapter -> Current Task Configuration`; task/profile choices fill configurable slots rather than silently changing source facts or waiving hard teaching checks.

Do not indiscriminately merge corrective rules from other platforms. See `ADAPTER_ROUTING.md`.


# Package Integrity
Before execution, an Agent SHOULD run `python tools/validate_package.py . --strict`.
A failed package check blocks production because Core/Schema omissions can invalidate stage contracts.
