---
title: "Eschatology Framework — Methodology (Current Operative Version)"
type: theology
category: methodology
tags: [methodology, epistemology, exegesis, ingestion-protocol, governance]
reference:
created: 2026-08-12
status: active
version: "1.0 — 2026-08-12, established at Stage 16"
related: "[[00-index]], [[00a-narrative-spine]], [[00b-biblical-epistemology]]"
---

# Methodology — Current Operative Version

> **Version 1.0 — established 2026-08-12 at Stage 16.**
> **This file is the rules by which today's incoming evidence gets processed. Read it FIRST, before ingesting any tranche.**

---

## Why This File Exists

The project accumulated three different kinds of governing document, and the third had no home:

| Document | Preserves | Answers |
|---|---|---|
| **ADRs** (`docs/adr/`) | *why the architecture exists* | "Why do we keep a narrative spine at all?" |
| **[[00a-narrative-spine]]** | *how the investigation unfolded* | "What did we learn, in what order?" |
| **[[00b-biblical-epistemology]]** | *the developed theory of knowing* | "What counts as evidence? What are the rules?" |
| **This file** | ***the operative procedure for processing new material*** | "What do I actually DO when a tranche arrives?" |

**The failure mode this prevents:** the method getting buried inside the very body of research it is supposed to govern. 00b has grown to hold a glossary, a working model, a 7-step test, four formal rules, two specialized instruments, and multiple worked examples. **That is a reference work, not a checklist.** A checklist that lives inside a reference work stops getting run.

**Relationship to 00b:** 00b remains the authority on *what the rules mean and why*. **This file is the executable version.** When they disagree, 00b is the source of truth for content, and this file must be corrected to match.

---

## The Ingestion Protocol

**Every tranche, every time, in this order:**

```
1. READ this file (methodology-current)
2. INGEST the tranche
3. CLASSIFY every substantive claim (12-point structure, below)
4. VERIFY every scripture citation by actual retrieval — never from memory
5. PRESERVE manuscript voice in real time — do not defer to a later prose pass
6. UPDATE the topical file(s)
7. UPDATE the narrative spine — advance, branch, correct, or return
8. RECORD corrections, promotions, demotions, and new open questions
9. COMMIT and PUSH — with verification against the remote
```

**Step 7 is the one most likely to be skipped under time pressure. It is not optional.** ADR-0007 exists because the sequence is part of the argument.

---

## The 12-Point Evidence Structure

For every substantive claim or connection, **preserve where applicable**. Not every point applies to every claim — but **the ones that apply and are missing must be named as missing**, not silently omitted.

| # | Element | Question it answers |
|---|---|---|
| 1 | **Textual observation** | What does the text actually say? |
| 2 | **Immediate literary context** | What surrounds it, and who is being addressed? |
| 3 | **Lexical / original-language evidence** | What is the word, and what is its range? |
| 4 | **Intratextual evidence** | How does this author use it elsewhere? |
| 5 | **Intertextual evidence** | What earlier Scripture is being drawn on? |
| 6 | **Historical / external evidence** | What outside the text bears on it? |
| 7 | **Interpretation** | What do I take it to mean? |
| 8 | **Hypothesis / speculation** | What am I guessing, labeled as guessing? |
| 9 | **Objections / competing readings** | What would a careful opponent say? |
| 10 | **Confidence / epistemic status** | How sure am I, and on what basis? |
| 11 | **Unresolved questions** | What did this open that it did not close? |
| 12 | **Falsification conditions** | **What evidence would strengthen, weaken, or overturn this?** |

> **Point 12 is the discipline's spine.** A claim with no stated falsification condition is not being held as a conclusion — it is being protected. If point 12 cannot be answered for a claim, that is itself the finding.

---

## The Four Boxes — and When Not to Force Them

**[[01-convictions]] · [[02-historical-observations]] · [[03-hypotheses]] · [[04-open-questions]]**

**Preserve the distinction. Do not force every statement into the same category when its status changes under investigation.**

**Record promotions, demotions, corrections, and refinements — never overwrite them.** The record of a position changing is evidence that the method works; erasing it destroys the only proof available.

**Evidentiary scale** (from 00b): **contradicts · permits · supports · requires.** Most findings land on *permits* or *supports*. Say which.

**Tier labels** (from 00b): **A** Text · **B** Interpretation · **C** Historical correlation · **D** Hypothesis.

---

## The Formal Rules, in Execution Order

**1. Category Collapse Test — BOTH FACES.** *Runs first; a malformed question cannot be rescued downstream.*
   - **Collapse:** is this one question, or several packaged as one? *("Is the Law abolished?" is at least eight.)*
   - **Importation:** does this argument depend on a category the text never named? *(moral/civil/ceremonial is theological taxonomy, not biblical terminology.)*

