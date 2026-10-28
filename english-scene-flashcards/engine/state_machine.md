# State Machine Contract

Canonical states:
`DRAFT -> PLANNED -> BRIEF_READY -> LAYOUT_READY -> PROMPT_READY -> GENERATED -> COMPOSED`

QA branch:
- `COMPOSED -> APPROVED` only when Stage 09 returns `PASS`.
- `COMPOSED -> QA_FAILED` when Stage 09 returns `FAIL`.
- `QA_FAILED -> REVISED` after the smallest failing layer is repaired.
- `REVISED -> GENERATED` when the base illustration was regenerated/edited.
- `REVISED -> COMPOSED` when only deterministic composition/layout/connectors/text were repaired.
- After either route, Stage 09 MUST run again before `APPROVED`.
- `APPROVED -> SUPERSEDED` is allowed when a later approved revision replaces a card.

No state transition alone proves QA; the QA report is the approval evidence.
