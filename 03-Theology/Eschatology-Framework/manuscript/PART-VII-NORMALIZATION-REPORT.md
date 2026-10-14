---
title: "Part VII — Normalization Report (EN)"
type: manuscript-report
created: 2026-10-14
status: en-approved-pending-r1.1-confirmation
related: "[[PART-VI-NORMALIZATION-REPORT]], [[10-manuscript-architecture]], [[EDITORIAL-RULES]]"
---

# Part VII — Normalization Report (English)

## Revision 1.1: review fixes applied (2026-10-14)

All six §E decisions are approved: D1 (all 24 trails stay hidden), the ch46 opening, N7/N8, N12/N14/N19, N20/N21, and lower-case labels. The four review fixes, verified in the rebuilt PDF:
- 197 pages, every gate passing, normalization 0;
- **0 raw `**` left anywhere in the Part.**

| # | Where | Fix |
|---|---|---|
| R1 | ch46 p.179, false prophet | "all three of his appearances share one sign-vocabulary" was wrong. Now: named at 16:13, where **the spirits** perform the signs (16:14); 19:20 ties him to the signs ("*who made the signs before it*", the second beast's description at 13:13–14); 20:10 names him **without** sign-vocabulary. The link to the second beast still stands, on 19:20 ↔ 13:13–14. |
| R2 | ch46 p.180, **γῆ re-audit** | Done from the project's base text (SBLGNT via MorphGNT, ledger S111); details below. |
| R3 | ch46 p.184, raw markdown | `**type**`/`**instance**` nested inside bold → *type* / *instance*. **A second leak of the same kind turned up in the full-Part sweep:** ch46 "the evidence ***does***" inside a bold sentence (p.188), now fixed. Both were already in the frozen `d1-reader3` as well. |
| R4 | ch46 p.173, overclaim | "unavailable to anyone quoting the standard argument…" → "**A one-name calculation cannot establish uniqueness. Testing multiple names shows why 666 functions as a filter rather than an identification by itself.**" |

### R2: the γῆ audit result

**The complete count is 82 occurrences in 67 verses, across 18 of the 22 chapters.** This matches your external concordance at 67 verses. Every number the printed box gave was wrong:

| Printed | Actual (SBLGNT) |
|---|---|
| "35, across all 22 chapters" | **82 occurrences, 67 verses, 18 chapters** (none in ch 2, 4, 15, 22) |
| *those who dwell on the earth*, eight | **10** (11 counting 13:12's *those who dwell in it*) |
| *the kings of the earth*, seven | **8** (1:5, 6:15, 17:2, 17:18, 18:3, 18:9, 19:19, 21:24) |
| earth paired with sea, "five other times" | **11 verses** (5:13, 7:1, 7:2, 7:3, 10:2, 10:5, 10:6, 10:8, 12:12, 14:7, 21:1) |
| scope markers "consistently universal — *all the tribes of the earth*…" | **Contradicted ch42**, which reads Rev 1:7 as *all the tribes of **the land*** (through Zech 12) |

**What the complete sweep supports:**
1. **No occurrence restricts γῆ to a named territory.** This holds on the full data.
2. **The usage is predominantly cosmic:** heaven-earth-sea as the whole creation (10:6, 14:7), *the whole earth* (13:3), *all the earth* (5:6), *the four corners* (7:1, 20:8), *the breadth of the earth* (20:9), *a new earth* (21:1). It also holds that 13:11's own structure pairs earth with sea: the first beast comes from the sea (13:1), the second from the earth.
3. **But the word is not sealed against *land*.** This book already keeps *land* open at 1:7 (ch42) and 18:24 (ch38: "on the earth" or "in the land").

**Conclusion, slightly weakened:** before, it said the territorial reading "runs uphill against **every occurrence** in the book". Now it says the reading "runs against the book's **dominant usage** and against the verse's own sea–earth pairing", and it is still **not neutral**. No grade moved, and the false-prophet verdict ("neither candidate family passes") is unchanged. "Where this leaves us" is updated to match ("the dominant usage of one word across eighty-two occurrences").

**Not changed:** ch46's frontmatter summary still says "35 occurrences". It is not printed, and it says the chapter text governs. The research file `03c-the-land-beast-and-the-false-prophet` is the likely source of the 35, and the closed investigation is not reopened. Both are logged on BIBLE-3c7. **Spanish ch46 must take R1–R4 from the start.**

**Checklist:** the one used on Parts I–VI, with Parts VIII–IX as the benchmark. **No argument rewritten and no grade moved.** The one strength change is the N19 overclaim, which is a correction (§B). Every fix to a cross-reference or a fact is listed in §B.

**Result:** normalization 0 in every category. Before the pass:

| Category | Count |
|---|---|
| decorative marks | 562 |
| grades | 16 |
| labels / process words | 36 |
| gloss gaps | 166 |
| structure | 11 |
| conventions | 28 |

**The build:**
- **196 pages, 34,856 words.** The last snapshot (`d1-reader3`) had 231 pages and 39,700 words. About 5,000 words are now hidden or gone, almost all of them in the hidden verification trails (§A5) and the removed marks.
- 0 mojibake and 0 sections missing.
- The original-language gate passes on 84 pages, all wrapped.
- The table gate passes on 46 table pages: 6 continue with a repeated header, and no rows split.
- **Pages checked visually:** 23, 75, 103, 134, 140, 154, 161, 170, 188, 191, 194, 195.

**How this Part was done:** I read all seven chapters in full myself (no agents). I applied every edit through exact-match asserts, and I checked every cross-reference against the printed chapter it names. Part VII had by far the most drift: 562 marks, many of them standing in for words in tables, and a heavy layer of research scaffolding.

## A. What changed

### A1. Titles, person boxes, chain

| Ch | Before | After |
|---|---|---|
| 40 | How strongly evidence bears — and this is a falsification criterion… | **Paul's transformed living — a falsification criterion, not a difficulty** |
| 41 | How strongly evidence bears | **1 Thessalonians 4 and the first resurrection — correspondence, not identity** |
| 41 | THEODOTION · Greek translator… | **Theodotion · Greek translator…** (BIBLE-3c7) |
| 43 | ANTIOCHUS IV EPIPHANES · reigned… | **Antiochus IV Epiphanes · reigned…** (BIBLE-3c7) |
| 46 | Growing Chain — Checkpoint 5 · *PF-01 stands at SUPPORTS. And the bill for it is about to come due.* | **The growing chain — checkpoint 5** · *PF-01 stands at <span>supports</span>. What it commits me to comes next.* |

Box captions that already described their content were kept. The labels are now «Where this leaves us.» / «The question this leaves.» in all seven chapters.

### A2. Grades and confidence labels (same strength)

- **ch46 scale:** all 16 grade words were in capitals. They are now grade spans:
  - the quoted scale reads "whether the evidence gathered so far <span>contradicts</span>, merely <span>permits</span>, actively <span>supports</span>, or actually <span>requires</span>…";
  - "PERMITS → SUPPORTS" becomes "the evidence no longer merely <span>permits</span> it; it <span>supports</span> it";
  - "PF-01 at <span>supports</span>", matching Part VIII's "PF-01 is carried forward at <span>supports</span>".
- **Confidence and status labels** (HIGH, VERY HIGH, PROBABLE, ESTABLISHED, MODERATE, OPEN, ZERO, VERY STRONG) are now lower case and still bold. Part VIII uses none in capitals. The words themselves are unchanged.
- **ch45:** "thrown in ALIVE" becomes "*alive*".

### A3. Decorative marks

All 562 are gone: ❗ ✅ ★ ⚠️ 🛑 ❌ 📌 📐 ⚖️ ⬇️ ⬆️ ⬅️ ❓ 🏷️ 🔶 ⭐ 🔁 🆕. Where a mark carried meaning in a table, it now has words:
- ch43 Synoptic table: ✅ → "yes", ❌ → "absent" / "—";
- ch43 shortcut line: "❌ abomination = army · ❌ …" → "*abomination = army* · …";
- ch45 "Where the chain stands": a bulleted list, where it had been seven lines run together;
- consecutive mark-led lines, which used to merge into one paragraph, are now separate paragraphs.

### A4. Original language

There were about 100 first-occurrence glosses (*translit*), checked by eye. Hebrew follows the book's existing simple style: *pesha*, *shiqquts*, *et asher-daqaru*, *veyitromem veyitgaddel*, *Neron Qesar*, *rabbim*. The two Greek forms in capitals are *Nerōn Kaisar* and *Teitan*. One existing inline form was converted: "— *kreittonos anastaseōs*," → "(*kreittonos anastaseōs*)".

### A5. Verification diaries hidden (D1), with the results kept printed at the same strength

**24 hidden `VERIFICATION TRAIL` comments, kept verbatim (raw material for Appendix G, *Corrections Made to My Own Work*).** Seven of them are whole sections or boxes. **This is the main decision for you (§E1).**

| Ch | Hidden | What stays printed |
|---|---|---|
| 40 | **Section** "I argued from incomplete text…": the table of passages first held only in part, plus "since verified in full" | The three passages are quoted in full where they are used. The Rev 6:10–11 result moves into the finding at the same strength: *rest yet a little time*, *until… fulfilled*, "conscious, addressed, waiting existence". The section also pointed at Part VI's Revelation 17 numbering note, which is now itself hidden (Part VI D1). |
| 40 | Matt 27 "written while the clause was still only reported"; "now stands at full strength"; "caught by a rule written one stage before it…" | The Matthew 27 quotation; the Hebrews 11:35 artifact, stated plainly |
| 41 | **Section** "A correction arrived for an error I did not have" (an incoming correction checked against "four independent files", next to a three-row table) | Nothing reader-facing is lost: the next section proves the same chronology from the text |
| 41 | **Section** "What was verified": the verification list, "the first stage owed it and the second stage paid", the "9 out of 10" rating | A new note, "Textual note — the Septuagint, and why English agreement proves nothing here". It keeps the LXX definition, the English-translations principle, the Theodotion person box, and the two items still missing. |
| 41 | "within the same twelve hours, an argument put to me…" | The status correction itself ("Restraint is not a verdict") |
| 41 | **Section** "A fabricated parallel, caught at the door" (a false row in an internal comparison table) | Its three Greek facts are printed elsewhere in the chapter (*hēxousin* in Isa 27:13; Deut 30's *synagō*; *opsontai* / *epiblepsontai*, different roots) |
| 42 | The inventory-miscount diary | One sentence: Luke 8:29's compound verb is not counted |
| 42 | **Section** "A closure the archive already held" ("second no-op in three stages", "not consulted this time") | One sentence: *son of destruction* occurs only here and at John 17:12, of Judas; a description, not a title for Satan |
| 42 | "Hebrew… reconstructed from dictionary reference numbers" | "The Hebrew is laid out in the next chapter" |
| 43 | The festival word "supplied from memory and labelled verified"; "table first drawn up without those texts"; the empty 8:13 cell | The festival link stated at its strength (same family, not same word); the checked table |
| 43 | **Section** "The Greek Daniel I could not find" ("three times, across three stages") | A new short section, "Theodotion's Greek Daniel": the recensions are separate texts, and the critical edition prints Theodotion |
| 43 | **Box** "A debt paid before the argument leaned on it" (Matt 24:12) | The word study, quoting the verified Greek |
| 44 | "Two debts were paid…" plus a box re-quoting Rev 6:10–11 and Matt 27:52–53 "now complete" | One line, "The same subtraction test, run against Revelation 20:4–6." Both texts are already quoted in ch40. |
| 44 | "accidental discovery… a genuine gap in a prior audit… Unpaid debts hide more than they cost" | The observation (6:11 and 20:3 share two words, reordered), as an observation |
| 45 | **Box** "A summary contradicted its own table" | Nothing reader-facing lost; the δέω table and its brakes stand |
| 45 | The visible label **RC-01** and "at this point 20:8 was verified and 16:13–14 was not" | Rewritten as "A recapitulation candidate, fenced the moment it appears"; ch46 tests it |
| 46 | Opening "discipline breach" (a name said "twelve paragraphs later", "named in my own notes fourteen sections after", "inside the stage") | The rule, and the *seven mountains* trap that motivated it, stated directly (§E2) |
| 46 | The Irenaeus page "restricted or no longer available… since read, three copies agree"; row 3 "stale, corrected" | The quotation, read in the standard public-domain English, and the corrected row. "English only" is still printed. |
| 46 | **Section** "And I found out I had been repeating myself", including the table of "six consecutive stages ended by deferring" | The rule that matters to the reader: PF-01 is not relitigated without contrary evidence |

### A6. Research-process language

| Ch | Before | After |
|---|---|---|
| 40 | twelve **stages** of walking at my own model | a whole Part spent walking at my own model |
| 40 | heading: Paul raises the **bill** | Paul raises the burden |
| 41 | **owe** (heading) · **owed** ×2 · **discharged** · debt goes to Chapter 43, where it is **due** · **this project** · **this morning** · may decide **the stage** · a claim already in my **archive** | from Chapter 10 · still needed · met · the comparison belongs to Chapter 43 · this book · at the start of this chapter · decide this · a claim this book made in Part II |
| 42 | a later **stage** · carried forward verbatim so they cannot drift · **this project** · one **stage** before the evidence | later · stated exactly · this book · before the evidence |
| 43 | anything I **retrieved** · thirty **stages** later · fifty **stages** · a **ledger** of a motif · a **debt** discharged | anything I have read · many chapters later · this whole investigation · a recurring motif · the second Greek Daniel, read beside the first |
| 44 | **this project** ×5 · narrative **debt** that chapter 20 **pays** · **spending** it as though lexical · rather than **spent** early | this book · a narrative thread that chapter 20 closes · treating · used |
| 45 | every other **stage** · a **project** that only runs lexical tests · this **archive** supports no step · a study is **owed** | every other point · an investigation · this investigation · still needed |
| 46 | **paying a debt** (heading) · sat **unpaid** for three **stages** · what is **owed** · in this **archive** · named **debts** · it is **owed** · already **on file** · **filed** it · I **owe** the reader · every **ledger** · fifty **stages** | reading both Greek Daniels in one edition · (removed) · what needs explaining · computed here · named open questions · still open · already in this book · setting it down · here is · every finding · before this evidence existed |

Kept as ordinary English, as in Parts I–VI: "spent" for time, resurrection "stages" and "two-stage structure", "pay taxes", "an argument put to me", "reported, not verified".

### A7. Structure and layout

- **Eleven `---` + `#` pairs → `##`:** ch42 ×2, ch43 ×3, ch44, ch45, and ch46 ×5. They no longer force page breaks or enter the table of contents.
- **L1:** the two "chain" boxes (ch44, ch46) ran their links together into one paragraph with inline ↓. Hard line breaks now put one link per line (pp.140, 194).

## B. Reference and factual fixes, each checked against the chapter it names

| # | Where | Before | After | Why |
|---|---|---|---|---|
| **N1** | ch40 | *rabbim*, "the word I was tempted by **four Parts ago**" | "…tempted by **in Part V**" | It first appears in ch25 (Part V), not Part III |
| **N2** | ch40 | Finding title "**fourteen** chapters early"; body "**thirteen** chapters before the verse it constrains" | fourteen, both places | Rev 6 → Rev 20 is fourteen; the box contradicted itself |
| **N3** | ch40 | "the thing I have spent **nine** Parts trying not to do" | **six** | ch40 opens Part VII; the same chapter says "six Parts" earlier |
| **N4** | ch40 | "the same discipline as the Revelation 17 numbering problem in Part VI" | (removed with its diary) | The Part VI note is now hidden, so this pointer had no target |
| **N5** | ch41 | Rev 3:3, "I established **two Parts ago**" | "**in Part VI**" | ch30 "a conditional coming, addressed to one city" |
| **N6** | ch41 | "My own **Until-Reversal Caution**, written **four Parts ago**" | "my own **until-reversal caution**, written **two Parts ago**" | Named in ch29 (Part V), lower case (BIBLE-3c7) |
| **N7** | ch41 | "the claim I had been leaning on hardest simply failed… **I had argued**… I had been implying three" | "a claim I would very much like to lean on fails, **exactly as Chapter 10 warned it would**… It is tempting to argue…" | **ch10 already prints that *parousia* "does not appear at Matthew 24:31… brackets this pericope"** |
| **N8** | ch41 | "In my **earlier work** on the gathering, I wrote that Matthew 13:41 *pairs it with the same gathering verb*… **That is false.**" | "In **Chapter 10** I wrote that Matthew 13:41 has *the same formula and the same gathering language*… and flagged there that a later chapter would take it apart. This is that chapter. **The gathering half of it is false.**" | ch10 prints the claim and says "Part VII is where the investigation catches it". The quotation now matches ch10, where the formula half is correct. |
| **N9** | ch41 | "destabilizes a claim already in my **archive**" | "unsettles a claim **this book made in Part II**" | ch08: the son of man "comes **to** the Ancient of Days… presented" |
| **N10** | ch41 | RVR1960 translators split the verbs "**centuries** before it" | "**long** before it" | The 1960 revision is decades, not centuries, before 2026. The older Reina-Valera tradition was not checked for this split. |
| **N11** | ch43 | "I established **two chapters ago** that those two verses share zero vocabulary" | "**last chapter**" | ch42 ("Matthew 24:15 and 2 Thessalonians 2:4 share no vocabulary at all") |
| **N12** | ch44 | "With the **sixth-seal** material…" · "the **sixth** seal's *a little time*" | "the **fifth-seal** arc" · "the **fifth** seal's" | **Factual: Revelation 6:9–11 is the fifth seal.** ch31 (Part VI) has it right |
| **N13** | ch44 | "the exact inversion this project forbade itself **before Part VII began**" | "…this book forbade itself **at the start of this Part**" | That rule is in ch40, which opens Part VII |
| **N14** | ch45 | Synoptics split "the third time in this Part: the cloud prepositions, **the trumpets**, and now this" | "…**the sign of the abomination**, the cloud prepositions, and now this" | The trumpet comparison (ch44) is Matthew against Paul, not the Synoptics. The Synoptic splits are the sign (ch43: Luke's armies) and the clouds (ch43). |
| **N15** | ch45 | examples of refused reasoning: "the Greek word that was not there, the half-verified festival link, the mouth-weapon promotion, **the millennium that turned out to be a phantom**" | "the verb-parallel that was not there, the physical-sanctuary reading, the mouth-weapon promotion" | Two examples pointed at now-hidden diaries. The "phantom" millennium is not printed before Part VIII (ch47). All three are now printed findings (ch41, ch42, ch45). |
| **N16** | ch46 | edition mismatch declared "**two chapters ago**" | "**three**" | ch43 |
| **N17** | ch46 | recapitulation candidate "fenced **two chapters ago**" | "**last chapter**" | ch45 |
| **N18** | ch46 | two start markers "established **two chapters ago**" | "**last chapter**" | ch45 |
| **N19** | ch46 | "Revelation names the false prophet three chapters earlier **than anyone had noticed**" | "…three chapters **before the destruction scene** — at the sixth bowl" | **Overclaim.** That Rev 16:13 names the false prophet is not a new discovery; the datum stays, the claim of novelty goes |
| **N20** | ch46 | "So I searched **my own files**, and the answer was sitting there, dated weeks before…" | "The answer was already written. **Chapter 2** set out the scale this whole book uses, before any of this evidence existed — and **my notes** from those early weeks applied it to the hypothesis itself" | ch02 introduces the four grade words. No printed chapter grades the core hypothesis before ch46, so the "permits that day" provenance stays as **notes**, the pattern approved for ch35 in Part VI |
| **N21** | ch46 | PF-01 does not license "anything from the **quarantined branch**" | "the **alternative-chronology proposal** — that conventional chronology itself is wrong — which stays quarantined" | An internal label. ch47 (closed) says "the calendar proposal was **quarantined in Part VII**", and this is the only Part VII text it can point to. See §D. |
| **N22** | ch44 | "this project refused exactly this shape **once before**" | "this book refused… **in Chapter 41**" | Pointer made specific (ch41 refuses δεῖ / ἄχρι) |

## C. Checked and left as it is

- **Cross-references checked:**
  - ch40: "the Greek of John 6 is worked through in the next chapter" (ch41 ✓); Rev 12 birth → enthronement compression (ch35 ✓); Part VI aligning death with 20:14 (ch39 ✓).
  - ch41: "a control set in Part VI", prolepsis (ch32 ✓).
  - ch42: "one taken… recorded long ago" (ch28 sidebar ✓); the closure "I had opened one chapter earlier" (ch41 ✓).
  - ch43: "last mention two chapters ago" (ch41 ✓).
  - ch46: gematria "met in Part VI" (ch36 ✓); "*was seen*, the contested point recorded in Part VI" (ch36 ✓); Tacitus "since Part VI" (ch36 ✓).
  - ch41: Matthew 24:14 "the verse that started this entire investigation" (ch01 ✓).
- **ch40's "A verb I had asserted for months turned out not to exist":** kept. ch10 itself says the error is caught in Part VII.
- **ch41's "Restraint is not a verdict":** kept ("My files said… My summary said"). It is the narrator's own summary, not a pointer to printed text. Only the "twelve hours" paragraph is hidden.
- **ch46 Irenaeus:** "read in English only… the Greek not checked" kept as written (the Part VII closure record).
- **Checker:**
  - **`source_words` now ignores hidden comments.** A hidden trail quoting `<span>` markup was being counted as source, a false failure of the word-recovery band with no text missing (34,856 recovered against 35,601; the comment-free source is 34,684). Fixed, with a regression test. All tests pass.
  - **Two lines flagged as stage-talk are about resurrection staging.** They were reworded within the same meaning rather than widening the regex: ch40 "Paul compresses several stages" → "a staged sequence"; ch44 "— a stage, relative to *the rest*" → "— its first stage, relative to *the rest*".

## D. Logged for the full-book audit (BIBLE-3c7)

- **ch47 (Part VIII, closed)** says "the calendar proposal was quarantined in Part VII, **on two structural grounds**". Part VII prints neither ground; ch46 now at least names the proposal (N21). The two grounds have to be printed somewhere, or ch47 has to say where they are.
- **Spanish Part VII:**
  - ch41 «la cautela del *hasta*», two Parts;
  - person boxes;
  - the same N-fixes, walked row by row.

## E. Decisions for you

1. **D1 scope (§A5):** 24 hidden trails, seven of them whole sections or boxes. Every result is printed at its old strength, and the hidden text is kept verbatim for Appendix G. Approve the set, or name any section that should stay printed? The likeliest candidates to keep are ch41's "fabricated parallel" and ch46's "discipline breach", because both show a correction against my own interest. If kept, they would need rewriting so they no longer narrate tables, notes and stages.
2. **ch46 opening:** the breach story is replaced by stating the rule and the *seven mountains* trap directly. OK?
3. **N7 and N8:** ch41 now points back to Chapter 10 for *parousia* and for Matthew 13:41, rather than presenting both as fresh failures. OK?
4. **Factual fixes N12 (fifth seal), N14 (Synoptic splits) and N19 (false-prophet overclaim).** OK?
5. **N20 and N21:** ch46 "Chapter 2 + my notes" for the scale's provenance, and the quarantined proposal named plainly. OK?
6. **Lower-case confidence labels (§A2)**, matching Part VIII. OK?

## F. Spanish Part VII

This waits for English approval. Every row above will be walked against the Spanish files before the Spanish report is written (the standing rule).
