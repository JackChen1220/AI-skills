# Migration Guide — V1.2 to V2.0 Agent Agnostic

## What stays unchanged
- Stage 01–11 production philosophy
- curriculum as Source of Truth
- Flashcard Visual Spec V2
- `connector.v3.light`
- Golden reference approach
- hard-gate QA philosophy

## What changes

### 1. Monolithic Skill -> three layers
V1 mixed product rules and current-runtime execution details.
V2 separates:
- `core/` — portable product rules
- `engine/` — portable contracts/utilities
- `adapters/` — runtime/Agent-specific integration

### 2. Explicit Agent Contract
`AGENT_CONTRACT.md` defines capabilities, stage I/O, lifecycle, errors, and deterministic boundaries.

### 3. Formal schemas
Stage artifacts now have versioned JSON Schemas under `schemas/`.

### 4. Runtime paths removed from core
Paths such as `/mnt/data/...` are adapter/runtime configuration only.

### 5. Approval restriction
An Agent without deterministic composition may create planning outputs and mockups, but may not mark final cards `APPROVED`.

## Recommended migration procedure
1. Keep V1 approved images as Golden Set assets.
2. Start all new production using V2 contracts.
3. For existing manifests, map fields to `schemas/manifest.schema.json`.
4. Keep connector token `connector.v3.light` unchanged.
5. Add an Adapter for each new runtime rather than modifying `core/`.
