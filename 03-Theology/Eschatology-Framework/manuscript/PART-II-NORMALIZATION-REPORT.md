---
title: "Part II — Normalization Report (EN)"
type: manuscript-report
created: 2026-10-13
status: en-approved
related: "[[PART-I-NORMALIZATION-REPORT]], [[10-manuscript-architecture]], [[EDITORIAL-RULES]]"
---

# Part II — Normalization Report (English)

## Revision 1.1: review fixes applied (2026-10-13). English Part II APPROVED.

| # | Fix | Applied |
|---|---|---|
| R1 | ch12: the unexplained "eight" | "'Is the Law abolished?' is at least six distinct things — and more questions than that — wearing one coat." (resolves D1) |
| R2 | ch10 box title must not be more certain than the box text | "The *angeloi* of 24:31 — **most probably** heavenly, not missionaries" |
| R3 | ch11: research-process phrase the checker missed | "the strongest argument **this project has produced**" → "the strongest argument **I have found**" |

The other 18 titles were approved as a set. All three lines were verified in the rebuilt PDF. **Checker gap closed:** "this project" / «este proyecto» is now flagged (2 new tests). It also flags frozen Part I ch01 ("the true first sentence of this project", EN + ES); that is logged on BIBLE-3c7 for the full-book audit, and Part I is not reopened.

**Checklist:** the one validated on Part I (see PART-I-NORMALIZATION-REPORT), with Parts VIII–IX as the benchmark. **No argument rewritten, no conclusion changed.** Chapter architecture unchanged.

**Result:** normalization 0 in every category. Before: 14 unstyled grades, 5 stage-talk hits, 7 gloss gaps, 12 old labels/rules, plus the box-title and bare-Greek issues below. Build: 51 pages, 0 mojibake, 0 sections missing, original-language gate OK on 11 pages, and all 11 visually checked.

## A. Checker extended (still report-only)

Part II showed two patterns that recur through Parts II–VII, so the checker now catches them in every later Part:

- **Generic box titles.** EN Parts II–VII reuse fixed captions ("How strongly evidence bears" ×22, "Original language" ×12, "Historical context" ×5, "Finding" ×3). Every Part VIII–IX box names what it shows. Spanish equivalents are included.
- **The debt metaphor** (RESEARCH-PROCESS-002). It survives in EN box captions in ch27/33/37/41/43, and in the ES caption «Nota textual — deuda declarada» in **26 chapters** (ES ch08 onward). These will be handled Part by Part.

