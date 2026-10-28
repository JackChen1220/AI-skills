# Qwen Office Observed Failure Audit

## Audit source
A batch of Qwen Office-generated primary-school English scene flashcards was reviewed visually. The batch is generally cleaner than the previously reviewed Doubao Work batch, especially in label readability and concrete-object rendering, but several recurring production issues remain.

## Overall assessment
Qwen Office is a promising production backend for this Skill when used with a dedicated adapter. Its strongest use case is **concrete object/place cards with a small coherent target set**. Its weakest use case is **mixed abstract/function-word groups forced into ordinary object cards**.

---

## 1. Fixed-corner labels create avoidable long connectors

Observed patterns:
- `blackboard` / `teacher's desk` / `computer` card: some labels are much farther from targets than necessary.
- `light` / `picture` / `window` / `door`: `picture` receives a long diagonal line despite available nearer label space.
- house cutaway card: room labels at the top/bottom force long vertical connectors.

Root cause:
- label-first perimeter template rather than target-first placement.

Required fix:
- connector-first layout;
- proximity-based label placement;
- special cutaway layout for multi-region cards.

---

## 2. Functional/abstract terms are not naturally grounded

### `wall / fan / floor / near`
`near` is a relation, not an object. The scene does not explicitly construct a near/far contrast or a clear relation pair.

### `clean / help / really`
`really` is a degree/discourse word. It has no concrete visual anchor in an ordinary cleaning scene.

### `lost / wow / cute / so much`
The card mixes event/state, exclamation, adjective, and degree phrase. The image can be expressive, but the teaching mechanism for each word is inconsistent.

### `his / her / or / right`
Possession, conjunction, and judgment are combined in one ordinary scene. This requires a choice/possession/dialogue template, not object labeling.

Required fix:
- mandatory card-type router;
- dialogue/contrast/possession/narrative templates;
- no arbitrary connectors for function words.

---

## 3. Connector endpoint accuracy is inconsistent

Observed examples:
- `hat`: endpoint appears above/near the hat rather than clearly on the hat itself.
- some lines terminate in visually empty or weakly defined regions.
- large environment targets such as `wall` can receive an endpoint that does not teach which exact region represents the concept.

Required fix:
- target feature must be explicit in Scene Brief;
- Stage 09 endpoint QA;
- use direct anchor on object body or omit connector when the whole region is the concept.

---

## 4. Context labels can be too remote from their subject

The `strong / friendly / quiet / hair` scene is pedagogically promising because the characters enact distinct meanings. However, context words with no connector need proximity to the intended person. A label placed far from the relevant character can create ambiguity even if no line is technically required.

Required fix:
- no-line context label proximity rule;
- strengthen pose/action semantics;
- local label placement near the relevant character.

---

## 5. Same-category objects are not differentiated strongly enough

The school-book card visually contains multiple books, but their identities rely heavily on the text labels. Without labels, `Chinese book`, `English book`, `maths book`, and `storybook` are not consistently self-evident.

Required fix:
- design distinct cover icon systems;
- vary color and visual motif;
- verify target recognizability without label text.

---

## 6. Cutaway/multi-region cards need a dedicated template

The `bedroom / study / living room / kitchen / bathroom` house cutaway is structurally clear, but standard perimeter labels create unnecessary line length and visual crowding.

Required fix:
- local labels adjacent to rooms;
- connector-free labels when room boundaries are clear;
- split 5+ regions or use dedicated map/cutaway template.

---

## 7. Excessive empty space lowers teaching density

Some cards use large areas of empty wall/floor/background while objects remain small. This increases connector length and weakens target salience.

Required fix:
- closer crop;
- larger target scale;
- intentional negative space only where labels need it.

---

## 8. Mixed scene mechanisms should trigger regrouping

Several cards are visually attractive but combine vocabulary requiring different instructional representations. The grouping system must not accept a group merely because the terms can be forced into one scene.

Required fix:
- Stage 03 teaching-mechanism compatibility gate;
- split or reroute weak groups.

---

## 9. Concrete-object cards are the strongest Qwen pattern

Observed strong/usable patterns include:
- classroom fixtures;
- simple room furniture;
- hat/glasses/shoe body-part/accessory cards;
- food table cards;
- fridge/object cards.

Recommended use:
- 3–4 concrete targets;
- clear spatial separation;
- short connectors;
- deterministic labels.

---

## 10. Adapter conclusion

Qwen Office should not receive a generic 'make a vocabulary flashcard' instruction. It should receive:
1. Core Skill constraints;
2. card-type routing result;
3. a Qwen-specific layout strategy;
4. connector length and endpoint constraints;
5. Qwen-specific QA gates.

With these controls, Qwen Office is suitable for batch production, especially for concrete-object and action cards.
