# ADR-0012 — Rendered-Layout Integrity Is Part of Build Correctness

**Status:** Accepted
**Date:** 2026-09-25
**Context stage:** Manuscript production, Part VII reader-review revision. Extends ADR-0011.

---

## Context

ADR-0011 made every build read its own PDF back: pages, words recovered, mojibake markers, sections present. That settled one question — *did the text survive rendering?* — and it was the right question to settle first, because a clean exit code from the renderer had already been shown not to be evidence.

It left a second question unasked: *does the page say what the source says?* Three defects in two weeks answered it, and every one of them passed every text gate:

- **LAYOUT-002** — correctly wrapped Greek rendered uppercased, its accents stripped, inside the aside whose argument depended on those accents. `pdftotext` reported the corrupted forms back as though they were the source.
- **LAYOUT-003** — comparison-table rows split across page breaks. In Part VI a trumpet stood on one page and its matching bowl on the next; in Part VII the author found the word *strong* stranded at the foot of p. 49, cut off from the pair of passages it graded. Every word was present, so extraction called the page complete.
- **LAYOUT-004** — an arrow printed as a boxed "?" seven times in the Part VII scorecard. Present in the PDF the author had already reviewed.

All three were found by a human looking at a rendered page. That is an expensive way to find a defect, and it spends the author's review attention on typesetting instead of argument. It also does not scale: Part VII alone has fifty table pages.

The underlying fact is simple and was demonstrated three times: **text extraction confirms presence. It cannot confirm layout** — and in a book built on comparison tables and original-language evidence, layout carries meaning.

---

## Decision

### A manuscript build is not valid merely because its text is intact. Rendered-layout integrity is part of build correctness, and a detected layout defect fails the build.

A layout check may become a build gate when the defect it detects is:

1. **objective** — present or absent, not a matter of taste;
2. **reproducible** — the same source and stylesheet give the same verdict;
3. **detectable from the rendered document itself** — the laid-out pages, not the source text and not extracted text.

Checks that fail any of those three remain manual inspection. The build script continues to name the pages that need it — as the original-language gate already does — rather than pretending to automate a judgement.

### The first implemented gate

**Table-row integrity** — `manuscript/scripts/check-table-breaks.py`, called by `build-manuscript.py` after every render, both editions, every Part. It walks WeasyPrint's own laid-out page boxes and fails the build on:

- a body table row whose boxes land on more than one page;
- a header row left as the last table content at the foot of a page.

A header repeated on a continuation page is expected and passes.

**Validated in both directions before adoption:** against the Part VII `d1-integrity2` source under the old stylesheet it fails, naming exactly the two split rows — including the scorecard row the author had reported; under the corrected stylesheet it passes.

---

## Three things this ADR is careful not to merge

| Layer | What it is | Where it lives |
|---|---|---|
| **Architecture** — *this ADR* | Rendered-layout defects can fail a manuscript build. | here |
| **Implementation** | The current post-render checker; its HTML assembly must mirror `render()` exactly, or it checks a layout that is not the one being printed. | `check-table-breaks.py`, `build-manuscript.py` |
| **Fixes and conventions** | U+FE0E stripped from Pandoc output · `break-inside: avoid` on table rows and a repeating header · smaller table type · scope labels that never hyphenate. | `design-system-v1.css`, `STRUCTURAL-DEBT.md` LAYOUT-003/004/005 |

Replacing the checker, or retiring a CSS rule, does not reopen this decision. Returning to text-only validation does.

---

## Consequences

**Bought.** A class of defect that has reached the author three times now stops at the build. *Build passed* means the pages were checked, not merely the words. New gates have a written bar to clear, so the list can grow without becoming a list of opinions.

**Paid.**

- **About fifteen seconds per Part per build** — the layout is rendered a second time for inspection.
- **Parity maintenance.** The checker reassembles the HTML the same way `render()` does. If the two drift, the gate silently checks the wrong document. Both files say so at the point of assembly.
- **Existing Parts inherit the gate.** Parts I–VI and VIII, in both editions, were **deliberately not re-rendered** when this was adopted. Each must pass at its next appropriate build or final-layout pass, and may fail the first time it runs. That is the gate working, not a regression — and it is not to be turned into a separate review project.

**Deliberately not decided.** Which further layout checks to add. Candidates exist — glyphs falling back to a last-resort font, orphaned component labels — and each must meet the three criteria above before it gates anything.

**Relationship to other records.** Extends ADR-0011's "every build reads its own PDF back" from text to layout. `STRUCTURAL-DEBT.md` records the individual defects; `08-source-ledger.md` and `SYNC-LEDGER.md` are unaffected.

---

## Terminology

| Informal | Formal |
|---|---|
| "the build passed" | **text gates and layout gates passed** — both, not either |
| "check the PDF" | **extraction check** *(is the text there?)* vs **layout gate** *(does the page carry it correctly?)* |
| "table got split" | **split row** — a row whose boxes land on two pages; distinct from a **continued table**, which is correct |
