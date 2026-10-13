---
title: "Part III — Normalization Report (EN)"
type: manuscript-report
created: 2026-10-13
status: en-approved
related: "[[PART-II-NORMALIZATION-REPORT]], [[PART-I-NORMALIZATION-REPORT]], [[10-manuscript-architecture]], [[EDITORIAL-RULES]]"
---

# Part III — Normalization Report (English)

## Revision 1.1: review fixes applied (2026-10-13). English Part III APPROVED.

D1 (ch18 verification diary hidden, results printed) and the 13 titles are approved as a set.

| # | Fix | Applied |
|---|---|---|
| R1 | ch14 (p19): the four-option box printed "1." then "(b), (c), (d)" | **Cause:** a paragraph opening with "(a) " is parsed by Pandoc as an ordered list and printed as "1.". Escaped as `\(a)`. **The checker now flags this pattern** (2 tests). It finds exactly one other case, ES ch14, to be fixed in the Spanish pass. |
| R2 | ch16 summary (p40): "Circumcision predates Sinai and **predates** the righteousness it seals", which contradicts the chapter's own Genesis 15:6 → 17 ordering | "Circumcision predates Sinai, **but the righteousness it seals precedes it.**" **Factual fix:** a pre-existing error in the summary box, not introduced by normalization. |

Both lines were verified in the rebuilt PDF.

**Checklist:** validated on Parts I–II, with Parts VIII–IX as the benchmark. **No argument rewritten, no conclusion changed, no grade moved.** Chapter architecture unchanged.

**Result:** normalization 0 in every category (before: 10 unstyled grades, 5 project/stage-talk, 14 gloss gaps, 10 generic titles + 14 old labels/rules, 1 ⛔). Build: 69 pages, 0 mojibake, 0 sections missing. Original-language gate OK on 14 pages, all visually checked.

## A. Checker

- **Word-study header form accepted:** `<span>κοινός</span> · *koinos* · common`. The span capture was 3 characters and ` · *` is 4; the bug was mine and is fixed, with a regression test. Total tests: 40, all passing.
- Benchmark and Parts I, II and IX unchanged. Part I's single hit is the ch01 "this project" origin line already logged.

## B. What changed

### Conventions, titles, grades, original language

Same treatment as Part II:

- Box labels and rules updated.
- 10 generic titles made descriptive:
  - ch13: *To cut a covenant*; *Berit olam* on three institutions; Covenant as an ancient Near Eastern form
  - ch14: Jeremiah 31:33 — where the Torah goes; Ezekiel 37:24 — Torah-keeping inside the everlasting covenant
  - ch16: Circumcision moved inward, inside the Tanakh
  - ch17: Peter's vision — what Luke makes explicit; *Koinos* and *akathartos* in Romans 14:14
  - ch18: *Sabbatismos* after Genesis 2
  - ch19: Israel's covenant vocabulary, applied to communities including Gentiles
- Two "contrary evidence" titles now name their verse (Zechariah 6:13; Isaiah 53:10).
- ch19's chain box follows the benchmark: "The growing chain — checkpoint 2".
- Capitalized grades are now grade spans. Non-grade phrases ("does **not** establish", "**established**") are plain bold. Claim types ("explicit text") are plain words.
- Bare-bold Hebrew and Greek are now wrapped and glossed (בְּרִית, διαθήκη, בְּרִית עוֹלָם ×2), and the old `*(x)*` transliterations become `(*x*)`. ch17's second καθαρίζων got its transliteration.

### Research-process language

