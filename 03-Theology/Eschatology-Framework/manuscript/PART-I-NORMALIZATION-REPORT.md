---
title: "Part I — Normalization Report (EN pilot)"
type: manuscript-report
created: 2026-10-13
status: closed-both-editions
related: "[[10-manuscript-architecture]], [[EDITORIAL-RULES]], [[PART-IX-DRAFT-REPORT]]"
---

# Part I — Normalization Report (English pilot)

## Revision 1.1: decisions applied (2026-10-13)

| # | Decision | Applied |
|---|---|---|
| D1 | **Keep** the ch02 clause that shows the four grades where the scale is introduced | No change (N11 stands) |
| D2 | **Update** the foreword so it matches Part VIII's *contradicts* | 00a: "rejected, because the evidence for it was weak **and the evidence against it proved decisive**, and because I do not get to …" |
| D3 | **Keep** "four" removed; do not add the other Elijah texts unless a later substantive review needs them | No change (N13 stands) |

Part VIII slips stay closed until the full-book audit. Spanish Part I starts only after English approval.

---

**Phase:** Book One consolidation (bead BIBLE-3c7, architecture §13 ruling ㉓). The benchmark is Parts VIII–IX. Part I is the pilot: the checklist is proven here, then reused for Parts II–VII.

**Scope held:** no settled argument rewritten and no conclusion changed. Chapter architecture is unchanged. One factual correction was made (N1).

## A. Automated checks added (build-manuscript.py, report-only)

`check_normalization()` now runs on every build in both languages. It prints findings and does not fail the build. The pilot showed where it is wrong, and **the checker was fixed, never the prose.**

| Category | Catches |
|---|---|
| decor | emoji and decorative symbols (✅ ★ ⚠ …). Plain arrows (→ ↓) and math symbols (≈) are allowed. |
| grade | evidence grades written in capitals instead of a grade span (SUPPORTS, APOYA …) |
| label | research-process leaks: "Stage 61", stage-talk without a number ("five stages"), SYNC/PR/q-numbers, bead ids, visible scope labels. Anything inside HTML comments is exempt. |
| gloss | GLOSS-001: a Greek/Hebrew term with no transliteration at first use |
| structure | a second chapter-level heading (the Coda is allowed); headings deeper than ### |
| convention | the pre-VIII box labels ("Where we are.", "What it earned.", and the ES equivalents) and `---` rules around boxes |

**Calibration against the benchmark:**

1. The first run flagged 37 legitimate gloss forms in Part VIII. Each one was the checker's error. All benchmark forms are now accepted: `term (*translit*)`, `(term, *translit*)`, `*translit* (term)`, quoted clauses of 3+ words, blockquoted verses, and table rows.
2. Spanish lowercase *etapa* was dropped from the stage-talk check. It is ordinary Spanish (ES ch53, «dos etapas» = the two-stage structure of Rev 20:5).
3. Part IX now reports zero in both editions.

**30 regression tests** pin these cases (`test-build-checks.py`); all pass.

**The calibration found real defects in already-closed Part VIII.** These have not been touched (Part VIII is closed); they are logged for the full-book audit:

- EN ch47 ("across the preceding fifty-eight stages")
- EN ch49 (same phrase)
- ES ch51 («Una etapa anterior de esta investigación»)
- EN ch47 still prints a SOURCE-LANGUAGE label (known, BIBLE-3c7)

## B. Part I (English): what changed

**Result:** every category went to 0.

| Category | Before | After |
|---|---|---|
| unstyled grades | 3 | 0 |
| stage-talk | 5 | 0 |
| old box labels + rules | 19 | 0 |

The full scan finds no emoji, visible labels or heading problems anywhere in Part I. Build: 54 pages, all gates OK.

### Conventions (mechanical, all chapters)

- "**Where we are.**" → "**Where this leaves us.**" (6 times)
- "**What it earned.**" → "**The question this leaves.**" (6 times). Each box was read first: all six already end on the question the next chapter takes up, so the new label fits without changing any box text.
- `---` rules removed before and after boxes. The foreword's `***` section breaks stay; they are scene breaks, not box rules.

### Specific edits

