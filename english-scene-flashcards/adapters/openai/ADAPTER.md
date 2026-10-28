# OpenAI Adapter

## Role
Map the Agent Contract to an OpenAI-capable environment.

## Capability mapping
- structured reasoning -> ChatGPT model
- file read/write -> project/file tools + local runtime when available
- image generation/edit -> image generation capability
- deterministic compose -> Python/PIL or equivalent deterministic renderer
- image inspect -> model vision + structured QA rules

## Execution rules
1. Read source files before planning.
2. Generate one independent Stage 07 image per card; do not ask for a collage/grid as a substitute for separate outputs. Independent calls may be batched when the environment permits.
3. Explicitly request a **base illustration only** at Stage 07.
4. Never trust generated text for Stage 08.
5. Use deterministic rendering for English/IPA/Chinese and connector graphics.
6. Run QA after composition and repair only the failing layer where possible.
7. Use the current environment's native image generation/edit capability and its tool instructions. Inspect a referenced image before editing. An explicitly chosen native path must not silently become a CLI, external API or provider fallback.
8. Preserve successful native outputs and record failures separately. Retry transient failures a bounded number of times (normally up to two retries); persistent failure leaves the affected card pending while independent work may continue. Do not infer success from an older same-named file.
9. Use combined base/overlay review boards where helpful. Inspect suspicious regions only when needed; once source, scene and readability checks pass, respect the user's detail budget and continue the batch.
10. For application delivery, load the requested product profile, validate the actual application schema and keep base/content/layout separate. Composition can use the product renderer or deterministic local code; no baked teaching text is needed in the source asset.

## Environment-specific paths
Do not encode `/mnt/data` or other runtime paths into core schemas. Paths belong in run manifests or adapter configuration.
