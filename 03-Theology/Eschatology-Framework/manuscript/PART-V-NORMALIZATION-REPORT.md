---
title: "Part V — Normalization Report (EN)"
type: manuscript-report
created: 2026-10-14
status: approved
related: "[[PART-IV-NORMALIZATION-REPORT]], [[10-manuscript-architecture]], [[EDITORIAL-RULES]]"
---

# Part V — Normalization Report (English)

## Revision 1.1: review fixes applied (2026-10-14). English Part V APPROVED.

The titles, N1–N3 and the ch27 scope rewrite are approved. Fixes, all verified in the rebuilt PDF (74 pages, all gates OK, normalization 0):

| # | Where | Before | After |
|---|---|---|---|
| R1 | ch26 textual note | "The perfect is completed action with continuing present relevance." (textbook formula stated as a rule) | "The perfect presents the arrival as a completed development whose resulting state is in view." |
| R2 | ch27 scope note | "the broader Second Temple literature … the intertestamental material, Josephus on the parties, the rabbinic discussion" (rabbinic material is mostly later) | "the broader Jewish evidence on resurrection expectation — Second Temple literature, Josephus on the parties, and later rabbinic discussion" |
| R3 | ch27 John 5 finding | "John uses spiritual-resurrection language and bodily-resurrection language … and distinguishes them with a clause." | "John juxtaposes present death-to-life language with future tomb-resurrection language in the same discourse and marks them differently. Verse 24 strongly supports a spiritual, death-to-life reading of the first; verses 28–29 explicitly describe tombs, coming out, and two destinies." |
| R3b | ch27, the same claim in three more places (not flagged by the reviewer) | "because John separated them" · rule box "tells you which is which" · summary "John proves the two categories are distinguishable by distinguishing them himself" | "because John marks them differently himself" · "and marks them differently" · "John shows the two can be told apart by marking them differently himself" |
| R4 | ch28 Luke 4 | "He stopped within a single sentence, before its second clause" (modern punctuation read back) | "He stopped within the same prophetic unit, before the next coordinated clause — within what our Bibles now number as a single verse." |
| R4b | ch28, the same framing elsewhere (not flagged) | heading "stopped partway through the sentence" · "a single sentence in the scroll" · "even the sentence he had begun" · summary "the sentence our Bibles number as verse 2" | "…through the prophecy" · "one continuous prophetic unit in the scroll" · "even the prophetic unit he had begun" · "what our Bibles number as verse 2" |
| R5 | ch28 sidebar, Luke 17 | "They ask where the taken ones go, and the answer invokes a corpse… That sounds like judgment rather than transport to safety." | "The exact antecedent of their question is debated, but Yeshua answers with a corpse and gathering vultures, which pushes the scene toward judgment rather than making *taken* automatically mean transport to safety." |
| L1 | ch27 layout | the "Rule — metaphorical does not override bodily" box started with two lines at the foot of p.33 | The box is now `::: {.commentary .keep}` and prints whole on p.34. The new CSS class `div.keep` affects **only boxes that carry it**. Commentary boxes stay breakable by default because some run past a page, so no other Part reflows. |

**Knock-on from L1:** the ch27 classification table now breaks after the 1 Corinthians row and continues on p.39 under a repeated header, with no row split. The layout gate permits this (LAYOUT-003), and I checked it visually.

**Checklist:** the same checklist used on Parts I–IV, with Parts VIII–IX as the benchmark. **No argument rewritten, no conclusion changed, no grade moved.** Chapter architecture unchanged.

**Result:** normalization 0 in every category. Before: 3 unstyled grades, 5 labels, 21 gloss gaps, 14 conventions. Build: 73 pages, 0 mojibake, 0 sections missing. The original-language gate passes on 17 pages and the table gate on 13 pages; I checked all of them visually.

## A. Checker (report-only, 54 tests)

- **Added:** old chain titles are now flagged: "Growing Chain — Checkpoint N" / «Cadena creciente — Punto de control N». Part II's box was normalized to "The growing chain — checkpoint 2", but ch29 (and Part VI) still used the old form. Four tests cover the old and new forms in both languages.

