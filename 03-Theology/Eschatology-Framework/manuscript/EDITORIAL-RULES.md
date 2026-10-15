---
title: "Manuscript — Editorial Rules (living)"
type: reference
category: theology
tags: [manuscript, editorial, reader-facing, person-intro, typography, novice-reader]
created: 2026-09-21
status: active
localization: "★★★ RULES ABOUT WHAT THE READER RECEIVES, as distinct from what the evidence establishes. ❗ The other registers govern correctness: [[SYNC-LEDGER]] tracks cross-edition debt, [[PROVENANCE-LOG]] guards facts about the author, [[STRUCTURAL-DEBT]] holds missing structure and rendering defects, [[ES-REGISTER]] governs Spanish register. THIS ONE GOVERNS COMPREHENSIBILITY — whether a competent reader who is not a specialist can follow what is in front of them. ✅ A book that is correct and unreadable has failed differently, not less."
related: "[[10-manuscript-architecture]], [[PROVENANCE-LOG]], [[STRUCTURAL-DEBT]], [[ES-REGISTER]], [[SYNC-LEDGER]]"
---

# Editorial Rules

> ### **WHAT GOES IN HERE: standing rules about how the manuscript treats its reader.** Not what is true, not how it is verified — **whether it can be followed.**

---

# PERSON-INTRO-001 — First-appearance orientation

> ### **AT THE FIRST MEANINGFUL APPEARANCE of a biblical, historical or extra-biblical figure whose identity cannot reasonably be assumed of the intended reader, provide a concise orientation capsule.**

## What a capsule contains

| ✅ **Include — only what helps the reader weigh the person's relevance** |
|---|
| approximate dates or period |
| role — what they were |
| relationship to the biblical or historical events under discussion |
| the principal relevant work or testimony, where applicable |
| ❗ **whether the person is biblical or extra-biblical** |

| 🛑 **Exclude** |
|---|
| **what conclusion the reader should draw from them.** A capsule orients; it does not argue |
| biography beyond what the argument needs |
| anything that pre-decides the evidentiary weight the chapter is about to assign |

## Worked examples

> **IRENAEUS · c. AD 130–202**
> Early Christian bishop and writer, of the generation after the apostolic era. His *Against Heresies* preserves important early testimony about Christian beliefs and traditions. **An extra-biblical historical witness — not Scripture.**

> **EUSEBIUS OF CAESAREA · c. AD 260–339**
> Early Christian bishop and historian whose *Ecclesiastical History* preserves quotations and reports from earlier Christian writers, including material that no longer survives independently. He wrote centuries after the apostles. **A historical source, not a biblical authority.**

📐 **With those in place, the sentence *"Eusebius, quoting Irenaeus, places the vision under Domitian"* carries meaning for a reader who has not spent years in early-Christian-history debates.** Without them it is a name, quoting a name, about a date — and a perfectly intelligent reader is entitled to ask *who are these people and why should I care what either one says.*

## The rules of use

🛑 **Do not re-introduce the same person.** A second full capsule reads as though the book forgot it had a reader.

❗❗ **TRACK INTRODUCTIONS GLOBALLY, NOT PER CHAPTER.** If Josephus is introduced in Part II, Part VI does not introduce him again. **A short reminder after a very long absence is acceptable; a second first-introduction is not.** This requires a manuscript-wide index of who has been introduced where — see the audit register below.

⚠️ **Do not bloat the running paragraph.** The capsule is a component, set apart from the narrative. The prose then simply uses the name.

✅ **Candidates include** figures such as Josephus, Irenaeus, Eusebius, Antiochus IV, Nero, Domitian — and, where the intended reader would not be expected to place them, some biblical figures too.

---

# TYPOGRAPHY-001 — Visual hierarchy of the components

> ### **NOT EVERY GRAY BOX SHOULD SHOUT AT THE READER WITH THE SAME WEIGHT.** The design has to say what kind of thing each block is before it is read.

| Tier | What belongs to it | Treatment |
|---|---|---|
| **1 — main narrative** | the running first-person argument | body size, full weight |
| **2 — findings and orientation** | `finding` · `whereweare` · `earned` | ❗ **near body size.** These are part of the principal argument and of the reading rhythm, not apparatus |
| **3 — supporting capsules** | person capsules · `historical` · `commentary` | somewhat smaller, tighter |
| **4 — technical apparatus** | `textualnote` · `wordstudy` · `claimtypes` · dense tables | smallest, tightest |

🛑 **Enforce this in the final design pass, as one deliberate change to the stylesheet — not by patching box by box as instances are noticed.** Patching individual blocks is how a design system stops being a system.

⚠️ **Related open presentation debt:** `LAYOUT-001` *(commentary padding and table overflow)*, `LAYOUT-003` *(table rows fragmenting across page breaks)* — both in [[STRUCTURAL-DEBT]]. **The design pass that implements this hierarchy is the natural moment to service both**, since all three touch the same stylesheet.

