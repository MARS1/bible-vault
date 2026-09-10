# ADR-0011 — Manuscript Production Architecture (Versioning, Sibling Editions, and Semantic Components)

**Status:** Accepted
**Date:** 2026-09-10
**Context stage:** Post-Stage 66. The investigation closed 2026-09-09; this governs the artifact it produces.

---

## Context

The investigation ended with sixty-six stages, one hundred and nine archive files, and a book to produce in two languages. Three questions had no recorded answer, and all three are expensive to answer late.

**How are versions preserved?** The obvious instinct is `part-01-v2.md`, then `-final`, then `-final2`. Every project that has ever done this regrets it, and the regret arrives exactly when someone asks which file was the one that got reviewed.

**What is the Spanish edition?** ADR-0008 already established that research happens once at source-language level and each edition renders separately. It did not say what that means in production: whether Spanish is drafted alongside English, after all nine Parts, or somewhere between, and what happens when the Spanish witness raises a problem the English does not have.

**How do the book's recurring elements get their appearance?** The manuscript has scripture quotations, orientation checkpoints, open questions, textual notes, findings, word studies, historical context and person notes. Styling each occurrence by hand means restyling five hundred pages by hand later.

The trigger for writing this down was a small failure. A build script was told to snapshot a milestone that already existed, and it happily would have overwritten the exact text a reviewer had read. The fix was not to be more careful.

---

## Decision

### 1. Git is the history. Snapshots are the milestones. The tool enforces both.

Canonical chapter files are revised **in place**. No `v2`, no `final`, no dated copies in `manuscript/en/` or `manuscript/es/` — git already preserves every prior state byte for byte.

Every state actually submitted for substantive review gets an **immutable milestone snapshot** under `manuscript/_snapshots/<lang>/part-NN/`, carrying a MANIFEST that records the **exact git commit it was generated from**.

`build-manuscript.py --snapshot <name>` **refuses to overwrite an existing milestone and exits.** A new reviewed state gets a new name; it never silently replaces the previous one.

### 2. Spanish is a sibling edition, produced in staggered tandem.

Per Part: draft English → build → review → correct → commit as the reviewed baseline → snapshot → **draft Spanish from that baseline plus the Master Evidence Vault** → review → snapshot → next Part.

Not simultaneous, which creates two moving targets and lets Spanish inherit English wording still in flux. Not after all nine Parts, which produces an edition that reads as a translation bolted on.

Scripture is quoted **directly from RVR1960**, never rendered into Spanish from an English quotation. Load-bearing original-language claims are checked independently in each edition.

**A translation witness is evidence about that translation, never about the Greek or the Hebrew.** Where the editions cannot say the same thing, the case is logged in `SYNC-LEDGER.md`. A **theological or evidentiary divergence is a defect** and corrects both editions; a **prose divergence is expected**, because identical sentences would mean the Spanish had been translated rather than written.

Register is fixed in `ES-REGISTER.md` and checked mechanically on every Spanish build.

### 3. Components are semantic. Appearance is central. Claim type and evidence strength never merge.

Callouts are fenced divs in the source — `person`, `whereweare`, `earned`, `openquestion`, `textualnote`, `finding`, `wordstudy`, `historical`, `evidence`, `claimtypes`, `chain`. The source says **what** a thing is; `design-system-v1.css` decides **how** it looks. Nothing is styled by hand.

Every component is distinguishable in grayscale, by rule weight, rule style, indentation and a small sans-serif label. **No component means anything by colour alone.**

And one separation is permanent:

- **`claimtypes`** — *what kind of claim is this?* Explicit text · strong cumulative inference · probable reconstruction · historical observation · hypothesis · open question. **A set, not a ladder.** Historical observation is not weaker than probable reconstruction; an open question is a status, not a faint conclusion.
- **`evidence`** — *how hard does this evidence bear?* **CONTRADICTS → PERMITS → SUPPORTS → REQUIRES.** The only genuine scale.

They may never share a component, a heading, or a visual treatment.

---

## Consequences

**Bought.** Restyling the entire book in both languages is one CSS edit. The question *"which English state was this Spanish Part built from?"* has an exact answer months later without checking out a commit. A reviewer can always reopen the precise text they reviewed. Every build reads its own PDF back and reports pages, words recovered, mojibake markers and any section that failed to render, because a clean exit code from the renderer is not evidence.

**Paid.** Two editions must be corrected whenever a divergence turns out to be evidentiary rather than stylistic — the Spanish lane has already produced two such findings (Revelation 20:10's supplied *estaban*, Romans 9:4's singular *el pacto*), which is the argument for the tandem workflow and also its ongoing cost. Snapshots accumulate: eleven exist for Part I alone across both languages. That is the intended trade.

**Deliberately deferred.** Chapter openers, Part title pages, running heads, final trim size, cover, indexes and final pagination. Parts II through IX will reveal components that do not exist yet, and typesetting before they appear would be work done twice. Design System v1 is the visual grammar, explicitly not the finished book.

**Relationship to other records.** This ADR records *why*. `10-manuscript-architecture.md` records *what* — the operative chapter map and twenty-two numbered rulings — and is the document to read before touching manuscript files. This extends ADR-0008 from research policy into production, and carries ADR-0010's rule against collapsing evidence types into the design system itself, where §3's separation makes the collapse structurally harder rather than merely forbidden.

---

## Terminology

| Informal | Formal |
|---|---|
| "the reviewed version" | **milestone snapshot** — immutable, manifest-bearing, refuses overwrite |
| "the Spanish version" | **sibling edition** — never "the translation" |
| "the boxes" | **semantic components** — declared in source, styled centrally |
| "how sure are we" | either **claim type** or **evidence strength** — never both at once |
