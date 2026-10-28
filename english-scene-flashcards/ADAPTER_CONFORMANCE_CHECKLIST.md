# Adapter Conformance Checklist

A new Agent/Adapter is production-ready only when all boxes pass.

## Capability
- [ ] Can read curriculum/source files.
- [ ] Can write structured JSON artifacts.
- [ ] Can generate one base illustration per card.
- [ ] Can inspect images for semantic/style QA.
- [ ] Can render deterministic text/labels/connectors OR hand off to a deterministic renderer.

## Contract
- [ ] Declares a unique platform/adapter ID.
- [ ] Records the active adapter in the run manifest.
- [ ] Loads Core + only the active platform adapter, not unrelated platform patches.
- [ ] Reads `AGENT_CONTRACT.md`.
- [ ] Validates representative artifacts against JSON Schemas.
- [ ] Enforces legal lifecycle transitions.
- [ ] Returns explicit error codes on blocked stages.

## Stage 07
- [ ] Generates one card, not accidental batch collage/grid.
- [ ] Produces zero instructional typography.
- [ ] Preserves required visual targets.
- [ ] Leaves label-safe perimeter space.

## Stage 08
- [ ] Renders English from source data.
- [ ] Renders IPA from source data with full glyph coverage.
- [ ] Renders Chinese from source data.
- [ ] Uses `connector.v3.light` only.
- [ ] Uses no connector where policy is `none`.
- [ ] Uses no red/orange/yellow anchor beads.

## QA / Approval
- [ ] Hard QA failures block approval.
- [ ] Batch vocabulary coverage is checked.
- [ ] Approved export includes manifest + provenance.
- [ ] Mockups are never mislabeled `APPROVED`.

## Conformance result
- `PASS`: may execute full Stage 01–11 production.
- `PARTIAL`: may execute only supported stages and must hand off blocked stages.
- `FAIL`: planning/reference use only.