## B. What changed

### Titles (4 generic → descriptive; title line only)

| Ch | Before | After |
|---|---|---|
| 25 | How strongly evidence bears — against the reading I was moving toward | **Matthew 13's harvest** — against the reading I was moving toward |
| 26 | How strongly evidence bears — against a purely administrative reading of the transition | **Luke 20** — against a purely administrative reading of the transition |
| 26 | How strongly evidence bears — a correction to my own earlier scope work | **Hebrews 2:5** — a correction to my own earlier scope work |
| 27 | Historical context — the resurrection question was contested, and the texts show it | The resurrection question was contested, and the texts show it |
| 29 | Growing Chain — Checkpoint 3 | The growing chain — checkpoint 3 |

"Word study — …" titles stay; the benchmark uses them too (ch42–51).

### Grades

All three were "**CONTRADICTS** — …" opening a paragraph. Each became a sentence with the evidence as subject and the grade as a span. The strength and the object are unchanged:
- ch25: "The harvest material <span>contradicts</span> the thin version of the hypothesis…"
- ch26: "Luke 20 <span>contradicts</span> any version of my developing model…"
- ch26: "Hebrews 2:5 <span>contradicts</span> any use of my scope work…"

### Original language

All old `*(x)*` transliterations became `(*x*)`, except in table cells (as in Part IV). Transliterations were added where missing: *aiōn* and *synteleia tou aiōnos* (ch25 title), *kosmos*, *rabbim* (ch25 title, ch27), *katēntēken*, *telos*, *oikoumenē*, *to telos*, *paralambanetai*, *aphietai*, *yeshoteṭu* and *ha-daʿat* (ch29 title).

### Research-process language

| Ch | Before | After |
|---|---|---|
| 25 | age-ending language **cashes out** entirely as | **reduces** entirely to |
| 25 | **At Stage 25** it destroyed a bridge | **In Chapter 23** it destroyed a bridge (Stage 25 = ch23, where Paul never chooses *oikoumenē*) |
| 25 | I **retrieved** this and then deliberately stopped | I **noted** this… |
| 25 | summary: — **retrieved**, recorded, and not yet used | — recorded, and not yet used |
| 26 | The problem dissolved **on retrieval** | dissolved **once I read the passage** |
| 27 | **Retrieval debt, stated rather than filled:** the broader Second Temple literature… has not been **retrieved in this pass** | **What this box does not cover:** the broader Second Temple literature… **I have not worked through it here**, and I am not going to characterize a body of literature I have not read. *(The scope limit stays printed at the same strength; only the debt/retrieval framing went.)* |
| 27 | I **retrieved** the surrounding verses as a block | I **read** the surrounding verses as a block |
| 27 | And the **verified** passages, classified | And the passages, classified |
| 28 | **Retrieval** made it sharper than that | **A closer reading** made it sharper |
| 28 | What the hypothesis must **discharge** | must **account for** |
| 28 | It clarified what the hypothesis **owes** | **has to show** |
| 28 | did not survive **retrieval** (Zechariah 14 details) | did not survive **a check of the text** |
| 28 | I have not **retrieved** that passage **in this pass**, and I am recording it as reported rather than verified (Josephus) | I have not **checked** that passage **myself**, so I am treating it as reported rather than verified |
| 28 | carrying five specific **debts** | five specific **burdens** |
| 29 | I am **thirty-one stages** into building a chronology | I am **deep** into building a chronology |
| 29 | My hypothesis goes further and therefore **owes more** | **has more to prove** |
| 29 | After **thirty stages** of refusing to build on resemblance | After **all these chapters** of refusing… |
| 29 | a hypothesis that **owes five specific debts** | that **carries five specific burdens** |

Section labels: "Where we are." / "What it earned." → "Where this leaves us." / "The question this leaves." (all 5 chapters).

### Reference fixes

