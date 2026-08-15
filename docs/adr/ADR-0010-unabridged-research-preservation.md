# ADR-0010 — Unabridged Research Preservation (Three Artifacts, and the Rule Against Collapsing Evidence Types)

**Status:** Accepted
**Date:** 2026-08-15
**Context stage:** Stage 21½ (orientation), prompted by the Ephesians 2:15 evidence-typing distinction

---

## Context

The project is producing **three different artifacts from one investigation**, and they have three different requirements. Conflating them is the risk.

The immediate trigger was small and precise. At Ephesians 2:15 the translations diverge materially (ESV: Messiah *abolishing the law*; CJB: *destroying the enmity occasioned by* the Torah). The reasoning that followed was recorded as:

> **"Contextual datum favoring the narrower reading — recorded as contextual, not lexical."**

**That distinction is not editorial scaffolding. It is part of the intellectual history of the conclusion.** Twenty months from now, "our notes say the narrower reading is preferred" is nearly useless. What must be recoverable is:

> ESV rendered X · CJB rendered Y · we noticed the disagreement · the immediate discourse repeatedly uses *hostility* (2:14, 2:16) · therefore **contextual** evidence favoured Y · **and we deliberately did NOT call that lexical proof** · Greek syntax remained an outstanding verification task.

**That is backwards-compatible research.** The manuscript will never contain it. The project must.

**A second, related risk surfaced the same day:** if the vault is eventually reorganized purely by subject — Sabbath under Torah, Cornelius under Gentile inclusion, Matthew 24 under eschatology, Enoch under Second Temple literature — the reorganization is *good for reference* and **destroys something epistemologically meaningful if it becomes the only organization.** The chain *A → raised B → contradicted C → forced revisiting A → produced D* is the record of the method actually correcting us.

## Decision

### The three artifacts, permanently distinguished

| # | Artifact | Requirement |
|---|---|---|
| **1** | **The Research Record** — complete and unabridged | **Nothing substantive is discarded.** Approaching an **append-only event log** |
| **2** | **The Structured Vault** — this repository | **Derived state**: claims → evidence → classification → objections → corrections → confidence → open questions → relationships → sequence |
| **3** | **The Manuscript** — eventual book | **Ruthlessly edited.** The reader may never see 80% of the above |

> ### **The manuscript should not contain everything. The project absolutely should.** Completely different requirements.

### The Unabridged Research Preservation Rule

> **The polished manuscript is an editorial product; the research corpus is not. Preserve the complete intellectual provenance of the investigation even when material will never appear in the book. Do not discard substantive reasoning merely because it is repetitive, methodological, conversational, speculative, superseded, or too detailed for publication.**
>
> **Preserve especially:** distinctions between **lexical, grammatical, contextual, intertextual, historical, textual-critical, theological, and inferential** evidence · translation divergences · rejected readings **and why they were rejected** · corrections **and what caused them** · confidence classifications · falsification conditions · methodological brakes · unresolved questions · side branches · manuscript-voice insights · and reasoning that explains **why** a conclusion was reached.
>
> ### **Compression may create a NEW derivative artifact; it must not replace or overwrite the fuller artifact from which it was derived.**
>
> **Every major conclusion in the structured vault must remain traceable backward to the reasoning and evidence that produced it.** The goal is **backwards-compatible research**: a future reader, researcher, or model should be able not merely to recover *what* we concluded, but to reconstruct **why** we concluded it, **what alternatives were considered**, **what evidence carried what kind of weight**, and **what remained unresolved** at that point in the investigation.

### ❗ Never Collapse Evidence Types

> - **"Contextually favored" must not silently become "lexically established."**
> - **"Plausible" must not become "proven."**
> - **"Unverified" must not become "false."**
> - **A later conclusion must not erase the uncertainty under which an earlier stage operated.**

**This is the clause with the most day-to-day force.** Evidence-type collapse is quiet, feels like tidying, and is nearly undetectable downstream.

### Both organizations are mandatory

**Subject topology** — *where does this knowledge belong?* — and **discovery chronology** — *how did we get here?*

**[[00a-narrative-spine]] carries the second. Topical organization must NEVER replace it.** *(This is ADR-0007 restated with a sharper reason: the chain of correction is itself evidence that the method works.)*

**Corollary, added at the same time:** **interlude stages (`16½`, `18½`, `21½`) are stages in their own right.** A methodological stage is still a stage. **Never merge one into its neighbour because it is not exegetical** — Stage 21½ freezes the project's destination and keeps preterism downstream of the evidence, which is load-bearing, not supplementary. **The spine now carries an explicit Stage Index making every stage addressable by number.**

## Consequences

**Positive**
- A future model can receive the concise methodology and relevant structured files first, then **drill backward into the unabridged material when it needs provenance.**
- Confidence *changes* stay auditable: *Reading B was downgraded by Acts 21:25* rather than silently vanishing.
- Protects against the specific failure where a conclusion survives but its warrant is lost — the thing that makes old research unusable.
- **Millions of words are not inherently a problem.** Millions of *unstructured* words are. With stable stage numbers, cross-references, classifications, indexes, a narrative spine, corrections and provenance, it becomes a **research corpus**.

**Negative / accepted costs**
- The vault grows substantially. **Accepted** — git-backed, searchable, and the alternative is irreversible loss.
- Some files carry material that will never be published. **That is the point, not a defect.**
- Requires per-tranche judgment about what is *substantive*. **Bias toward preserving**; over-inclusion is recoverable, deletion is not.

## Related

- **ADR-0007** — dual architecture; the narrative spine that this ADR makes non-optional.
- **ADR-0009** — the three content *provenance* layers (Main Argument / Manuscript Voice / 🔬 Researcher's Commentary). **ADR-0009 says how material is classified inside a file; ADR-0010 says what may never be thrown away and what the three artifacts are for.** Complementary, not overlapping.
- **ADR-0004** — manuscript voice captured inline.
- Recorded operationally in `00-methodology-current.md` (v2.1).
