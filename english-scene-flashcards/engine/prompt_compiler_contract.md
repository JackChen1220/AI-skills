# Prompt Compiler Contract

Input:
- validated `SceneBrief`;
- validated `LayoutSpec`;
- Core visual rules;
- active platform Adapter;
- current task configuration.

Output: `CompiledPrompt` conforming to `schemas/compiled_prompt.schema.json`.

Hard invariants:
1. request exactly one base illustration per card;
2. explicitly forbid English teaching text, IPA, Chinese gloss, label cards, arrows, connector lines and anchor dots;
3. preserve visual target requirements and forbidden constraints;
4. include layout-aware negative-space guidance;
5. record the active adapter ID.