| # | Where | Before | After | Why |
|---|---|---|---|---|
| **N1** | ch26, ch28 | "**Chapter 17** is where I learned what happens when a shared lemma gets quietly counted as corroboration" / "the rule I adopted after **Chapter 17**" | **Chapter 21** in both | Chapter 17 is *clean and unclean*. The shared-lemma lesson comes from the Romans 10:18 *oikoumenē* bridge and Romans 10:4's *telos*, which is research Stage 23 = **Chapter 21**. Same leak as before: a stage number written as a chapter number. |
| **N2** | ch29 | "The caution I adopted **in Part IV** applies unchanged: *until* guarantees…" | "One caution applies here, and it will apply to every *until* in this book; **call it the until-reversal caution.** *Until* guarantees…" | The caution was written into the research methodology at Stage 26, but **no Part I–IV chapter contains it** (checked all 24). The reader would be pointed at something never shown. It is now introduced here, with the same wording and strength. |
| **N3** | ch29 summary list | "the resurrection taxonomy, **category-lock**, …" | "the resurrection taxonomy, **classification before harmonizing**, …" | "Category-lock" is never introduced anywhere in the book. The substance (ch27: "classify each passage by its own markers before harmonizing anything") is. |

**Logged for Part VII (BIBLE-3c7), not touched:** ch41 says "My own Until-Reversal Caution, written **four Parts ago**". After N2 it should say *two* Parts ago (V → VII).

## C. Checked and left as is

- **Cross-references, all checked:** ch25 "Chapter 21 records what that cost me", "since Part II", "Part III"; ch26 "Part III … Part IV", "Part II and Part IV" (*oikoumenē*: ch7 and ch23); ch27 "two chapters ago" (ch25); ch29 "four chapters ago" (ch25), "three chapters in a row", "the brake that killed my trumpet bridge" (ch27). All correct.
- "I spent Part III building" / "the phrase I spent the last chapter on": ordinary time usage, not the money metaphor.
- ch25 table header "Stage in Matthew" and ch27 "demonstrate multiple stages from Scripture": ordinary English, not internal labels.
- "Recorded. Not used." / "I am recording…": first-person statements of evidence strength, kept as in Parts I–IV.
- ch28 Nicaea "a date I am carrying rather than having verified": reader-facing scope honesty, kept.
- ch28 "That comparison is surgical work and it is bookmarked, not done" and ch27 "I am bookmarking it": they state what the book defers. Kept.

## D. Typesetting note (fixed in r1.1, L1)

p.33 (draft build): the "Rule — metaphorical does not override bodily" box starts with two lines at the foot of the page and continues overleaf. The table gate doesn't cover boxes, so this is noted for the typesetting pass.

## E. Decisions for you

1. Approve the 4 titles plus the chain title as a set?
2. N1–N3: the corrected chapter number, the until-reversal caution introduced in ch29 instead of being credited to Part IV, and "category-lock" replaced. OK?
3. ch27's "Retrieval debt" paragraph rewritten as "What this box does not cover", with the limit kept printed. OK?

## F. Spanish Part V: normalization (2026-10-14). Revision 1.1: APPROVED.

D2 (ch27 and ch29 boxes hidden whole) and N4 («Esto matiza el capítulo 7») are approved. **r1.1 language fixes**, verified in the rebuilt PDF (78 pages, all gates OK, normalization 0):

