---
title: Book One — full-book audit (Parts I–IX, EN + ES)
status: CLOSED 2026-10-14 — applied, verified, committed
date: 2026-10-14
---

# Book One — full-book audit (Parts I–IX, EN + ES)

**Scope.** Every chapter of both editions, read-only. The normalization of all nine Parts is complete and frozen; this audit looks *across* Parts for what a per-Part pass cannot see. **Nothing has been edited.** Every row below is a proposal. Fixes to frozen Parts will be rebuilt under new snapshot names (`…-audit1`), since snapshots are immutable.

**Evidence rule.** Every row was checked against the chapter files by me, not only by a helper script or agent. Where a row rests on an agent's report I say so.

**Decisions for the reviewer**

1. Approve the mechanical batch: A4, A5, A6, §B (six Part VIII process-talk sites), C1–C4, D1, D2, D3, and the checker extension in §E.
2. **A8 — ch39 "already there" (Revelation 20:10).** A content correction in Part VI (EN+ES). The proposed wording leaves the finding and its grade untouched. Approve, amend or reject.
3. A3 ch01 origin line and ch21's missing CJB table: confirm "keep".

Parts touched if all approved: II (ES ch07), III (ch13), VI (ch39), VII (ch41, ch45, ch46 + frontmatter), VIII (ch47, ch49, ch51), plus research file 03c (erratum line) and the build checker.

---

## A. Items carried over from the Part VII close (BIBLE-3c7)

| # | Item | Finding | Proposal |
|---|---|---|---|
| A1 | Part VIII process talk | **Six sites per edition, not three.** The checker caught two (EN ch47:33, ch49:5); it misses the rest because its pattern needs a number, and Spanish «etapa» is excluded by design. See §B. | Fix all six in both editions (§B). Extend the checker (§E). |
| A2 | ES ch06 «Parte VII» → «Parte IV» | **Verified fixed.** es/ch06 reads «la Parte IV de este libro le dedica bastante espacio a la diferencia». | None. |
| A3 | ch01 "That is the true first sentence of this project" (EN+ES) | Checker label hit. This is the author's origin story in narrated voice ("Somebody asked me to show my work, and I discovered I could not"), not process mechanics. | **Keep.** Whitelist in the checker. |
| A4 | ES ch07:136 «la pequeña temporada» | Real term drift. Canonical ES term is «el poco de tiempo» (used everywhere else). | «…la pregunta del milenio y del poco de tiempo.» |
| A5 | ch47 "quarantined in Part VII, on two structural grounds" | Part VII prints only ch46 "…the alternative-chronology proposal … which stays quarantined" — no grounds. The grounds are actually given **in ch47's own calendar section**: Revelation may not be evidence for the chronology being tested, and the usual defence seals itself. The sentence also contradicts its neighbour ("I set (d) aside earlier in this chapter"). | EN: "The calendar proposal was already marked as quarantined at the close of Part VII, and earlier in this chapter I gave the two structural reasons — Revelation cannot be its own evidence, and the usual defence seals itself — before I knew how much pressure…" ES mirror. |
| A6 | "35" γῆ count outside the printed text | ch46 frontmatter summaries (EN+ES, not printed) and research file `03c-the-land-beast-and-the-false-prophet.md` (6 places) still say 35. | Frontmatter: update to 82 / 67 verses / 18 chapters. **03c is the historical research log** — do not rewrite; add one dated erratum line at the top pointing to the Part VII γῆ audit. |
| A7 | BIBLE-ki6 exhaustive counts | See §C (agent lane, re-verified). | — |
| A8 | BIBLE-elf, Revelation 20:10 | Gaps 2 and 3 closed 2026-09-28. **Gap 1 still open, and it is an English content error, not only a Spanish gap:** en/ch39 says of 20:10 "They are **already there**. From chapter 19." stated as fact; es/ch39 «Ya **están allí**. Desde el capítulo 19.» The Greek clause has no finite verb; ch46 and ch51 already treat "already" as inference from arrangement. | EN ch39: "They are there — the clause has no verb, so 'already' is my inference from the order, but chapter 19 put them there first." ES mirror, plus the RVR1960 «estaban» note pointer (SPANISH-SPECIFIC). **Author decision required** (grade untouched: the sequence finding stands on 19:20 → 20:10 order, not on a verb). |

## B. Process talk in Part VIII (both editions)

