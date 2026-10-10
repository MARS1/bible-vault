---
title: "Part VIII (EN) — Revision 2 report: change log, verification, completion checklist"
type: reference
category: theology
created: 2026-10-10
status: awaiting-author-review
related: "[[EDITORIAL-RULES]], [[PROVENANCE-LOG]], [[SYNC-LEDGER]], [[STRUCTURAL-DEBT]]"
---

# Part VIII (English) — Revision 2

**Status: at the review gate.** Nothing committed, no new snapshot taken, Spanish untouched, Part IX not started, Book Two material not inserted.

| | Before | After |
|---|---|---|
| Baseline snapshot (immutable) | `_snapshots/en/part-08/part-08-en-d1-prerev.*` (source commit `11ebad4`) | — |
| Pages | 141 | 100 |
| Words (reader-visible) | 21,771 | 19,807 |
| Build gates | — | terminology OK · 0 mojibake · 0 sections missing · all Greek/Hebrew wrapped · 0 split table rows |
| Reader PDF | — | `Desktop/7-MARS/Bible Study/en/Part 08/` and `_build/en/part-08-en.pdf` |

Compare chapter by chapter: `git diff 11ebad4 -- manuscript/en/ch4[7-9]*.md manuscript/en/ch5[0-2]*.md`, or the baseline `part-08-en-d1-prerev.pdf` against the new PDF.

---

## A. What changed in every chapter

1. **Research narration removed.** Debts, payments, sweeps, archives, files, stages "running," flattening, "earned" boxes, and every invented questioner ("someone asked me," "it was put to me," "a reader"). Genuine changes of reasoning kept, in the first person.
2. **Context restored.** Options (a)–(e) restated in words wherever cited; earlier findings briefly recalled; every Greek and Hebrew term transliterated and glossed at first use in a discussion.
3. **Typography.** No emoji, no checkmarks, no `###`-plus-bold emphasis, no mid-chapter `#` headings. Box labels only at the top of boxes. Evidence grades set as one formal label style.
4. **Endings.** Each chapter ends with "Where this leaves us" (plain findings) and "The question this leaves" (the open question and the next chapter) — restoring the `earned` component's original design purpose rather than self-praise.
5. **Chapter titles.** ch47 "What remains open, and how long is a little season?" · ch49 "A thousand years — what the number can and cannot tell us" · ch50 "The chronology under test" · ch51 "What clock — and the two little whiles." ch48 and ch52 unchanged.

---

## B. Factual and interpretive corrections (separate from editing)

Each was verified against a source during this revision. None changes PF-01, PF-02, or any graded conclusion except where a downgrade is noted.