---

# RESEARCH-PROCESS-002 — Narrate the Scripture, not the research

> ### **Reader-facing prose may narrate genuine changes in reasoning, evidence, interpretation or conviction. It does not narrate internal file state, retrieval mechanics, verification tooling, agent behaviour, audit artifacts, or invented research interactions.**

Adopted 2026-10-10 from the Part VIII reader review (seven tranches; Part VIII EN `d2-reader3`). Its two diagnoses, in the reviewers' words: *the manuscript was narrating the research process instead of the biblical investigation*, and *performative rigor — writing that announces how careful it is instead of letting the evidence show it.*

## The test for every section

1. **What does Scripture say?**
2. **What does the evidence establish?**
3. **What remains uncertain?**

## Not in reader prose

| Category | Examples removed from Part VIII |
|---|---|
| Bookkeeping metaphors | debts, owed, paid, discharged, costs, prices, "properly priced," the bill |
| Self-evaluation | "flattening caught," "the rule paid off," "protects a model from itself," boxes that praise the chapter |
| Research machinery | the archive, the file, a stage "ran," sweeps, retrieval, ladder rungs, paywalls, "sent out to be checked," precheck |
| Invented interlocutors | "someone asked me," "it was put to me," "a reader," "nobody decided," "anyone was hoping" (see PR-003 in [[PROVENANCE-LOG]]) |
| Artificial suspense | withholding a word or concept that can simply be named |

## What stays

- A genuine change of reasoning, in the first person, owning authorship: *"When I reviewed the preceding stages, I found I had never directly tested…"*
- Genuine uncertainty in the evidence. **Obsolete incompleteness in the research does not stay:** if a gap can now be checked, check it and report the result.
- Methodological explanation where it helps the reader weigh an argument (a test fixed before its answer was known).

## Related standing practices from the same review

- **Restate before citing.** Lettered options, earlier findings and named formulas are restated in words wherever they are cited; a reader is not expected to remember a label from three chapters earlier.
- **Chapter endings.** `whereweare` states the findings plainly; `earned` holds *the question this leaves* (its original design purpose), never praise of the chapter.
- **Do not upgrade while rewriting.** Clearer prose must not turn a contextually favoured reading into an established one; re-verify any claim whose strength a rewrite touches.

---

# GLOSS-001 — Original-language terms

> ### **Every Greek or Hebrew term carrying an argument is given a transliteration and a short English gloss at its first use within a discussion — and again after a long gap, or wherever two original-language expressions are directly contrasted.**

Format: <span class="gr">μικρὸν χρόνον</span> (*mikron chronon*, "a little while"). A term is never left untranslated to carry the argument on its own. Adopted 2026-10-10 (Part VIII reader review, tranches 2, 3 and 5).

---

# TYPOGRAPHY-002 — Emphasis and symbols

> ### **No emoji, checkmarks or warning symbols in reader prose. No heading markup used for emphasis. Bold sparingly — at most a key sentence in a section.**

Adopted 2026-10-10 for Part VIII. Beyond tone, emoji embed colour-bitmap and private system fonts that some PDF viewers draw as black boxes. Headings: `#` for the chapter title only, `##` for sections, `###` for genuine subsections. Inside a box, only the first paragraph carries the uppercase label. Evidence grades use `<span class="grade">`, kept visually distinct from confidence words. **Parts I–VII have not yet been brought to this standard** (author decision 2026-10-10: later, using Part VIII as the benchmark).

**Exception, box icons (author ruling 2026-10-15):** each box type has a pastel fill and an emoji before its title (finding 🔎, evidence ⚖️, word study 🔤, textual note 📜, historical 🏛️, person 👤, commentary 💬, claim labels 🏷️, open question ❓, where this leaves us 📍, the question this leaves 🧭, growing chain 🔗). Its purpose is quick identification in the full-color edition, and in black and white together with the border styles. The icons are **generated by `design-system-v1.css`, never typed into the source**. The rule above still holds for prose, and the decor checker still flags any emoji in a chapter file. The orientation page shows them through `<span class="boxicon TYPE">`. The font is Noto Color Emoji (SIL OFL), subset in `scripts/fonts/`. It must not be swapped for Apple Color Emoji, whose license does not cover a sold book; that also answers the black-box concern above. All fills pass WCAG AA (body text ≥ 15:1).

---

# Cross-reference — rules that live elsewhere

| Rule | Home | What it governs |
|---|---|---|
| **SCRIPTURE-COMPLETE-001** | `00-methodology-current.md`, retrieval family | Complete-passage retrieval, and the ban on research machinery appearing in reader-facing prose |
| **PR-READING-001** | [[PROVENANCE-LOG]] | Never convert research chronology into the author's reading history |
| **Spanish register** | [[ES-REGISTER]] | Latin-American international Spanish, enforced at build time |