| Site | EN (printed) | ES (printed) | Proposal (EN; ES mirrors) |
|---|---|---|---|
| ch47:27 / es:17 | "I reviewed what the preceding stages had already established" | «revisé lo que las etapas anteriores ya habían establecido» | "what the preceding Parts had already established" |
| ch47:33 / es:33 | "across the preceding fifty-eight stages" | «las cincuenta y ocho etapas anteriores» | "across the seven Parts before this one" |
| ch47:272 / es:274 | "more pressure on the model than any earlier stage had" | «más presión que cualquier etapa anterior» | "than any earlier question had" |
| ch49:5 / es:5 | "across the preceding fifty-eight stages" | «a lo largo de las cincuenta y ocho etapas anteriores» | "across the seven Parts before Part VIII" |
| ch51:82 / es:88 | "An earlier stage of this investigation examined which of these belong together" | «Una etapa anterior de esta investigación examinó…» | "Before writing this chapter I examined which of these belong together" (narrated reasoning; the result table follows in print) |
| ch51:108 / es:104 | "the earlier stage settled its own tie" | «la etapa anterior resolvió su propio empate» | "that examination settled its own tie" |

## C. Exhaustive counts (BIBLE-ki6)

Every printed count line in EN was listed and each NT claim re-run against SBLGNT (MorphGNT, all 27 books, in the scratchpad). OT/LXX counts (e.g. Ezekiel's purpose formula ×4, Daniel's abomination ×3) are **not checked** against a base text here. ES carries the same numbers as EN at every site checked.

**Wrong or mis-scoped — fix in both editions:**

| # | Site | Printed | SBLGNT | Proposal |
|---|---|---|---|---|
| C1 | ch47 (two lines: the χίλια ἔτη bullet and "A characterization") | "Revelation 20:2, 4, 6, 7 — *chilia etē* … four times in six verses"; "just said 'a thousand years' four times in six verses" | **Six times in six verses, 20:2–7** (2, 3, 4, 5, 6, 7; with the article at 3, 5, 7). ch49 already prints "six times in six verses" — the two chapters contradict each other. | "**Revelation 20:2–7** — … six times in six verses"; "…said 'a thousand years' six times in six verses." No conclusion depends on four vs six. |
| C2 | ch45 "The nations are not a fixed category" | "Thirteen occurrences of *the nations*" | Plural with article: **fifteen** (2:26, 11:2, 11:18, 12:5, 14:8, 15:4, 16:19, 18:3, 18:23, 19:15, 20:3, 20:8, 21:24, 21:26, 22:2); ἔθνος overall 22. No reading of the scope yields 13. | "Fifteen occurrences…" — the two-directions conclusion is unchanged (2:26, 12:5, 19:15 are rule/strike texts and fit the existing negative/positive lists). |
| C3 | ch41 John's "last day" | "All six occurrences checked in the Greek." | The phrase occurs **seven** times; 7:37 ("the last day, the great day of the feast") is silently omitted. Six is right for the eschatological uses. | "All six eschatological occurrences checked in the Greek (7:37, the last day of the feast, is set aside). All singular." |
| C4 | ch46 "The mountains" | "Every occurrence swept — seven of them." | ὄρος occurs **eight** times; the eighth is 17:9 itself, the verse under study. The description of the seven is exact. | "Every **other** occurrence swept — seven of them." |

**Confirmed (MATCH):** ἵππος 16 (ch51) · πόλεμος 9 (ch52) · πλανάω 8 (ch45) · γῆ 82 / 67 / 18 (ch46) · χίλια ἔτη 6, article ×3 (ch49) · 42 months ×2, 1,260 days ×2, time-times-half ×1 (ch49) · ἐδόθη + infinitive in Rev 13 ×4 (ch36 "allowed four times"; ἐδόθη overall is 6, the other two are "a mouth was given" and "authority … was given" without an infinitive) · σεισμὸς μέγας three times elsewhere, 6:12 / 11:13 / 16:18 (ch48) · παρουσία ×4 in Matt 24 · γενεά ×13 in Matthew · συντέλεια τοῦ αἰῶνος ×5 in Matthew, ×3 in ch. 13 · περὶ δέ ×4 in Matthew · ἐπισυνάγω + ἐπισυναγωγή = 9 verses (ch41 "list is complete") · ἁρπάζω 14 · συναρπάζω 4 · ἀήρ 7 · ἀπάντησις 3 · ἐγκεντρίζω 6 (Rom 11 only) · ναός in Paul 6 verses (8 occurrences; the text counts verses consistently) · Yeshua says "the last day" 5 times.

