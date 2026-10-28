# Changelog

## 2.3.1 — General English scene-flashcard naming
- Renamed the skill, package directory and active references to english-scene-flashcards.
- Added the Chinese display name 英语场景闪卡 and updated the invocation example.
- Kept production rules and historical provenance unchanged.

## 2.3.0 — Curriculum application bundles and proportionate review
- Added the Speak Replay profile for separated base/vocabulary/learning/layout delivery, natural examples and per-term exercises.
- Defined 9:16 course covers reused from pure bases; album-cover policy remains independent and follows current instructions.
- Added cross-source reconciliation, documented source corrections and partial/missing IPA handling.
- Added stable recurring-character references, age-appropriate scenes and explicit no-connector context-card routing.
- Added actual base/overlay review, hash-bound QA, separate generated/ready/published counts, resumable work and bounded native-tool retries.
- Distinguished hard teaching failures from accepted cosmetic warnings; stop low-value repair once required checks pass.
- Extended layout schema with text-free wordId references while preserving legacy layouts; manifest supports multi-artifact hashes and QA records support evidence/human-review identity.
- Updated Agent Contract to 1.1 and moved version/protocol frontmatter under supported metadata; preserved the existing invocation name.

## 2.2.2 — Completeness and contract-consistency hotfix
- Added the missing `engine/` interface layer promised by README architecture.
- Added `core/design_tokens.json`, required by deterministic Stage 08 composition.
- Added Stage 07 base-asset and Stage 10 repair-action schemas.
- Added array wrapper schemas for VocabularyMaster and CardPlanSet.
- Added an actual Golden Set reference and usage rules.
- Tightened manifest/run-state provenance requirements with platform identity.
- Required `mapping_mode` in LayoutSpec labels.
- Replaced the package validator with strict hash, meta-schema, reference, Engine and Golden Set checks.
- Corrected adapter version headings.


## 2.2.0
- Added Qwen Office / 千问办公 Adapter.
- Added Qwen observed-failure audit.
- Added adapter routing specification.
- Added Qwen card-type router and teaching-mechanism grouping gate.
- Added Qwen connector length, endpoint, context-proximity, cutaway, object-differentiation and density QA rules.
- Added adapter selection to Agent Contract and conformance checklist.
- Retained Doubao Work Adapter and Connector V3 unchanged.

## 2.1.0
- Added Doubao Work Adapter based on observed production failures.
- Tightened Doubao label scale, connector geometry, text contamination and style drift QA.
## 2.2.1 — Packaging hotfix
- Restored mandatory `core/` documents referenced by `SKILL.md`.
- Restored mandatory `schemas/` JSON Schemas referenced by `AGENT_CONTRACT.md`.
- Added `PACKAGE_MANIFEST.json`.
- Added `tools/validate_package.py` to fail fast on missing required files or invalid JSON schemas.
- Restored all supported platform adapters in the distributable folder.
- Root cause: V2.2 packaging assembled only root docs/adapters and omitted Core/Schema directories while the contract still referenced them.

