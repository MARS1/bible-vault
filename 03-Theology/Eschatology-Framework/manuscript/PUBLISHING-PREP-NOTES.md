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
| Copyright page | title; "© 2026 Marcelo Mario Berta Silva. All rights reserved."; publisher line; no-reproduction clause with a brief-quotation exception; trademark disclaimer; as-is warranty disclaimer; "First published: 2026 / Version 1.4"; permissions contact |
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
| P6 | **Bible-translation permissions and notices: a dedicated publishing-prep check.** The translations in use are ESV and CJB (English), RVR1960 and RVA-2015 (Spanish), and SBLGNT (Greek). **Also credit (added 2026-10-15, author request that every biblical source used be acknowledged):** the Hebrew text *Miqra according to the Masorah* via Sefaria (Source Ledger S115), the Septuagint (Swete's edition, S25), and MorphGNT (S111). Each has its own license or attribution terms; check them at this step. See 02j-translation-architecture, which also requires the book to *name its base translation*. Each publisher sets quotation limits and exact notice wording. **Verify against each publisher's current terms; never copy boilerplate from memory.** |
| P7 | **Imprint.** "Bright Forest Publications" is a *proposed* imprint name only. **Never print "Bright Forest Publications LLC" unless that entity legally exists.** For comparison, the Idea Vault printed "Published by Kollabs" while its config said "Kollabs LLC". |
| P8 | **Deferred to publishing prep:** all legal wording, translation permissions, ISBN, Library of Congress (LCCN/CIP), and imprint finalization. Verify current processes at that time rather than relying on stale guidance. |

## 3. Already covered elsewhere

- Dedication: architecture §1 iii (the author writes it).
- Glossary / divine names: only if Appendix D (Word Study Index) does not already do that job (ruling ㉓).
- Bibliography: only if Appendix F (Source Ledger) is not enough for readers (ruling ㉓).
- Cover, chapter openers, Part title pages, running heads, trim: bead BIBLE-493.

**Author name (author ruling 2026-10-15):** always **Marcelo Mario Berta Silva**, everywhere: copyright page, title page, about the author, metadata, ISBN and LoC records.

**Fonts (added 2026-10-15):** box icons use Noto Color Emoji under the SIL Open Font License 1.1. Embedding in the PDF is permitted. Keep `scripts/fonts/NotoColorEmoji-OFL.txt` with the font. Confirm at this step that every other embedded font (Georgia, Helvetica Neue, Times New Roman) is licensed for a sold PDF and print book, or replace it.

**Book title (author decision 2026-10-16):**

| | Title | Subtitle |
|---|---|---|
| English | **The Promise and the Little Season** | *An investigation into prophecy, the great commission, and the thousand years* |
| Spanish | **La promesa y el poco de tiempo** | *Una investigación sobre la profecía, la gran comisión y los mil años* |

Alternates the author proposed, kept on file: *Sailing the Sword* (the double-edged sword of Hebrews 4:12; the author as conduit, Yahweh as author) and *The Sword of His Mouth*. Constraint: the title must not promise an answer the book does not give. The ending is an open question about the present.

**Cover (author decision 2026-10-16):** artwork = Ideogram v3, round 1, image 3 (olive tree at dusk, grafted branch, countable stars, ochre horizon). Settings and seed: `~/Desktop/7-MARS/Bible Study/Cover/round-1/settings.json`. Typesetting: `scripts/cover/make_cover_mockup.py` (Baskerville, cream #F3EBDD). Palette sampled from the art: sky #2A3642 / #3D4D5E, ochre #9A815D. Still owed: upscale from 832×1248 to 1875×2775 (one paid Fal call, run by the author), then back cover and spine once the page count is final.

**Imprint on the cover (author decision 2026-10-16):** under the author's name, *Bright Forest Publishing*, with *kollabs.ai* beneath. The author asked for "Bright Forest Publishing Co."; "Co." was left off under P7, because no entity exists and a company suffix implies one. **Confirmed 2026-10-16: "Bright Forest Publishing"**. It replaces P7's earlier "Bright Forest Publications" everywhere: cover, title page, copyright page, metadata. No legal suffix.
