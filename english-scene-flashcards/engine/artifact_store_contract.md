# Artifact Store Contract

The runtime may use any filesystem/object store, but must preserve stable logical artifacts per card:

- source vocabulary identity IDs;
- card plan item;
- scene brief;
- layout spec;
- compiled prompt;
- base illustration + base asset metadata;
- final composed image, or separate application assets/content/layout plus a composed review image for `app_bundle`;
- QA report;
- repair actions when present;
- approved manifest entry.

Physical paths are Adapter/runtime details. Do not hard-code `/mnt/data` or platform-specific paths in Core schemas.

Preserve native image output and provenance when a normalized export is made. Course and album covers have independent policies. Record hashes for each reviewed base/cover/content/layout artifact and bind QA to those versions. Keep failed generation calls and retry resolutions; an older file is not evidence that a new call succeeded. Resuming a run must preserve approved data, repair history and native originals.
