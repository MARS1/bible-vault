---
title: "ADR-0011 — The Growing Chain and the Evidence Ledger"
type: theology
category: adr
tags: [adr, architecture, navigation, evidence-strength, growing-chain, evidence-ledger, refusals]
created: 2026-08-24
status: accepted
related: "[[ADR-0007-dual-architecture-narrative-and-reference]], [[ADR-0009-three-content-provenance-layers]], [[ADR-0010-unabridged-research-preservation]], [[00-methodology-current]], [[00a-narrative-spine]]"
---

# ADR-0011 — The Growing Chain and the Evidence Ledger

**Status:** Accepted · 2026-08-24 · proposed by the author at Stage 50

---

## Context

By Stage 50 the project holds **50+ stages, 250+ open questions, 11 ADRs, a methodology at version 4.8, and a narrative spine of several thousand lines.** A reader — and increasingly the investigators themselves — cannot see the load-bearing argument at a glance.

Two concrete failures made the need visible:

1. **A reader cannot locate the argument.** The spine records *how* the investigation unfolded and the topical files record *what* it holds, but **nothing renders the current dependency chain** — which claims the conclusion actually rests on, and how strong each is.
2. **Evidence inflation is hard to catch without one.** Within a single day at Stages 48–48½, *both* parties committed the same error in opposite directions: a tranche upgraded *"parousia context"* into *"that lexical pair,"* and this project upgraded *"identity not established"* into *"non-identity adopted."* **Neither was caught by re-reading its own document. Both were caught by comparison against something external.** A maintained chain with explicit per-link confidence is that external thing.

---

## Decision

**Adopt two linked devices — the Growing Chain and the Evidence Ledger — as part of both the research methodology and the eventual narrative architecture.**

### 1. The Growing Chain

A rendering of **only the links the investigation has actually earned**, in dependency order, **each carrying its own confidence label**, and terminating in an explicit **`?`**.

```
A — ESTABLISHED
↓
B — HIGH
↓
C — STRONG CORRESPONDENCE
↓
D — CURRENT HINGE (OPEN)
↓
?
```

**The chain may not display downstream conclusions the investigation has not reached.** Rendering *millennium → little season → present era* while those remain beyond the `?` would prime the reader with the destination and invert the whole method. **The chain grows; it is never pre-drawn.**

### 2. The Evidence Ledger

A per-stage table with **six standing categories, all rendered with equal prominence**:

| Category | Meaning |
|---|---|
| **ESTABLISHED** | the text says it; verified by retrieval |
| **STRONGLY SUPPORTED** | inference the evidence favours, short of established |
| **OPEN** | genuinely undecided; named as such |
| ❗ **REFUSED / RULED OUT** | actively rejected, with the reason |
| **CORRECTED** | previously held, since revised — with what changed it |
| **DEFERRED** | preserved, deliberately not opened |

---

## The clause that matters most: REFUSED gets equal weight

> ### **A chain built only of forward-moving conclusions would systematically hide this project's best work, because much of that work is negative.**

Actual examples the chain would otherwise erase:

- *"Last trumpet" ≠ "seventh trumpet"* — **refused** (ἔσχατος ≠ ἕβδομος)
- **παρουσία is absent from Matthew 24:29–36** — the tranche's strongest lexical claim, refuted
- **Hebrews 10:25 breaks the ἐπισυναγωγή bridge** — the word-family is not inherently eschatological
- **δεῖ and ἄχρι refused as noise** — shared ubiquitous words are not a lexical link
- **No clean verb-object rule in Matthew 13** — a pattern built and destroyed eighteen verses later
- **ἁρπάζω does not encode a heavenly destination** — Acts 8:39 sends Philip to Azotus
- **ἀπάντησις carries no escort sense** — Matthew 8:34's city meets Yeshua and asks him to leave