| # | Where | Before | After |
|---|---|---|---|
| S1 | ch26 | «La palabra que dediqué la Parte II y la Parte IV a establecer…» | «La palabra a la que dediqué la Parte II y la Parte IV para establecer…» |
| S2 | ch27 | «la frase no puede hacerse significar *no es un cuerpo*» | «la frase no puede forzarse a significar «no es un cuerpo»» |
| S3 | ch28 | «encoger el año 70 hasta *los romanos derribaron un edificio*» | «reducir el año 70 a «los romanos derribaron un edificio»» |
| S4 | ch28 | «nótese lo que la etiqueta compra» (calque) | «nótese qué ventaja ofrece la etiqueta» |
| S4b | ch28, same calque (not flagged) | «La distinción me compra espacio cronológico. No me compra…» | «…me da espacio cronológico. No me da…» |
| S5 | ch28 | «…en vez de un derrotador de ella — y si ese puente llega a construirse, se vuelve un derrotador» | «…queda como un texto de control importante para mi hipótesis, no como una refutación; si ese puente llega a construirse, **se convierte** en una.» *(The reviewer suggested «podría convertirse»; I kept «se convierte», because EN says "it becomes a defeater" and the strength should not drop.)* |
| S6 | ch28 | «una consumación del primer siglo de *un* siglo» | «la consumación de *un* siglo en el primer siglo» |
| S7 | ch29 | «Miguel está atado a **el pueblo de Daniel**» | «Miguel está ligado **al pueblo de Daniel**» |
| S8 | ch29 | «eso es la condición de falsación llegando y no una objeción…» | «…haciéndose efectiva, no una objeción…» |

A search of Spanish Part V found no further «compra», «derrotador», «hacerse significar» or «a el».


**Result:** normalization 0 in every category. Before: 3 unstyled grades, 12 labels, 21 gloss gaps, 24 conventions. Build: 78 pages, 0 mojibake, 0 sections missing, register 0, terminology 0. Original-language gate OK on 16 pages; checked visually, together with all 15 table pages. Provenance and evidence strength match EN.

### F1. Every English row walked against the Spanish files

| EN row | ES counterpart | Status |
|---|---|---|
| 4 titles + chain | «La siega de Mateo 13 — en contra de la lectura hacia la que yo iba» · «Lucas 20 — en contra de una lectura meramente administrativa…» · «Hebreos 2:5 — una corrección a mi propio trabajo anterior sobre alcance» · «La resurrección era discutida, y los textos lo muestran» · «La cadena creciente — punto de control 3» | done (5/5) |
| 3 grades | «El material de la siega / Lucas 20 / Hebreos 2:5 <span>contradice</span> …» | done (3/3) |
| glosses | `*(x)*` → `(*x*)` outside tables; added *kosmos* (×3), *aiōn* / *synteleia tou aiōnos* and *rabbim* (titles), *katēntēken*, *telos*, *oikoumenē*, *rabbim*, *to telos*, *paralambanetai*, *aphietai*, *yeshoteṭu* / *ha-daʿat* (title) | done |
| ch25 "cashes out" | ES «se resuelve enteramente en» was never a money metaphor | already correct |
| ch25 "At Stage 25" | «En la Etapa 25» → «En el capítulo 23» | done |
| ch25 retrieved / summary | «Lo recuperé» → «Lo anoté»; «— recuperado, registrado y…» → «— registrado y…» | done |
| ch26 "dissolved on retrieval" | «al recuperar el texto» → «en cuanto leí el pasaje» | done |
| ch27 "Retrieval debt" | «Deuda de recuperación…» → «Lo que este recuadro no cubre: la evidencia judía más amplia… la literatura del Segundo Templo, Josefo sobre los partidos y la discusión rabínica posterior» (includes r1.1 R2) | done |
| ch27 retrieved / verified passages | «Recuperé los versículos» → «Leí…»; «los pasajes verificados» → «los pasajes» | done |
| ch28 Retrieval / discharge / owes / survive retrieval / Josephus / debts | «La recuperación lo volvió más filoso» → «Una lectura más atenta…»; «debe saldar» → «debe dar cuenta»; «Aclaró lo que debe» → «lo que tiene que mostrar»; «no sobrevivieron a la recuperación» → «a una revisión del texto»; «No he recuperado ese pasaje en esta pasada» → «No he revisado ese pasaje por mí mismo»; «cinco deudas concretas» → «cinco cargas concretas» | done (6/6) |
| ch29 stages / owes / debts | «treinta y una etapas» → «Estoy muy metido en la construcción de una cronología»; «debe más» → «tiene más que probar»; «treinta etapas» → «tantos capítulos»; «debe cinco deudas» → «lleva cinco cargas» | done (4/4) |
| section labels | «Dónde nos deja esto.» / «La pregunta que esto deja.» (5 chapters) | done |
| N1 | «capítulo 17» → «capítulo 21» (ch26 and ch28) | done (2/2) |
| N2 | «La cautela que adopté en la Parte IV…» → «Aquí se aplica una cautela, y valdrá para todo *hasta* de este libro; llamémosla la cautela del *hasta*.» | done |
| N3 | «el bloqueo de categorías» → «la clasificación antes de armonizar» | done |
| r1.1 R1 perfect | «acción completada con relevancia presente que continúa» → «presenta la llegada como un desarrollo completado cuyo estado resultante está a la vista» | done |
| r1.1 R3/R3b John 5 | finding, «porque Juan los separó», rule box «dice cuál es cuál», summary «Juan prueba…» — all four softened as in EN | done (4/4) |
| r1.1 R4/R4b Luke 4 | heading «a media oración» → «a mitad de la profecía»; «una sola oración en el rollo» → «una sola unidad profética continua»; «dentro de una sola oración, antes de su segunda cláusula» → «dentro de la misma unidad profética, antes de la siguiente cláusula coordinada»; «la oración que había empezado» → «la unidad profética…»; summary «a mitad de la oración que…» → «a mitad de lo que…» | done (5/5) |
| r1.1 R5 Luke 17 | «Preguntan a dónde van los tomados… Eso suena a juicio» → «El antecedente exacto de su pregunta se discute, pero Yeshúa responde con un cadáver…» | done |
| r1.1 L1 | `::: {.commentary .keep}` on «Regla — lo metafórico no anula lo corporal»; prints whole on p.36 | done |

