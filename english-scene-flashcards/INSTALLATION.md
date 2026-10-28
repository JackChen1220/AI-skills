# Installation / Codex Check

1. Clone or download the repository as one folder.
2. Keep the folder structure intact; do not copy only `SKILL.md`.
3. From the Skill folder run:

```bash
python tools/validate_package.py . --strict
```

Expected output:

```text
PACKAGE VALIDATION: PASS
```

Strict mode verifies required Core/Engine/Schema/Adapter artifacts, JSON parsing/meta-schemas, package path references, manifest inventory, and the minimal Stage 01–03 examples.

For the GitHub repository distribution, Git object integrity is used for repository bytes; reference PNGs may be recompressed for lightweight distribution, so the validator does not compare source-ZIP byte/SHA256 metadata against those Git-distributed assets.

Required top-level directories include `core/`, `engine/`, `schemas/`, `adapters/`, `assets/`, and `tools/`.

Codex should read `SKILL.md`, then `AGENT_CONTRACT.md`, Core docs, JSON schemas, and exactly one active platform Adapter according to `ADAPTER_ROUTING.md`.