> ### 🛑 **NONE OF THOSE FORMS A LINK. A CHAIN THAT ONLY ACCRETES WOULD SHOW A TIDY LINE AND SILENTLY DROP EVERY PLACE THE PROJECT TOLD ITSELF NO — WHICH IS PRECISELY THE EVIDENCE THAT MAKES IT AN INVESTIGATION RATHER THAN AN ADVOCACY.**
>
> ### **THEREFORE THE LEDGER'S *REFUSED / RULED OUT* COLUMN IS MANDATORY AND RENDERED AS PROMINENTLY AS *ESTABLISHED*. WITHOUT IT THE CHAIN FLATTERS THE HYPOTHESIS *BY CONSTRUCTION*, AND DOES SO INVISIBLY.**

---

## Three further constraints, each from an observed failure

### A revised link stays historically visible

**Never silently rewrite a link.** When a later stage overturns an earlier one:

```
~~Link 21B — previous conclusion~~
REVISED at Stage 62 — because X evidence changed the assessment.
```

*Consistent with ADR-0007. The chain thereby becomes a history of the investigation, not a snapshot of its current opinion.*

### The chain shows the spine, and says how much it is not showing

> **A chain is a LINEAR metaphor and this investigation is NOT LINEAR.** It has side branches (27½, 30½, 32½, 34½, 35½, 39½, 40½, 45½, 45¾, 46½), methodological interludes, a private branch, and a deferred historical register.

**If the chain becomes the primary artifact, branches get pruned to fit it — the exact compression ADR-0010 forbids.** Therefore: **the chain renders the LOAD-BEARING SPINE ONLY, and each link states how many branches hang off it.** The reader must be able to tell they are seeing a skeleton.

### Every rendering is stamped, and audited with the spine

> **It will drift, because everything hand-maintained in this repository already has.**

**Observed:** at Stage 48 the index still claimed *"30 stages"* and *"Methodology version 2.1"* when the true values were 48 and 4.7. **Not carelessness — just what happens to a hand-kept summary beside a growing corpus.**

**Therefore every chain rendering carries an `as of Stage N` stamp and is audited on the same pass as the spine. A stale chain is worse than none, because it looks authoritative.**

---

## Cadence — natural movements, not a fixed interval

**A numerical interval (every 10, every 15) is arbitrary. The corpus already reveals its own joints:**

| Movement | Stages | What changed |
|---|---|---|
| **I** | 1 – 21½ | commission · covenant · Torah · identity |
| **II** | 22 – 31 | Israel · then resurrection *before* Revelation |
| **III** | 32 – 46½ | Revelation, read sequentially |
| **IV** | 47 – 50+ | the resurrection / gathering hinge |

**Four movements in fifty stages** — roughly every 10–15, but **earned rather than imposed**.

**Three levels of navigation follow:**

1. **Per stage** — one line: *"Current question: …"*
2. **Per movement** — the full Growing Chain, plus what remains open and what the next link requires
3. **Per movement, alongside** — the Evidence Ledger with all six categories

---

## Consequences

**Positive**
- A dissenter can say *"I accept links 1–17; link 18 fails because Matthew 24:31 is Isaiah-style regathering"* — **a testable disagreement, not a verdict on a book.**
- **Anti-circularity:** each link carries its basis and confidence, so an OPEN hypothesis cannot quietly become an ESTABLISHED finding thirty stages later. *(The project has come close to this more than once.)*
- The chain **bridges the two artifacts of ADR-0010** — the readable investigation and the unabridged archive. Follow the chain for the argument; drop into the archive to audit any single link.

**Negative / accepted costs**
- **Real maintenance burden**, and it will drift if unaudited — mitigated by the stamp and the shared audit pass.
- **The linear form under-represents the branches** — mitigated by the branch counts, never eliminated.
- **A confidence label is itself a judgement** and can be wrong. **That is acceptable: a wrong label stated explicitly is falsifiable, whereas an unstated confidence is not.**

---

## What this ADR does not decide

- **The exact rendering** (prose, table, diagram) in the published manuscript.
- **Whether the chain appears at every chapter head** or only at movement boundaries. *The author's instinct — condensed per chapter, full per movement — is recorded as the working preference, not a decision.*
- **Any conclusion whatsoever about the investigation's content.** This ADR is a navigation and evidence-integrity device. **It must never become a reason to prefer one exegetical result over another because it renders more cleanly.**
