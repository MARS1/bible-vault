---
title: "Book One — timeline and effort estimate"
type: reference
category: theology
tags: [manuscript, timeline, effort, book-one]
created: 2026-10-20
status: active
localization: "Recorded at the author's request, 2026-10-20. The measured figures come from git history and file counts. The solo-author estimate is a rule-of-thumb calculation from general publishing working rates, not a measurement and not a sourced figure; read it as an order of magnitude."
---

# Book One — timeline and effort estimate

*The Promise and the Little Season* / *La promesa y el poco de tiempo*, digital editions in English and Spanish, distributed free.

## What was measured

| Measure | Value | Where it comes from |
|---|---|---|
| Vault start | 2026-08-06 | earliest `created:` date on the research files (`00-index.md`, `01-convictions.md`, `02-historical-observations.md`) |
| Assembled | 2026-10-20 | last commit; both editions built by `scripts/build-book.py` |
| **Total days** | **75 days elapsed** in the vault (76 counting both ends); about 89 from the earlier research start | calendar span, start to assembly |
| **Active days** | **48** | distinct dates with at least one git commit to `03-Theology/Eschatology-Framework/` |
| Commits | 250 | `git log` on the same folder |
| Research archive | 109 files, ~660,000 words | the stage, audit and index files in `Eschatology-Framework/` |
| English manuscript | ~187,000 words; 54 chapters + coda; Appendices A–G; ~1,007 pages | `manuscript/en/` plus the English matter |
| Spanish manuscript | ~203,000 words; same structure; ~1,050 pages | `manuscript/es/` plus the Spanish matter |

**Total days against active days.** Total days is the calendar from start to finish. Active days counts only the dates on which something was saved to git, so it is a floor and does not measure hours: a day spent only reading, thinking or reviewing without a commit does not appear, and a short day counts the same as a long one.

**Earlier start.** The research began before the vault existed. ChatGPT, asked by the author on 2026-10-20, places the first substantial investigation at **2026-07-23 or earlier**, which makes the whole project about **three months** (2026-07-23 → 2026-10-20, 89 days elapsed). The vault dates above begin when the research was first filed.

## Actual hours spent (AI-assisted)

Two tools, two phases, kept separate so nothing is counted twice.

| Phase | Hours | How it was obtained | Strength |
|---|---|---|---|
| Research with ChatGPT (Revelation, Daniel, Ezekiel, Matthew, Thessalonians, chronology, New Jerusalem, Gog and Magog, review of arguments) | **100–150 (working figure 125)** | ChatGPT's own estimate, 2026-10-20; it states it has no complete time log | estimate |
| Manuscript with Claude Code, 2026-09-27 → 2026-10-20 | **24.4** (18.8 with the author present and sending messages) | **measured** from the session log's timestamps: time between consecutive entries counted only when under 30 minutes apart, so breaks and overnight pauses are excluded | measured |
| Manuscript with Claude Code, 2026-08-07 → 2026-09-25 | **50–100** | no session logs survive for this period (Claude Code clears old logs); 36 git-active days × the measured rate of about 2 hours per active day, widened for uncertainty | estimate |
| **Total, author's AI-assisted work** | **about 200–250 hours** | | mixed |

Roughly 5–6 forty-hour weeks of actual work, spread over three months. Not counted anywhere: time the author spent reading drafts and PDFs away from either tool. Some overlap is possible between the ChatGPT research and the earliest vault work, which filed that research.

## Solo-author estimate: how it was worked out

The question: how long would one person need for the same output, working without AI tools? Each part of the work was estimated separately, using common working rates applied to this book's actual word counts. A full-time working year is taken as about 250 working days.

| Part of the work | Basis (rule-of-thumb rate) | Working days | Full-time |
|---|---|---|---|
| Research: 66 stages, original-language checks (Greek, Hebrew, Aramaic, two Greek versions of Daniel), ~120 sources logged including failed retrievals | ~660,000 words of research notes at 1,500–2,000 words a day, slower than ordinary writing because of the look-ups and verification | 330–440 | 1.3–1.8 years |
| Writing and revising the English | ~187,000 finished words at 750–1,000 words a day, a common pace for researched nonfiction including revision | 190–250 | 0.75–1 year |
| Spanish sibling edition | ~203,000 words at about 2,000 words a day for professional translation, plus about half that time again for adaptation and checking against the RVR1960 | ~150 | ~0.6 year |
| Appendices, indexes, counts, assembly, proofing | judgment, from the size of Appendices A–G and two ~1,000-page builds | 40–60 | 2–3 months |
| **Total** | | **~710–900** | **about 3–4 years full-time** |

Part-time at roughly half pace: **about 5–7 years**.

**Limits of this estimate:**

- The working rates are general publishing rules of thumb, not figures checked against a source. They vary widely from person to person.
- It assumes a person who already reads Greek and Hebrew and knows the tools. Someone learning those would take longer.
- It counts output, not insight. The direction of the investigation, the theology, and the decisive corrections recorded in Appendix G were the author's. Much of the AI contribution was checking, counting, cross-referencing and assembly.
- For comparison, scholarly books of similar depth are commonly said to take 3–5 years, and a typical published nonfiction book runs 70,000–100,000 words. Book One is about twice that length per edition, in two editions.

Related: beads memory `book-one-timeline-2026-10-20`, `PUBLISHING-PREP-NOTES.md`, bead BIBLE-493.
