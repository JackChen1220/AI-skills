# Engine Layer

The Engine layer defines portable execution **interfaces and invariants**, not one mandatory renderer implementation.

Core says **what** must be true. Adapters say **how** a platform exposes capabilities. Engine contracts define the hand-off between stages.

Read:
- `state_machine.md`
- `prompt_compiler_contract.md`
- `composer_contract.md`
- `qa_engine_contract.md`
- `artifact_store_contract.md`

An Agent may implement these contracts with Python, JavaScript, a workflow engine, a native design renderer, or another deterministic system.