| # | Where | Before | After | Why |
|---|---|---|---|---|
| **N1** | ch06 | "Part **VII** of this book spends a long time on the difference" | "Part **IV** …" | **Factual cross-reference error.** Part VII (ch40–46) is about resurrection, Daniel, Paul and PF-01. The apostolic-commission vs ordinary-witness distinction is worked out in Part IV, ch24 ("'Everything I commanded' does not distribute every role"; "Corporate mission, individual vocation"). |
| N2 | 00a | "investigated **for three stages** and rejected" | "investigated **at length** and rejected" | RESEARCH-PROCESS-002 |
| N3 | ch03 | "a contradiction **in this stage**" | "**at this point**" | RESEARCH-PROCESS-002 |
| N4 | ch04 | "my favorite thing that happened **in this stage**" | "**at this point**" | RESEARCH-PROCESS-002 |
| N5 | ch05 | "there is **a stage** much later" | "**a point** much later" | RESEARCH-PROCESS-002 |
| N6 | ch06 | "I had spent **five stages**" | "**five chapters**" | RESEARCH-PROCESS-002 |
| N7 | ch04 | "I **filed** the food question **as a sidebar to be worked later**" | "I **set** the food question **aside to be examined later**" | bookkeeping verb (RESEARCH-PROCESS-002) |
| N8 | ch06 | "I had that last point backwards **in an earlier draft**. I wrote that … and then, **four pages later**, cited Acts 21:8 … **Both sentences were in the same chapter.**" | "I had that last point backwards **at first**. I had the people announcing in Acts 8 as the ones Luke does not identify by office, while Acts 21:8 calls one of them Philip the evangelist. **Both claims could not stand.** One of them had to go, and it was not the one with a verse attached." | The old text narrated the manuscript ("draft", "pages") rather than the investigation. The correction itself is kept at the point where it happened (architecture §11, Appendix G rule). Only the drafting bookkeeping is gone. |
| N9 | ch04 | "The verb is **euangelizo**, announcing good news." | "The verb is <span>εὐαγγελίζω</span> (*euangelizō*), announcing good news." | GLOSS-001: original + transliteration + gloss. This is the lemma; the chapter makes no claim about the form. |
| N10 | ch06 evidence box | **REQUIRES** — / **SUPPORTS** — / **DOES NOT ESTABLISH** — | grade spans *requires* / *supports*; "**Does not establish**" in plain bold | TYPOGRAPHY-002. The benchmark spans only the four grades; "does not establish" stays plain (as in ch49). |
| N11 | ch02 | "Most of what people call proof lives at permits." / "I will use those four words throughout, and …" | "… lives at <span>permits</span>." / "I will use those four words throughout, **set apart in the text like this** — *contradicts*, *permits*, *supports*, *requires* — and …" | The scale's first appearance now shows the reader the visual form used for the rest of the book. One connective clause is added (see decision D1). |
| N12 | ch01 open-question box | label "**Open question**" | "**"All nations" and "all the world" — not yet examined**" | Benchmark open-question boxes carry a descriptive title (ch50, ch52). |
| N13 | ch03 | "So **the four texts** sit side by side" | "So **the texts** sit side by side" | Only two texts are cited in the chapter (John 1:21, Matt 11:14). The source (00c) holds four, including Luke 1:16–17. The number is dropped; no content is added. |
| N14 | ch06 | "predicar no es lo **mio**" | "*predicar no es lo **mío***" | Missing accent; ch01 has it right. Italic for the Spanish phrase. |
| N15 | ch06 | "I am deliberately not ranking … here. … **I am not going to adjudicate that here.** What matters …" | second sentence removed | Same statement twice in a row. |

## C. Decisions for you

1. **D1 (N11).** Is it acceptable to show the four grade forms where the scale is first introduced? It is one added clause.
2. **D2.** The foreword says a theory was rejected "because the evidence for it was weak." Part VIII later graded the inserted millennium <span>contradicts</span>: the Hijri count is decisive. The sentence is not false, because the evidence for it was weak, but it understates the final result. I left it as written. Options: keep it, or change it to "because the evidence for it was weak and the evidence against it decisive."
3. **D3 (N13).** Drop the number (done), or name all four Elijah texts (this adds content: Luke 1:16–17 and the fourth text in 00c)?

## D. Not resolved here (needs substance, or belongs to the full-book audit)