The benchmark still reports zero (Part VIII's 3 hits are the stage-talk leaks already logged). 37 regression tests, all passing.

## B. What changed in Part II

### Conventions (all six chapters)

- "Where we are." → "Where this leaves us." and "What it earned." → "The question this leaves." (6 each). Each "question" box was read first; all six fit.
- `---` rules around boxes removed.

### Box titles, generic → descriptive (title line only, box text unchanged)

| Ch | Box | New title |
|---|---|---|
| 07 | historical | The temple in the first century |
| 07 | evidence | What *oikoumenē* can carry at Matthew 24:14 |
| 07 | wordstudy | Romans 15:19 — what Paul fills up |
| 07 | evidence | Romans 15:19 and 23 — what they show and what they do not |
| 08 | evidence | Daniel 7:13 — which way the figure travels |
| 08 | historical | Storm and cloud as the language of judgment |
| 09 | evidence | Cosmic collapse in the Prophets — three kingdoms |
| 09 | historical | Pentecost (Shavuot) |
| 10 | evidence | Matthew 24:31 and Israel's regathering vocabulary |
| 10 | finding | The *angeloi* of 24:31 — heavenly, not missionaries |
| 10 | openquestion | One trumpet, or several? |
| 11 | evidence | Matthew 24:30, Revelation 1:7 and Zechariah 12 |
| 11 | finding | The land-sense of *gē* at Matthew 24:30 — supported, not established |
| 11 | finding | What a translation decides for its reader |
| 12 | evidence | Luke's "and all the trees" against the fig-tree code |
| 12 | evidence | Matthew 23:36 and "this generation" at 24:34 |
| 12 | wordstudy | Two "untils", side by side |
| 12 | evidence | Matthew 5:18 and 24:34 — a prompt, not a proof |
| 12 | wordstudy | Matthew 5:17 — the two verbs |

### Evidence grades (TYPOGRAPHY-002)

Capitalized grades in the evidence boxes and findings are now grade spans: contradicts / permits / supports / requires. Phrases that are not one of the four grades go to plain lowercase bold: "does **not** establish", "**strongly counts against**", "**establishes a reason to ask**". Claim types ("explicit text") become plain words. Wherever a grade was used as a verb, the sentence was turned minimally so the grade word itself carries it.

Examples:
- "It does not **REQUIRE** that sense" → "It does not reach <span>requires</span>"
- "**STRONGLY SUPPORTS** … It does not **REQUIRE** it" → "<span>supports</span> …, strongly. It does not reach <span>requires</span>"
- ch11 finding: "**permits** and is contextually **supported** in a covenantal-land sense by the Zechariah 12 background" → "<span>permits</span> a covenantal-land sense, and the Zechariah 12 background <span>supports</span> it"

Strength is unchanged in every case; no grade moved up or down.

### Original language (GLOSS-001 + original-language gate)

Part II had Greek in bold with no protected span (**αἰών**, **κόσμος**, **ἡ οἰκουμένη**, **γῆ** ×2, **ἄγγελος**, **συλλέγω**, **ἐπισυνάγω**, **παρουσία**, **φυλαί**, **καταλῦσαι**, **πληρῶσαι**). That is a gate failure: the stylesheet can mangle unprotected Greek. All are now wrapped and glossed, with transliterations in the benchmark form `(*translit*)` instead of the old `*(translit)*`. Glosses were added only where the sentence did not already give one (*aiōn*, age; *kosmos*, world; *hē oikoumenē*, the inhabited world; *gē*, land, earth; *angelos*, messenger). Two terms in the ch07 word study got their transliterations (*peplērōkenai*, *to euangelion*).

### Research-process language (RESEARCH-PROCESS-002)

| Ch | Before | After |
|---|---|---|
| 07 | I ended this stage with three live possibilities | I came out of this with three live possibilities |
| 08 | came out of this stage | came out of this chapter |
| 09 | I **logged** it as a real datum with an explicit **note** not to convert it… that note is doing more work | I **kept** it as a real datum, with an explicit **caution** against turning it into a rule, and that caution is doing more work |
| 09 | I had it **filed** as text | I had been **holding** it as text |
| 10 | something wrong here that took **thirty-seven stages** to catch | that was not caught **until Part VII** |
| 10 | which I made **at this stage** | at this point |
| 10 | Part VII is where **this project** catches it | where **the investigation** catches it |
| 10 | I ended this stage by writing down | I closed this part of the investigation by writing down |
| 10 | several things I believed **when I wrote this** | several things I believed **at this point** |
| 12 | which is **a dividend paid by** investigating in sequence | which is **the advantage of** investigating in sequence |
| 12 | I am **logging** it as a cost / one cost was **logged** | I **record** it as a cost / one cost was **recorded** |

### Factual fix

| # | Where | Before | After | Why |
|---|---|---|---|---|
| **N1** | ch08 | "That question gets its own chapter, **four** chapters from here." | "…**three** chapters from here." | The γῆ / "tribes of the land" question is ch11, three chapters after ch08 (ch12 is the fig tree and "this generation"). |

## C. Deliberately NOT changed

- **ch10's preserved error.** The claim that Matthew 13:41 shares 24:31's gathering verb stays exactly where it was made. The chapter says so, and Part VII narrates the correction. That is the architecture rule (corrections appear where they occurred), not a defect. Only the bookkeeping around it changed ("thirty-seven stages" → "until Part VII").
- **ch12, "six things" / "eight questions".** This looks like an inconsistency but is not one. The source has six categories (Torah, Mosaic covenant, priesthood, temple, sacrificial administration, moral commandments) and eight questions, listed in 00n. The chapter prints only the six, so the "eight" lands unexplained. It is left as written; optional decision D1 below.
- **"How claims are labeled" (claimtypes) legends** in ch07 and ch08 keep their capitalized claim types. They are a legend, not evidence grades.

## D. Decisions for you

1. **D1 (optional).** ch12's "at least eight questions wearing one coat" follows a list of six things. Leave it, or make it "at least six things, and more questions than that, wearing one coat"?
2. **Box titles.** The 19 new titles are editorial (title line only). Approve as a set, or name any to change.

## E. Spanish Part II

Not started; it waits for English approval. Spanish needs the same pass plus its first «Nota textual — deuda declarada» caption (ES ch08), which gets a descriptive title.
