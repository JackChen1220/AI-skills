# Flashcard Visual Spec V2

## Overall character
- warm 2D storybook/textbook illustration appropriate to the learner's age; older students need age-appropriate student/adult characters rather than a compulsory children's template;
- soft texture, rounded forms, clean silhouettes;
- controlled saturation, calm background hierarchy;
- age-appropriate expressions and actions;
- no photorealism, glossy 3D toy look, or strong anime drift.

## Final label cards
- white / light-warm rounded rectangle;
- subtle shadow, no heavy border;
- English: dominant, bold, deep navy;
- IPA: secondary gray-blue;
- Chinese gloss: secondary dark neutral;
- sufficient internal padding and line spacing;
- long phrases enlarge/wrap the card rather than shrinking text excessively.

## Layout hierarchy
`illustration subject > vocabulary label > connector`.
Connector must never become the visual protagonist.

## Base illustration rule
Stage 07 contains no instructional English, IPA, Chinese, label cards, arrows, anchor dots or connector graphics.

## Style consistency
A batch must use one stable style family and Golden Style Reference when the platform supports it.
Use an accepted character reference and concise identity notes when recurring protagonists are requested; preserve age, facial features, hairstyle, palette and rendering family. Do not impose a previous batch's specific character identities on unrelated work.

## Application assets and covers
In `app_bundle`, preserve pure base artwork and independently render the teaching layer. Canvas and cover policies are run configuration, with Speak Replay defaults in `profiles/speak_replay.md`. Course covers and album covers have separate roles; never infer one aspect ratio from the other. Branding is a deterministic product layer when the active profile calls for it.
