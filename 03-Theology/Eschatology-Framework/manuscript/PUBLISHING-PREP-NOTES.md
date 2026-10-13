---
title: "Publishing Prep — Notes and Precedent"
type: reference
category: theology
tags: [manuscript, publishing-prep, front-matter, legal, imprint, cover, idea-vault-precedent]
created: 2026-10-13
status: active
localization: "PRECEDENT, NOT ARCHITECTURE. Architecture §1/§11 (ruling ㉓) controls front and back matter. This note records what an earlier book (The Idea Vault, 2026) did, and the decisions taken on what carries over. Nothing here is final legal text. Legal wording, translation permissions, ISBN/LOC and the imprint are decided in the publishing-prep phase, not before."
related: "[[10-manuscript-architecture]], [[02j-translation-architecture-the-spanish-edition-and-the-greek]], [[PART-I-NORMALIZATION-REPORT]]"
---

# Publishing prep — notes and precedent

**Status of this note:** precedent, not controlling architecture. `10-manuscript-architecture.md` §1 and §11 (ruling ㉓) control the front and back matter. This note is a reference for the publishing-prep phase. That phase comes after the Parts I–VII normalization and the full-book consistency audit.

## 1. Source of the precedent

*The Idea Vault* (2026), built at `/Users/MARS/Desktop/7-MARS/IDEA-VAULT-PDF/`. That project used the same toolchain as this book: Pandoc, WeasyPrint and pypdf. It was reviewed 2026-10-13 from its CLAUDE.md, MODS.md, SESSION-LOG.md, book.toml, style.css and the final v1.4 PDF. Its `.env` and settings files were not opened.

What it did:

| Element | What The Idea Vault did |
|---|---|
| Order | cover → dedication → copyright/legal (2 pp.) → author's note → contents → "A Note on What Came Before" → chapters → conclusion → glossary |
| Copyright page | title; "© 2026 Marcelo Mario Berta. All rights reserved."; publisher line; no-reproduction clause with a brief-quotation exception; trademark disclaimer; as-is warranty disclaimer; "First published: 2026 / Version 1.4"; permissions contact |
| Running footer | `@page @bottom-center`: author © · site · version, plus title © · all rights reserved; page number at `@bottom-right` |
| Version rule | version in footer = copyright page = filename, always updated together |
| Cover | full-bleed illustrated PNG → cover PDF (Pillow) → merged before content (pypdf). Three steps, never collapsed into one. |
| Change tracking | MODS.md modification log + SESSION-LOG.md |

## 2. Decisions (author + ChatGPT, 2026-10-13)

| # | Decision |
|---|---|
| P1 | **Copyright page:** use the Idea Vault's *structure* as a template, not its text. It slots into architecture §1 ii. The tech-trademark list does not apply; this book needs Bible-translation notices instead (P6). |
| P2 | **Versioned footer for review/draft PDFs only.** The snapshot milestone (e.g. `d2-normalized`) can print on review drafts so a reviewer always knows which version they hold. **Final reader/print editions carry edition and version on the copyright page only, not on every page.** |
| P3 | **Keep the separate cover step + merge.** Add it to `build-manuscript.py` with the cover design work (bead BIBLE-493). |
| P4 | **No MODS log.** The Part reports, SYNC-LEDGER, beads and immutable snapshots already do that job. |
| P5 | **"A Note on What Came Before": UNRESOLVED, optional, decided at assembly.** The book began with the question "which author, which teacher?", so a note on influences could blur intellectual influences actually used with authors met only later. Possible homes: the Author's Note, acknowledgments, or a short "Sources and influences" note. Name only what the manuscript and the source ledger (Appendix F) support. |
| P6 | **Bible-translation permissions and notices: a dedicated publishing-prep check.** The translations in use are ESV and CJB (English), RVR1960 and RVA-2015 (Spanish), and SBLGNT (Greek). See 02j-translation-architecture, which also requires the book to *name its base translation*. Each publisher sets quotation limits and exact notice wording. **Verify against each publisher's current terms; never copy boilerplate from memory.** |
| P7 | **Imprint.** "Bright Forest Publications" is a *proposed* imprint name only. **Never print "Bright Forest Publications LLC" unless that entity legally exists.** For comparison, the Idea Vault printed "Published by Kollabs" while its config said "Kollabs LLC". |
| P8 | **Deferred to publishing prep:** all legal wording, translation permissions, ISBN, Library of Congress (LCCN/CIP), and imprint finalization. Verify current processes at that time rather than relying on stale guidance. |

## 3. Already covered elsewhere

- Dedication: architecture §1 iii (the author writes it).
- Glossary / divine names: only if Appendix D (Word Study Index) does not already do that job (ruling ㉓).
- Bibliography: only if Appendix F (Source Ledger) is not enough for readers (ruling ㉓).
- Cover, chapter openers, Part title pages, running heads, trim: bead BIBLE-493.