| Ch | Before | After |
|---|---|---|
| 13 | flagging that and deliberately **not spending it** … **cashing it** early | **noting** that and deliberately **setting it aside** … **using it** early |
| 13 | neither the circumcision **stage** nor my own notes | the circumcision **work** |
| 13 | the lexical study of *olam* is still **owed**. This finding does not **discharge** it. | still **to be done**. This finding does not **replace** it. |
| 14 | textual note: "I record it because I **hit it the expensive way**: a first attempt **to fetch** CJB 'Jeremiah 31:34' returned…" | removed. The note keeps the reader-useful fact (the CJB is one verse behind in this range; check wording, not number). |
| 14 | Ezekiel 40–48 is **bookmarked** … **Cashing it** mid-chapter would repeat the error **this project avoided earlier with Daniel 2** | **set aside** … **Opening it** mid-chapter would mean deciding a large question inside a small one. *(Daniel 2 is not discussed anywhere before ch14, so "earlier" pointed at research order the reader never saw.)* |
| 14 | I would rather **file** it that way | **leave** it that way |
| 14 | **This project** is not inventing symbolism | **This book** |
| 15 | the most useful thing **this stage** produced | **this chapter** |
| 16 | heading: The verse that guards the whole **project** | whole **argument** |
| 16 | open question titled "**and I was supposed to close it here**"; "This chapter **was expected** either to resolve that or to explain why it cannot, and…" | title "**What Paul means by 'the commandments of God'**"; "I do not know, and the reason is specific: …" *(narrated a planned deliverable)* |
| 17 | "**Researcher's commentary —** …" (3 box titles) | prefix dropped, titles kept (benchmark commentary boxes carry content titles only) |
| 17 | "I **inserted this** before reading Romans 14 rather than after" | "This comes before Romans 14 rather than after" |
| 17 | Recorded per the rule **this project gave itself** | Kept under the rule **this investigation set itself** |
| 18 | Chapter 13 … deliberately **did not spend it**. Here is where it **gets spent**. | **set it aside** … Here is where it is **taken up**. |

### ch18 — the verification diary (needs your approval: D1)

The *sabbatismos* word-study box printed a research diary: ⛔, "a Perseus lookup … returned the wrong treatise", "a full-text search located…", and a to-do list ("To close it: obtain the Greek text of Plutarch *Moralia* 166A … then check Justin Martyr …").

**Now printed:** a sub-heading, "What could and could not be confirmed outside the New Testament", followed by:

- **Established:** occurs once in the NT; Thayer cites Plutarch, *De Superstitione* c. 3, plus ecclesiastical writings.
- **Not confirmed:** the Sabbath passage sits at §8, not §3, and the Greek word was not confirmed at either place. The attestation stands as "**reported by a lexicon, not independently verified**".

**Every result is kept at exactly its old strength.** Only the search narrative and the to-do list moved, into a hidden `<!-- VERIFICATION TRAIL -->` comment with the full original text. This is the same principle as the Spanish D2 decision.

Unchanged, because it narrates the method rather than the paperwork: the paragraph after the box ("this was the first time I applied a rule I had just written…") and the "Lexical Escalation" finding.

### Factual / reference fixes

| # | Where | Before | After | Why |
|---|---|---|---|---|
| **N1** | ch19 | "the **fourth** passage in this project where an English rendering has been quoted to me as though it were the verse — after Mark 7:19's parenthesis, Hebrews 4:9's *sabbatismos*, **and Colossians 2:14**" | "the **third** passage in this investigation … after Mark 7:19's parenthesis and Hebrews 4:9's *sabbatismos*." | Colossians 2:14 appears nowhere in the book before this sentence (ch18 discusses Col 2:16–17), so the reader could not follow the count. |
| **N2** | ch14 | "2 Corinthians 6:16 quotes Ezekiel 37:27, and I flag that citation as **not yet verified by me** rather than leaning on it." | "2 Corinthians 6:16 **appears to quote** Ezekiel 37:27, a citation this chapter does not lean on." | The verification narration is removed. **The hedge is kept ("appears to"), so the claim is not strengthened.** |

## C. Deliberately NOT changed

- **ch13 opening** ("This chapter did not exist when I needed it… In the research it came fourth"). The Note to the Reader promises exactly this: "Where I moved a chapter out of the order I actually worked in, I say so in the chapter and tell you why." It stays.
- ch15's "full apparatus work is beyond what I have done", ch17's "syntax and discourse analysis I have not done", ch19's "Greek work I have not done". These are honest epistemic limits stated to the reader, not process narration.
- Cross-references checked and correct: ch13 "two chapters from now" (ch15); ch15 "three chapters from now" (ch18); ch16 "two chapters ago" (ch14); ch18 "Chapter 13" and "Chapter 15"; ch19 "back in Part II" (Isaiah 19 in ch08); ch14 "Part IV".

## D. Decisions for you

1. **D1:** the ch18 verification diary is now a hidden comment, with all results printed at their old strength. Approve?
2. **Titles:** approve the 13 new titles as a set?

## E. Spanish Part III

Waits for English approval. It has 3 more «deuda declarada» boxes (ES ch13, 16, 19), which get the D2 treatment unless one carries reader-facing content.
