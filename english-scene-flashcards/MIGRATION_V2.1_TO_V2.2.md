# Migration — Skill V2.1 to V2.2

## What changed
V2.2 adds the second production-platform adapter: **Qwen Office / 千问办公**.

V2.1 already contained:
- Agent-Agnostic Core
- OpenAI Adapter
- Doubao Work Adapter
- Connector V3

V2.2 adds:
- `adapters/qwen_office/ADAPTER.md`
- `adapters/qwen_office/OBSERVED_FAILURE_AUDIT.md`
- `ADAPTER_ROUTING.md`
- explicit adapter-resolution order in `AGENT_CONTRACT.md`
- Qwen-specific QA codes and card-type routing

## Compatibility
No Core hard rule is removed.
No curriculum schema is intentionally changed.
No Connector V3 visual token is changed.

Existing Doubao Work runs should continue to use the Doubao adapter.
Qwen Office runs should use the Qwen adapter only.

## Main Qwen improvements
- card-type routing before Scene Brief;
- abstract/function-word guard;
- teaching-mechanism consistency gate;
- shorter connector geometry;
- semantic endpoint accuracy;
- local/context label proximity;
- special cutaway/spatial template;
- same-category object differentiation;
- Qwen-specific Stage 09 QA codes.
