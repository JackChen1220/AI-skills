# Platform Adapter Routing

## Purpose
The Skill uses one shared Core and multiple platform-specific Adapters. The active Adapter is selected by the actual execution environment.

## Rule stack
Effective production rules are resolved in this order:

1. **Agent Contract** — cross-agent hard contract
2. **Core Skill** — curriculum, workflow, visual, connector, QA standards
3. **Active Platform Adapter** — platform-specific corrections and thresholds
4. **Current Task Configuration** — grade, textbook, unit, card plan, batch settings

Current user instructions and platform constraints take precedence over these skill defaults. Later package layers select supported output/profile choices and may tighten execution details; they do not silently change source facts or waive hard teaching checks.

## Adapter selection

| Execution platform | Adapter |
|---|---|
| OpenAI / ChatGPT environment | `adapters/openai/ADAPTER.md` |
| Doubao Work / 豆包工作 | `adapters/doubao_work/ADAPTER.md` |
| Qwen Office / 千问办公 | `adapters/qwen_office/ADAPTER.md` |
| Unknown/generic Agent | `adapters/generic/ADAPTER_TEMPLATE.md` until a tested adapter exists |

## Important behavior
Do NOT merge every platform's corrective rules into one giant prompt.

Example:
- Qwen Office should read Core + Qwen Office Adapter.
- Doubao Work should read Core + Doubao Work Adapter.
- Doubao-specific label oversizing rules do not automatically apply to Qwen if Qwen does not show that failure.

## Shared rules remain shared
All platforms still use:
- exact curriculum Source of Truth;
- Stage 01–11 pipeline;
- deterministic teaching text;
- Flashcard Visual Spec V2;
- `connector.v3.light`;
- Core mapping modes;
- hard QA approval gate.

## Adapter identification
At the beginning of a production run, write the following into the run manifest:

```json
{
  "skill_version": "2.3.1",
  "platform": "qwen_office",
  "adapter": "adapters/qwen_office/ADAPTER.md",
  "visual_spec": "Flashcard Visual Spec V2",
  "connector": "connector.v3.light"
}
```

This makes platform-specific behavior auditable and reproducible.

Output mode and product profile are independent of platform selection. Speak Replay uses `profiles/speak_replay.md` in addition to Core and one adapter; it does not require reading every other adapter.