- The "second week" in the foreword and "the second or third week" in ch06 are compatible. No change.
- Cross-references to later chapters were checked only where a sentence names a Part or chapter number in Part I: ch01 "Chapter 23" is correct, ch06 "Chapter 2" is correct, and N1 was fixed. A full cross-reference sweep belongs to the full-book consistency audit.
- The Part VIII leaks listed in A.

## E. Spanish Part I

Not started; it waits for English approval. The scan shows ES Part I needs the same conventions pass (17 old labels and rules, 3 unstyled grades) plus the matching N-edits where they apply. The N1 cross-reference must be checked in ES ch06 as well.

---

# Spanish Part I — normalization (2026-10-13)

**English r1.1 was approved and frozen:** snapshot **d2-normalized** (`65f72b8` / `28f412e`). Spanish Part I is normalized from that approved baseline, applying the same rules and the same decisions. The prose stays written in Spanish rather than translated from the English edits.

**Result:** normalization 0 in every category (before: 17 old labels/rules, 3 unstyled grades, 6 stage-talk). Register 0, terminology 0. Build: 56 pages, 0 mojibake, 0 sections missing, original-language gate OK. I visually checked pp. 17, 21, 34, 41, 50.

| EN # | Spanish edit |
|---|---|
| conventions | «Dónde estamos.» → «**Dónde nos deja esto.**» · «Qué se ganó.» → «**La pregunta que esto deja.**» · `---` rules around boxes removed |
| **N1** | ch06: «la **Parte VII** de este libro» → «la **Parte IV**» (same factual error as EN) |
| N2 + D2 | 00a: «investigada **durante tres etapas** y descartada, porque la evidencia a su favor era débil, y porque…» → «investigada **a fondo** y descartada, porque la evidencia a su favor era débil **y la evidencia en contra resultó decisiva**, y porque…» |
| N3, N4, N5, N6 | «En esta etapa» → «En este punto» (ch03) · «de esta etapa» → «de este punto del recorrido» (ch04) · «una etapa mucho más adelante» → «un momento mucho más adelante» (ch05) · «cinco etapas» → «cinco capítulos» (ch06) |
| N7 | ch04: «**Archivé** la cuestión de la comida **como nota lateral para trabajarla después**» → «**Dejé a un lado** la cuestión de la comida **para examinarla después**» |
| N8 | ch06: «**Un borrador anterior** tenía este punto al revés. **Escribí** … **cuatro páginas después** … **Las dos frases estaban en el mismo capítulo.**» → «**Al principio** tenía este punto al revés. **Tenía** a los que anunciaban en Hechos 8 como … mientras que Hechos 21:8 llama a uno de ellos Felipe el evangelista. **Las dos afirmaciones no podían sostenerse juntas.**» |
| N9 | ch04: «euangelizo» → <span>εὐαγγελίζω</span> (*euangelizō*) |
| N10 | ch06 evidence box: **EXIGE** / **APOYA** → grade spans; **NO ESTABLECE** → «**No establece**» |
| N11 + D1 | ch02: «vive en <span>permite</span>» + «destacadas en el texto así — contradice, permite, apoya, exige —» |
| N12 | ch01 open-question box: «Pregunta abierta» → «**«Todas las naciones» y «todo el mundo»: todavía sin examinar**» |
| N13 + D3 | ch03: «los **cuatro** textos» → «los textos» |
| N14, N15 | Not needed: ES ch06 already has «mío», and the duplicated sentence exists only in EN. |

**One pre-existing defect fixed (Spanish only).** ES ch05's Romans 9:4 textual note (Spanish-specific, RVR1960 «el pacto») had its Greek variant as bare bold text: **αἱ διαθῆκαι** / **ἡ διαθήκη**. The original-language gate added after Part I closed now fails that, so this build stopped on it. It is now <span>αἱ διαθῆκαι</span> (*hai diathēkai*, «los pactos») and <span>ἡ διαθήκη</span> (*hē diathēkē*, «el pacto»). The note's claim is unchanged.

**Bilingual parity:** grade spans, boxes, Greek spans and box labels match chapter by chapter. The one difference is ES ch05's extra `textualnote`, which is the sanctioned Spanish-only Romans 9:4 note.

## Spanish verdict (2026-10-13): APPROVED

Spanish Part I normalized r1 approved. **Part I is normalized and closed in both editions.** Next: Part II English normalization, same checklist, Parts VIII–IX as benchmark.
