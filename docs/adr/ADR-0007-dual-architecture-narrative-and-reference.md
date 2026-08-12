---
title: Dual architecture — reference structure and narrative spine, neither replacing the other
status: active
date: 2026-08-11
project: BIBLE
tags: [eschatology-framework, methodology, manuscript, terminology]
---

# ADR-0007: Dual Architecture — Reference and Narrative

## Terminology
**Reference architecture** — topical files, verse index, glossary, sidebars, source notes. Optimized for *finding*.
**Narrative architecture (Narrative Spine)** — the ordered record of how the investigation actually developed. Optimized for *understanding why each question came next*.
**Intertextuality** — the study of how one text echoes, quotes, alludes to, reuses, or develops another. An **intertextual question** asks: *is this passage deliberately drawing on that earlier passage, and if so, what does the earlier context contribute to its meaning?*

## Context
The vault had been growing well as reference material — topical files, a thorough scripture index, ADRs — and the sequence was *implicitly* preserved through sequential file numbering (00b → 00l) and each file's closing "Next —" section. But there was **no single artifact showing the arc**, and no written rule protecting it.

That's a real risk, because **the order is part of the argument.** Each stage earned the next question: the epistemology was deliberately built before the controversy; Acts 8 corrected an over-narrow claim; Acts 11:19 then corrected the over-broad reading of Acts 8; Ephesians 2 later vindicated a restraint exercised at Acts 2:39. Filed purely by topic, that shape disappears and the manuscript loses its most credible feature — the visible experience of *observation → tension → investigation → correction → stronger formulation*.

A second risk: silently overwriting an earlier position when a later discovery corrects it. In several cases **the correction is the story** — most sharply where the method corrected its own author (Stage 6) and where the lexically convenient reading of *angeloi* was rejected (Stage 11).

## Decision
1. **Maintain both architectures permanently.** Neither replaces the other. New material is appended to **both** the appropriate topical file **and** [[00a-narrative-spine]].
2. **Each stage in the spine records:** the triggering question · the prior assumption or tension · the evidence examined · intertextual connections found · the methodological correction or refinement · the provisional conclusion · the open question leading to the next stage.
3. **Do not silently overwrite a corrected earlier stage.** Preserve the correction as part of the intellectual journey — *unless* the earlier statement was simply factually erroneous (a misremembered citation, a confused name), which is fixed rather than memorialized. The spine keeps a running **Corrections Preserved** table distinguishing the two.
4. **Do not reorganize the master narrative purely by subject** if doing so would destroy how one discovery leads to the next.
5. Prose capture (ADR-0004) and the three manuscript layers (ADR-0006) continue to operate inside both architectures.

## Consequences
- The eventual manuscript can be drafted from the spine as its outline and the topical files as its evidence base — rather than reverse-engineering a narrative from a pile of notes.
- Reader-facing benefit: the reader can see conclusions being *earned*, including the places where the framework cost its own author something. That is the project's strongest claim to credibility and it only survives if the sequence does.
- Auditability: the spine can be read back on request to verify nothing has been flattened, reordered, or quietly overwritten — which is exactly the check that produced this ADR.
- "Intertextuality" is now a named glossary term rather than an unnamed practice, though the vault had already been doing intertextual work extensively (Matthew 24 ↔ Daniel 7, Zechariah 12, Isaiah 13/34, Ezekiel 32, Joel; Acts 15 ↔ Amos 9; Acts 13 ↔ Isaiah 49; Jude ↔ 1 Enoch).
