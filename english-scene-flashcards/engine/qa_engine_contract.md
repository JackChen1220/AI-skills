# QA Engine Contract

Input:
- authoritative source records;
- SceneBrief;
- LayoutSpec;
- base asset metadata;
- current base and composed final/review image;
- active Adapter and Skill version.

Output: `QAReport` conforming to `schemas/qa_report.schema.json`.

Required dimensions:
- Data QA
- Semantic QA
- Mapping QA
- Layout QA
- Connector QA
- Style QA
- Provenance QA

Core hard failures block approval. Adapter checks are additive. A repaired card must be rechecked before approval.

`app_bundle` additionally checks learning-data consistency and the current target-application schema. Record the artifact hashes and actual visual evidence. Do not mark Agent inspection as human review. Accepted harmless cosmetic details are `WARN` with a reason; they do not justify repeated regeneration after teaching checks pass.