**2. Intertextual Priority.** Earlier scriptural usage **constrains possible meaning**; immediate context still **governs application**. **Never build a rigid symbolic dictionary.** And never run it backwards — a *later* text developing an earlier one is not evidence about what the earlier one meant.

**3. Audience Continuity.** The addressee is presumed continuous unless the text gives sufficient reason to change it. A "you" that shifts to a far-future audience needs textual evidence, not a system that requires it.

**4. Anti-Replacement Principle.** **Disproving interpretation A does not establish interpretation B.** Expanded semantic possibility requires renewed contextual testing, not immediate doctrinal substitution. *Apply preemptively where a stage's own conclusion is attractive.*

**5. Distinguish explicit text from inference, and inference from speculation.** Every time.

---

## The Two Specialized Instruments

- **The 7-Step Test** — for a **passage**, before it enters [[01-convictions]].
- **The Eleven-Question Protocol** — for a **Torah command** (origin / audience / purpose / prophetic anticipation / Yeshua / Acts / apostolic / retained? / transformed? / discontinued? / **inferring beyond the text?**). Q8–10 are deliberately **not** complements.
- **The Companion Question** — always ask **"what was the purpose of the thing that changed?"** alongside "what changed?"

---

## Source and Translation Policy (ADR-0003)

- **Originals first when wording is the question** — Hebrew, Aramaic, Greek.
- **Three standing witnesses:** **CJB · ESV · RVR1960.** RVR1960 is a Spanish *witness*, never the basis for a Hebrew/Greek claim.
- **When translations diverge on a clause the project would like to use — print the divergence.** Do not bury it. Precedents: CJB's "this people" (Matthew 24:34), Zechariah 6:13's separate priest, Isaiah 53:10's conditional.
- **Never write "planet Earth."** Exegetical hygiene — the phrase imports a frame *gē*, *kosmos*, and *oikoumenē* do not carry.
- **Verify every citation by retrieval.** Never record a verse from memory. Record **"NOT RETRIEVED"** rather than approximate.
- **Record versification offsets** where found (CJB Jeremiah 31 is one verse behind; Zechariah 2:6 differs).

---

## Manuscript Layers (ADR-0006)

- **Main Exposition** — carries the argument.
- **📖 Exegetical Sidebar** — preserves a real secondary textual question without letting it hijack the chapter. States what the passage establishes, what it does not, then **closes**. No promised follow-up.
- **✍️ Author's Reflection** — personal experience where it illuminates why a passage matters. Visibly distinct from textual evidence.

**Manuscript voice (ADR-0004) is captured in real time** — especially: *why this matters*, *notice the sequence*, methodological discoveries, moments where evidence corrected an assumption, and explanations of why a connection is strong, weak, or premature. **Never deferred to a later prose pass.**

---

## Side Branches

**Preserve at the point they arose. Never allow them to reorder the main argument.**

Established branches: **Daniel 2 / Rupes Nigra** (Stage 13) · **Leviticus 16 / Azazel / 1 Enoch** (Stage 16).

**The rule that governs them:** *a passage can be true and relevant to the theology while not being evidence for the specific question under investigation.* Filing something forward is not dismissing it.

---

## The Overriding Constraint

> # **Do not protect the author's current conclusions. The method outranks the hypothesis.**

- **Preserve contrary evidence.** If new evidence weakens an existing conviction or hypothesis, **flag it — do not harmonize it away.**
- **Give less rope, not more, to the possibilities most convenient to the framework.** *(Worked instance: resurrection→national-restoration at Stage 15.)*
- **When a stage's own conclusion is attractive, apply the brake preemptively.** *(Worked instance: Stage 16 §18.)*
- **Record the project's own self-corrections** in the spine's corrections table — including corrections to this project's own coined phrases.

---

## Verification Honesty

- **A failed retrieval is a finding, not an inconvenience.** Record **VERIFICATION FAILED** with the reason and the exact step required to complete it. *(Worked instance: 1 Enoch, HTTP 403, Stage 16 §21.)*
- **Never assert an external source's content from conversational report alone.** Mark it **REPORTED — NOT VERIFIED** and name what would verify it.
- **Static-analysis language discipline** (global rule): for anything derived from reading rather than observing, say **"traced"** or **"the text would mean X if"** — never "confirmed."

---

## Change Log

| Version | Date | Change |
|---|---|---|
| **1.0** | 2026-08-12 | Established at Stage 16, in response to a direct request to make the operative method auditable rather than implicit. Consolidates ADR-0002 through ADR-0007, 00b's four formal rules and two instruments, and the ingestion protocol that had been running informally since Stage 1. |

> **When this file changes, note it here.** The methodology is living and may be refined by new evidence — **but later tranches must inherit the latest version without silently rewriting earlier stages.** An earlier stage judged under version 1.0 stays labeled as such.
