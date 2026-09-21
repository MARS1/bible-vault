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

# Cross-reference — rules that live elsewhere

| Rule | Home | What it governs |
|---|---|---|
| **SCRIPTURE-COMPLETE-001** | `00-methodology-current.md`, retrieval family | Complete-passage retrieval, and the ban on research machinery appearing in reader-facing prose |
| **PR-READING-001** | [[PROVENANCE-LOG]] | Never convert research chronology into the author's reading history |
| **Spanish register** | [[ES-REGISTER]] | Latin-American international Spanish, enforced at build time |