### F2. Spanish-only

- **D2 (standing pattern):** five «Nota textual — deuda declarada» boxes (ch25–29) became hidden `<!-- SPANISH-SPECIFIC: … -->` comments with their full text kept. **Flagged:** the ch27 and ch29 boxes each end with a sentence telling the reader which half of a passage is quoted and which described (John 5's «y ahora es»; the seal table). That is still verification bookkeeping, so the whole box was hidden. If you would rather keep one line printed, ch29's «conviene que el lector sepa cuál mitad está citada y cuál descrita» is the candidate.
- **Term drift:** «pequeña temporada» → «el poco de tiempo» (ch28, ×4), including the label: «Hipótesis post-milenial **del poco de tiempo**». No other Spanish chapter uses the label.
- **N4 (ES ch25):** «**Esto corrige un registro anterior de este mismo proyecto.** En la Parte II quedó anotado que la RVR1960 *nunca* ofrece *fin del mundo*… Registrado y corregido en el libro de sincronización.» → «**Esto matiza el capítulo 7.** Allí la RVR1960 dejaba bien servido al lector con *siglo* en 24:3, y en 24:3 lo sigue dejando. Pero la traducción no es uniforme: en 28:20 dice *mundo*.» I checked ES ch07: the printed text never says «nunca». It says, correctly, that RVR1960 has *siglo* at 24:3. So the old sentence corrected something from the sync ledger the reader never saw. The new one qualifies what the reader actually read. The 28:20 finding is unchanged.
- **Not touched:** ch25's reader address in *usted* («el capítulo que usted está leyendo… su Biblia»). ES-REGISTER records it as an edition-wide copyedit item, to be swept across all Parts at once.

### F3. Sweep for process vocabulary the checker can't see

Every remaining printed hit was checked: «registro/registrado» (first-person record of evidence strength, as in EN), «pendiente» (resurrection still ahead, the theological sense), «por etapas / varias etapas» (staged fulfilment), «saldrán» (John 5), «nunca me había registrado» ("had never registered with me"), «verificado» (Josephus and Nicaea scope honesty, as in EN).

**Logged for Part VII (BIBLE-3c7):** ES ch41's counterpart of "Until-Reversal Caution, written four Parts ago" should match the name introduced here, «la cautela del *hasta*».

## G. Decision for you

1. Hide the ch27 and ch29 boxes whole (D2), or keep ch29's last sentence printed?
2. N4: the ES ch25 drafting-history sentence becomes a note that qualifies ch7. OK?