*(A helper agent ran this lane first and reported only five claims, one of them C4 as a plain mismatch. I re-ran every count above myself; C1–C3 are mine.)*

## D. Cross-references and EN/ES parity

**Relative references.** All 35 EN "N chapters ago / from now" references were resolved to their target and checked there (ES uses 49 because it also phrases Bible-chapter distances that way; each extra one was read).

| # | Site | Problem | Proposal |
|---|---|---|---|
| D1 | ch39 "Spiral Progression — promoted" (EN+ES) | "a model I promoted **three chapters after inventing it**" — in print the spiral is introduced *and* promoted inside ch39. "Three" is the research-stage gap (19 → 22, visible in the hidden trail). | "a model I promoted **in the same chapter that introduced it** deserves more suspicion, not less." (The point gets stronger, not weaker.) |
| D2 | ch13 → ch15 | "worth remembering two chapters from now, when the blood of the covenant at **Exodus 24:8** and Matthew 26:28 arrive" — ch15 treats Matthew 26:28 but never Exodus 24:8. | Minimal: ch13 "…when the blood of the covenant at Matthew 26:28 arrives." (Alternative: add Exodus 24:8 to ch15's "blood of the covenant" sentence — more text in a frozen chapter.) |
| A5 | ch47 | See §A. | — |

All other relative references land on the right chapter with the claimed content (checked by reading or keyword at the target), including the Bible-chapter ones (Acts 10, Matthew 23, Revelation 1 → 6, 6 → 8, 17 → 18, 18 → 20). Checkpoint numbering is monotonic in both editions.

**EN/ES parity.** The five structural flags were each opened:

| Chapter | Difference | Verdict |
|---|---|---|
| ch21 | ES lacks the ESV/CJB table for Romans 10:18 | **Recorded decision** (Part IV report: "ES has no CJB table — its ch21 note is about RVR1960 instead"). Keep. |
| ch23, ch25, ch52 | ES has extra Greek spans/rows | ES-specific RVR1960 textual notes. Keep. |
| ch51 | ES has 3 extra textual notes | ES-specific. Keep. **But:** EN quotes Revelation 16:18 in Greek (<span class="gr">οἷος οὐκ ἐγένετο…</span>) with an English rendering; ES gives only the RVR1960 Spanish. |
| D3 | ch51 ES | Same class as the Matthew 27:52 Greek restored in ES Part VII. | Restore the Greek line above the RVR1960 quotation in ES. |

ES ch41 names the "progresión en espiral" where EN says "visions that return to the same ground" — same referent, wording only.

## E. Dimensions checked and passing

| Dimension | Result |
|---|---|
| PF-01 / PF-02 grade consistency (31 lines each edition) | **Pass.** PF-01 is `supports` in every chapter that grades it (ch46, 47, 49, 50, 53, 54), never higher; ES `apoya` at the same sites. ch53's "Strong reconstruction" is the confidence column and matches ch54's "strong interpretive reconstruction … <span class="grade">supports</span>". PF-02 is never graded, consistently. |
| Terminology gate | Pass except A4. |
| "in my notes" (ch03, ch35, ch46) | Narrated provenance; ch35 wording is the approved Part VI fix R2. Keep. |
| Chapters present | All chapters present in both editions. |

**Checker change proposed:** STAGE_TALK to also match "(earlier|preceding|previous) stage(s)" and "stage of this investigation", and an ES list («etapas? anteriores?», «etapa de esta investigación», «cincuenta y ocho etapas») limited to those investigation phrases so resurrection «etapas» are untouched; whitelist ch01's origin line. Plus a test for each.

---

## F. Applied and verified (2026-10-14)

**Ruling:** batch approved with two refinements: the A8 wording, and the ch51 sites rewritten as description of the printed comparison rather than new research-diary narration. Both refinements were applied verbatim.

### F1. What changed

| Row | EN | ES |
|---|---|---|
| A4 | — | ch07 «del milenio y del poco de tiempo» |
| A5 | ch47 "The calendar proposal was already marked as quarantined at the close of Part VII; the two structural grounds are the ones given above — Revelation may not be evidence for the chronology being tested, and the usual defence seals itself — and both were in place before I knew…" | mirror, using ch47's own phrasing («no puede usarse como evidencia de la cronología que se pone a prueba», «se sella sola») |
| A6 | ch46 frontmatter → 82 / 67 / 18, "none names a country" (not printed) | same |
| A6 | research file `03c-…` keeps its text; dated erratum added under the title, pointing to ch46 and the Part VII report | — |
| A8 | ch39 "The narrative has them there — the clause itself has no finite verb, so "already" is an inference from the sequence: Revelation 19:20 places the beast and false prophet in the lake before 20:10." (reviewer wording) | mirror, carrying the RVR1960 note in place: «(el «estaban» de la RVR1960 lo suple la traducción)» |
| A8, consequential | ch39 finding: "That is not an inference from vision order; the verse says where they already are." contradicted the approved sentence → "That order is the book's own narrative, not a guess from where the visions happen to sit: 19:20 throws the beast and false prophet into the lake, and 20:10 sends the devil into the same lake." Finding title and grade unchanged. | mirror |
| A8, consequential | — | ch46 «mientras 20:10 tiene a dos de los tres ya en el lago» → «mientras para 20:10 dos de los tres han sido arrojados al lago en 19:20» (EN already said "have been thrown into the lake at 19:20"; ES had lagged) |
| §B | ch47 ×3 ("preceding Parts", "seven Parts before this one", "any earlier question"), ch49 ("seven Parts before Part VIII"), ch51 ("The comparison below examines…, and its result is a genuine split"; "that comparison resolved its own tie") | mirror at all six sites |
| C1 | ch47 "Revelation 20:2–7 … six times in six verses" ×2 | mirror |
| C2 | ch45 "Fifteen occurrences" | «Quince apariciones» |
| C3 | ch41 "All six eschatological occurrences … (7:37, the last day of the feast, is set aside)" | mirror |
| C4 | ch46 "Every other occurrence swept — seven of them." | «Barridas todas las demás apariciones — siete.» |
| D1 | ch39 "promoted in the same chapter that introduced it" | mirror |
| D2 | ch13 "…when the blood of the covenant at Matthew 26:28 arrives." | mirror |
| D3 | — | ch51 Revelation 16:18 Greek restored above the RVR1960 quotation |
| Checker | `STAGE_PROCESS` (EN "earlier/preceding/previous stage(s)", "stage of this investigation"; ES «etapa(s) anterior(es)/previa(s)», «etapa de esta investigación», «cincuenta y N etapas»), and a ch01 origin-line allowance for `PROJECT_TALK` | 10 new tests |

The two A8 consequential edits were not in the approved list. Without them, the ch39 finding would contradict the approved sentence two lines above it, and ES ch46 would keep the old claim. They are flagged here for the reviewer.

### F2. Verification

| Check | Result |
|---|---|
| Checker tests (`scripts/test-build-checks.py`) | 88 pass, 0 fail. The new tests failed before the change and pass after; the first run also caught an ES regex bug (`anteriores?` missed singular «anterior»), now fixed |
| Book-wide checker scan before edits | found exactly the 6 + 6 approved §B sites and nothing else new |
| Builds: EN III, VI, VII, VIII · ES II, III, VI, VII, VIII | all exit 0; terminology, register, original-language, table-layout gates OK; 0 mojibake; 0 sections missing |
| Normalization (report-only) | 0 everywhere except EN ch47:164 `SOURCE-LANGUAGE` (see F3) |
| Changed rows in rendered PDF text | 31 / 31: new wording present and old wording absent, in both editions |
| Visual | ES Part VIII p. 85: the 16:18 Greek renders in the blockquote under the earthquake table |
| Snapshots | `d2-normalized-audit1` for all nine Part/edition builds above (immutable; earlier snapshots untouched) |
| Desktop reader copies | untouched; only the working `part-NN-xx.pdf` files were rebuilt |

### F3. Closing housekeeping (approved with the commit)

- **EN ch47:** the `SOURCE-LANGUAGE` badge no longer prints after "A genuine variant in Revelation 5:10"; it is kept as a hidden comment, exactly as ES ch47 already has it. A rebuild confirmed the printed text is identical to the audit2 snapshot. EN Part VIII was rebuilt with 0 labels, all gates OK, title still rendered (small caps), badge absent → snapshot `d2-normalized-audit2`.
- **ch13 frontmatter `reference:`** (EN + ES): Exodus 24:8 removed. The field is not printed (24:8 appears 0 times in the Part III audit1 PDFs), so no Part III rebuild was needed.
- The two consequential A8 edits (F1) were approved by the reviewer.

**Book One Parts I–IX: normalization and full-book audit closed in both editions.** Next phase: front/back-matter assembly.
