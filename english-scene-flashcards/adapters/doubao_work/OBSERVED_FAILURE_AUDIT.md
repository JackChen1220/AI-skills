# Doubao Work — Observed Failure Audit

Source batch: 10 uploaded Grade-4 flashcards, 1536×2048 each.

## Cross-batch findings

### Critical
1. Label cards and word text are materially too small relative to canvas.
2. Connector lines are frequently several times longer than necessary because labels are pinned to outer edges.
3. Several semantic anchors are wrong or weak (e.g. abstract/action words pointing to faces or arbitrary objects).
4. Base illustrations contain generated pseudo-text/signage in some cards.
5. Illustration style drifts noticeably across the batch.

### High
6. Arbitrary red/blue left accent bars create an undefined visual coding system.
7. Long terms are handled by shrinking text instead of enlarging/wrapping the card.
8. Some groups are category-coherent but not naturally scene-coherent.
9. Several scenes include irrelevant visual objects that compete with vocabulary targets.

## Card-specific examples

- `G4A-C01`: doctor/nurse labels too small; both connectors excessively long; hospital context label is undersized.
- `G4A-C02`: four occupations are legible but connectors run almost the full card height; semantic-category grouping dominates scene plausibility.
- `G4A-C03`: cook/cleaner/delivery/office worker share a contrived frame; all direct lines are too long; red accent bar appears without defined meaning.
- `G4A-C04`: `clean` is anchored near the child's face rather than the cleaning action/state; `floor` connector is extremely long; style is more 3D/glossy than the rest of the set.
- `G4A-C05`: `cook` and `make the bed` lines are unnecessarily long; `chore` and `together` are context concepts and should not behave like direct objects.
- `G4A-C06`: `strong` points near the boy's face and is semantically weak; `kind`/`quiet` are not adequately demonstrated by a posed portrait; illustration style shifts toward polished anime.
- `G4A-C07`: `Chinese` has a weak/incorrect physical anchor; `photo` should target an actual photograph/frame; connectors cross large areas of the scene.
- `G4A-C08`: football/basketball lines are very long; simultaneous football + basketball creates competing focal sports while `play`/`game` are broad context terms.
- `G4A-C09`: label scale is too small; scene contains unrelated sports objects; `PE`/`sport`/`fun` are broad scene concepts and should not be treated as object labels.
- `G4A-C10`: shop/bus stop/buy lines are too long; generated storefront/bus-stop pseudo-text violates clean-base-illustration rules.
