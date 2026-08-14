# ADR-0009 — Three Content Provenance Layers (Argument / Manuscript Voice / Researcher's Commentary)

**Status:** Accepted
**Date:** 2026-08-14
**Context stage:** Stage 18.8 (Acts 21), where the clearest example of the third layer occurred

---

## Context

The project is producing at least three genuinely different kinds of material, and only two of them had a home.

**The trigger was concrete.** During the Acts 21 investigation, this sequence occurred:

1. A proposal: perhaps Paul's Temple participation was undertaken to publicly demonstrate he was not teaching Jews to forsake Moses.
2. A brake on the word *"technicality,"* because it would make Paul sound as though he were performing a rite he no longer believed — an integrity problem the text does not create.
3. **1 Corinthians 9:19–23** surfaced as a genuine Pauline control on accommodation.
4. A realization that not every offering is a sin offering.
5. A discovery that **Messiah cannot be reduced to the sin offering anyway** — Isaiah 53 uses *asham*, Paul uses Passover, Hebrews uses Yom Kippur.
6. **Numbers 6 then pushed back against the convenient solution**, because a Nazirite completion *does* include a sin/purification offering.

**That whole sequence is valuable. Almost none of it belongs verbatim in a finished chapter.** The chapter might contain three polished paragraphs derived from it.

**Without a defined layer, that reasoning gets either (a) dumped into the manuscript, making the book a commentary on itself, or (b) discarded once its conclusion is extracted — which destroys the only record of how the conclusion was earned.**

**Storage is cheap. Reconstruction is expensive, and sometimes impossible.**

## Decision

**Three content provenance layers are maintained permanently. Every tranche is classified against all three — material may qualify for more than one.**

### 1. Main Argument / Exposition
Textual, lexical, historical, intertextual, and theological evidence. **Destined for normal chapter prose.**

### 2. Manuscript Voice
First-person reflective passages communicating the author's intellectual and spiritual journey, methodological corrections, discoveries, uncertainty, and changing confidence. **Candidates for direct inclusion in the manuscript. Continue capturing inline when discovered (ADR-0004).**

### 3. 🆕 Researcher's Commentary
**Significant conversational reasoning that explains *how* an argument or correction was reached:** initial intuitions · objections · counterarguments · failed explanations · methodological brakes · surprising discoveries · and **why a reading was upgraded or downgraded.**

- **Do NOT automatically convert into manuscript prose.**
- **Do NOT discard after extracting the conclusion.**
- **Preserve as intellectual provenance**, including the **sequence** in which discoveries and corrections occurred.
- Marked in files as **`🔬 Researcher's Commentary`**.

**Later it can feed:** endnotes · methodological asides ("From the Research Notebook" boxes) · appendices · an expanded annotated edition.

### The classification question for every future tranche

> **Does this advance the argument? Is it Manuscript Voice? Does it expose important Researcher's Commentary?**

### Backfill requirement

**When BIBLE-04g (methodology backfill, Stages 1–12) runs, it must also recover Researcher's Commentary wherever the surviving material permits — not merely bring old conclusions into the current methodology.**

### Editorial principle

> **Preserve everything now. Curate later.**

**The manuscript pass is a different activity from research.** It asks: *of everything we learned, what does the reader need to experience — and in what order — to arrive honestly at the conclusions we earned?* **That is composition. This is excavation.** Do not perform the former while doing the latter.

## Relationship to ADR-0006 — a different axis, deliberately

**ADR-0006 defines three *manuscript* layers: Main Exposition · 📖 Exegetical Sidebar · ✍️ Author's Reflection.** Those describe **how content is presented rhetorically inside a chapter.**

**ADR-0009 defines three *provenance* layers.** Those describe **where content came from and where it is destined.**

> ### **They are orthogonal axes, not competing schemes, and must not be merged.**
>
> A ✍️ **Author's Reflection** (ADR-0006, a rhetorical form) is typically **Manuscript Voice** (ADR-0009, a provenance layer).
> **Researcher's Commentary has no ADR-0006 form at all**, because it is not currently destined for the chapter — that is precisely why it needed its own designation.

## Consequences

**Positive**
- The excavation site is preserved, not just the artifact.
- Confidence *changes* become traceable: a reader (or a later session) can see that Reading B was downgraded by Acts 21:25 rather than silently dropped.
- Supplies the raw material for "From the Research Notebook" boxes, which let the reader **watch the method work** rather than receive theology plus proof-texts.
- Protects against the failure mode where a conclusion survives but its warrant is lost.

**Negative / accepted costs**
- Files grow. Accepted — the vault is git-backed and searchable, and the alternative is irreversible loss.
- Requires a judgment call per tranche about what is *significant* commentary rather than ordinary discussion. **Bias toward preserving**; over-inclusion is recoverable, deletion is not.
- **Risk to manage in the eventual manuscript: use Research Notebook boxes sparingly.** If every few pages carries one, the book becomes commentary about itself. **Reserve them for turns that demonstrate the method especially well** — typically where an attempted answer exposed a deeper problem.

## Note on external tooling

**The git-backed Markdown vault remains the single canonical source of truth.** Conversational tooling (source attachments, conversation branches) is a **live laboratory**, not a store of record — introducing a second store would create competing sources of truth.

**Branching maps cleanly onto the existing side-branch concept (ADR-0007):** an experimental line of inquiry can be pursued without derailing the main investigation, and **only what survives returns to the spine.**

## Related

- **ADR-0004** — manuscript voice captured inline, not deferred.
- **ADR-0006** — three manuscript layers (rhetorical axis).
- **ADR-0007** — dual architecture; side branches preserved at point of origin.
- Recorded operationally in `00-methodology-current.md` (v1.6).