| # | Chapter | Draft 1 said | Corrected to | Evidence |
|---|---|---|---|---|
| F1 | ch51 | Earthquake "complete sweep": 6:12, 6:13, 8:5, 11:13, 16:18; formula "at the trumpets and again at the last bowl" | Adds **11:19** (lightnings, voices, thunders, earthquake, great hail); formula traced 4:5 → 8:5 → 11:19 → 16:18–21 | SBLGNT, Rev 4:5, 8:5, 11:19, 16:18 |
| F2 | ch51 | Survey of "little/time" words complete | Adds **17:10** (ὀλίγον, "a little while"), **2:21** (χρόνος), **1:3, 11:18** (καιρός). Core claim **holds**: μικρός of time only at 6:11 and 20:3 | BLB concordance G3641, G3398, G5550, G2540 |
| F3 | ch51 | 6:11 and 20:3 "same noun, same adjective" (flagged for re-check) | **Confirmed**: ἔτι χρόνον μικρόν / μικρὸν χρόνον; 12:12 ὀλίγον καιρὸν | SBLGNT |
| F4 | ch51 | Horses: fourteen occurrences | **Sixteen** (in fifteen verses); last at 19:21 | BLB G2462 |
| F5 | ch51 | "not interchangeable descriptions of one event" | Cannot be assumed to be one earthquake; different wording does not prove separate events either | Overclaim against the book's own recapitulation model |
| F6 | ch51 | Horses reductio (Messiah's horse would be literal) | Horses cannot serve as an independent chronological marker | Logical overreach removed |
| F7 | ch49 | Article pattern "perfectly alternating" | **Downgraded**: firm in the three completion clauses; 20:4 and 20:6 have manuscript variants with the article | SBLGNT footnotes on 20:4, 20:6 |
| F8 | ch48 | Whether John uses σεισμὸς μέγας elsewhere "not swept" | He does: **6:12, 11:13, 16:18**. Stated as a datum, not proof of intent | SBLGNT |
| F9 | ch48, ch52 | παρεμβολή "lexical authority owed" | 213 LXX uses, standard word for Israel's wilderness camp (Exod 14:19–20; 19:16–17; Lev 4:12; Num 2); "camp of God" Gen 32:1–2; Heb 13:11–13 | BLB G3925 (LXX and NT) |
| F10 | ch52 | πόλεμος: "capacity, not distribution; sweep still owed" | All **nine** uses: 9:7, 9:9, 11:7, 12:7, 12:17, 13:7, 16:14, 19:19, 20:8. War against God's people = persecution every time; 20:9 not decided by the word alone | BLB G4171 (TR and critical text agree) |
| F11 | ch52 | — | **New note**: 13:7's clause is missing from Codices A, C and others, probably by accident | Pulpit Commentary; Cambridge Bible for Schools and Colleges (via BibleHub); SBLGNT prints it |
| F12 | ch52 | Early little season "keeps option (c) genuinely live" | **Logic inverted** — (c) means *we are not* in the little season. Source stage 03q l.491 says only that an early little season remains possible. Corrected. **The proposed reviewer fix ("Option C = an earlier start to the little season") would have cemented the error and was not used.** | ch47/49/50 definitions; `03q-who-are-the-saints-in-revelation.md` |
| F13 | ch50 | "The theory would delete the manuscript base" | **Redate, not delete** — matches the already-correct Spanish ch50 | Tranche 4 headline |
| F14 | ch50 | Decisive evidence: "tree rings, comets and a lunar calendar" | **Reweighted**: the Islamic calendar decides; comets and tree rings support | ch50's own source table |
| F15 | ch50 | 7,272-year chronology "paywalled, six ladder rungs failed" | Cited: Pilcher, Baillie, Schmidt & Becker, *Nature* 312 (1984): 150–52; data not examined | Crossref metadata `10.1038/312150a0`. No access controls circumvented |
| F16 | ch50 | "Nobody has even proposed the thing the model needs" | Scoped to Illig (297 years). The same chapter names Fomenko's New Chronology, which proposes rearrangements of that scale or larger | Internal contradiction |
| F17 | ch50 | Astronomical test = eclipses (per ch47) | Says plainly it was run with **Halley's comet** apparitions (6 of 8 located) | `03n-is-the-chronology-secure.md` l.29, 80 |
| F18 | ch50 | Hebrew calendar = "second independent count" | Consistent and corroborating; its era reckoning has its own history | Tranche 1 item 4 caution |
| F19 | ch47 | Eclipse note named the earth's rotation | Correction factor described operationally only | **Author's standing constraint** |
| F20 | ch47 | "about nine hundred years" | "nine hundred and fifty" (AD 70 + 1,000 = 1070; 2026 − 1070 ≈ 956), matching ch49–51 | Arithmetic |
| F21 | ch47 | — | Ethiopian calendar added: about seven to eight years behind Gregorian; the year beginning September 2026 is 2019 | Tranche 1 item 4 |
| F22 | ch48 | (Self-check during revision) | Theodotion point kept at its original strength: "a live question," not "matches" | Evidence-strength rule |
| F23 | ch51 | ψύχω "only here in Matthew" | Only here **in the New Testament** | BLB G5594 |

---

## C. Verification and exceptions report

### Author decisions, 2026-10-10

1. ch50: **"not adopted"** stands. Hypothesis E stays unresolved — neither established nor disproven.
2. "Fifteen stages": **not restored.** It refers to the research workflow, not to anything the reader needs.
3. Parts I–VII: a comparable editorial pass **later**, using the approved Part VIII as the benchmark. Not started.

### Needs your decision (original questions, now answered above)

1. **ch50, "the little season may already have run its course."** Draft 1 said this door was "recorded as closed." The evidence given is only that the final judgment has not been *established* as past, so the revision says "not adopted here." This sentence touches Hypothesis E. Please confirm the wording.
2. **"Fifteen stages."** Tranche 4 approved "A lexical test first identified fifteen stages earlier…". Under the later bookkeeping ban, the revision says "noted long before but not yet carried out" without the count. Restore the number if you prefer.
3. **Style gap with Parts I–VII.** Part VIII is now restrained; Parts I–VII still use emoji and heavy bold. The stylesheet fixes (below) will improve them on their next build, but their prose style is unchanged. Decide whether they get the same pass.
4. **New content, not in any ticket:** ch51 adds Rev 2:4 ("left your first love") as a possible thematic link for Matt 24:12; ch52 adds the 13:7 manuscript note. Both are short and sourced; strike them if unwanted.

### Not verified, or verified only partly

- **42 months = 1,260 days**: "many interpreters equate them" is stated from general knowledge, not a cited source.
- **13:7 omission**: from two older commentaries; the Nestle-Aland apparatus was not consulted.
- **The 7,272-year chronology**: citation verified; its data not examined.
- **Radiocarbon and stratigraphy**: reported in the source material, not tested.
- **p.116 "corruption"** reported from a screenshot: not reproducible here. Plausible cause (not confirmed): the PDF embedded Apple Color Emoji and private macOS fallback fonts, which can render as black boxes in other viewers. Part VIII no longer contains emoji.
- **Rev 20:9 / 2 Kings 1:10 Greek comparison**: carried from Part VII's verification, not re-fetched this pass.

### System changes that affect the whole book (not just Part VIII)

- `scripts/design-system-v1.css`: real `h3` style (no more display-size bold); four-tier box sizes (TYPOGRAPHY-001); **label-leak fix** — the first bold phrase of every paragraph inside a box was being printed as an uppercase label; formal `.grade` style for evidence grades, `.conf` for confidence words; quieter `commentary` box.
- `scripts/build-manuscript.py`: (1) word count now counts reader-visible words, not table pipes, `<span>` tags or fences — the old count produced a false failure with no text missing (checked line by line); same 2% tolerance; (2) chapters no longer joined by a rule, which had produced a blank page holding one short line.
- `scripts/test-build-checks.py`: five regression tests for the count fix. All tests pass.
- Dry-run against every Part: the new count fits all 16 Part builds (EN VII, ES VII, ES VIII re-rendered to `_build/` only to confirm; Desktop copies of other Parts untouched).

### Owed to the Spanish edition (not done — English gate first)

ES ch48 still records the σεισμὸς μέγας question as pending (F8) · ES ch50 still credits tree rings, comets and calendar equally (F14) · ES ch51/52 need F1, F2, F4, F5, F7, F9–F12 · Evidence-grade and option restatements · Same narration cleanup. To be logged in `SYNC-LEDGER.md` when the English is approved.

### Housekeeping after approval

- `10-manuscript-architecture.md` still lists the old titles of ch47, ch49, ch50, ch51.
- Formalize in `EDITORIAL-RULES.md`: RESEARCH-PROCESS-002 (reader prose narrates reasoning, not research machinery), the bookkeeping-metaphor ban, the Greek-gloss rule, and the three-question test (*What does Scripture say? What does the evidence establish? What remains uncertain?*).
- Commit, then snapshot (`--snapshot d2-reader1`), then the reviewer reads the frozen PDF.

---

## D. Completion checklist — every tranche item

**Done** unless marked otherwise.

**Tranche 1 (ch47)** — 1 invented "someone asked" removed · 2 file/folder narration removed; table columns now *Question / What the investigation has already established* · 3 "Why test the calendar at all?" added; orientation count and the hypothesis separated · 4 Ethiopian calendar added; Hebrew/Islamic "independent" wording qualified · 5 "Y2K — the millennium bug" · 6 lead-in to the tests; "every recorded eclipse" softened · 7 half-verse failure-mode narration removed; the lesson kept as content · 8 Matthew 24:6–9 quoted in Greek and examined (ch51) · ΔT constraint honoured · Mayan Long Count: **not added** (still awaiting your dependency check)

**Tranche 2** — 1 "PF-01 — a first-century beginning — remains at SUPPORTS"; four statements numbered; glosses · 2 "fourth time it has paid" removed · 3 "nobody decided" → own authorship (ch47, ch49) · 5 "sent it back out blind" rewritten · 6 2 Kings 1:10 (4 Kingdoms in the Septuagint) · 7 "plunder plunder" explained · 8 "What the text does not authorize" block · 9–10 United Nations analogy box, as drafted; no misconduct claims · 11 "until someone looks" resolved with verified data (F8) · 12 sweep for nobody/someone/anyone: clean · 13 ch49 test explanation rewritten; heading replaced · 14 Rev 21:17 box rewritten

**Tranche 3** — 1 aside typography: done centrally (stylesheet) · 2 Greek glossed throughout Part VIII; **rule not yet formalized** · 3 2 Peter 3:9 text vs inference separated; "someone else's" device removed · 4 evidence-grade style: done (`.grade`) · 5 μικρὸν χρόνον / χίλια ἔτη glossed side by side · 6 "anyone was hoping" removed · 7 "fifty-eight stages" negligence rhetoric removed · 8 "conversion is mine" → interpreters' calculation (**partly verified**, see C) · 9 "three chapters away" removed · 10 manuscript deletion → redating · 11 paywalled row: identified and cited (F15) · 12 Phantom Time introduced at first mention

**Tranche 4** — EN ch50 matches ES's redating logic · 1 "What is AH?" added · 2 paywall/"sent out" narration (five places) removed · 3 magnitude kept, orientation added · 4 Fomenko named and distinguished · 5 Gregorian ten/thirteen days clarified · 6 contradicts-box restates the claim · 7 deletion fixed and evidence reweighted (F13, F14) · 8 "no stake" aligned with the careful version · 9 "opened the file / forgot writing" removed; the fact kept · 10 removed · 11 "fifteen stages": reworded, **count dropped** (see C.2) · 12 "nobody proposed" scoped (F16)

**Tranche 5 (ch51)** — titles replaced · invented questioners (L109, 131, 151, 166) removed · rescue-attempt section reframed as the author's reasoning · "debt / unverified cell" removed · recap box and frontmatter rewritten (all six chapters) · horses reductio softened (F6) · earthquake overclaim corrected (F5) · survey scope stated with the verified list (F1) · gap before the earthquake table: **fixed** (table no longer boxed) · Greek glossed · option (a) restated

**Tranche 6** — "the one holding this pen" removed; Matthew 24:6 rewritten as exposition · Matthew 24:12 section rewritten; voice note moved to a parenthesis · thousand-years/little-season passage rewritten with the hedges · p.116: **not reproducible** (see C) · three-question test: recorded, **not yet formalized**

**Tranche 7** — four-part formula restated (and corrected, F1) · ch51 ending boxes rewritten · ch52 opens by naming "saints" · "capacity, not distribution" resolved with the full survey (F10) · oversized type: fixed at source and in the stylesheet · option (c): **corrected, and the proposed fix rejected** (F12) · "both statements" now names 12:17 and 14:12 · bookkeeping ban applied (**not yet formalized**) · 6:11/20:3 re-verified (F3) · placeholder image links ignored
