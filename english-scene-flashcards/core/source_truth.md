# Source of Truth

## Authoritative fields
The curriculum source is authoritative for:
- English spelling and phrase boundaries;
- IPA when supplied;
- Chinese gloss;
- unit / page / lesson association;
- intended textbook sense.

## Prohibited behavior
- Do not silently normalize or “improve” textbook wording.
- Do not use image-model text as the source for Stage 08.
- Do not use OCR from a generated illustration to reconstruct curriculum text.
- Do not merge two repeated terms from different units/senses solely because the surface string matches.

## Identity key
Use a curriculum identity key that distinguishes repeated terms, e.g.:
`grade|book|unit|term|sense_id`.

## Ambiguity
If the source is unclear, emit `SOURCE_DATA_AMBIGUOUS` and require review.
A review correction must preserve the original source value in provenance.

## Multiple sources and partial IPA
- Reconcile textbook pages with spreadsheet/CSV rows before grouping. Preserve source file identity, page/row and raw values; count both source rows and semantic entries when spelling variants explain a difference.
- Preserve separate IDs for British/American variants and distinct unit/sense entries; never deduplicate solely by term string.
- A documented teaching correction records original value, corrected value, reason and reliable evidence. Verify a suspected OCR/source error against the original page first.
- Missing IPA remains null unless supplementation is explicitly part of the task and marked as such. IPA supplied for only one component of a phrase is not full-phrase IPA: retain the component separately and leave the displayed phrase IPA null. Do not manufacture a pronunciation from partial source data.

## Provenance
Every approved card must record:
- source identifier;
- vocabulary identity keys;
- active Skill version;
- active platform Adapter;
- visual spec token;
- connector token;
- QA result.
