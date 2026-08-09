---
title: Epistemological cycle — doorway-agnostic, replaces the linear working model
status: active
date: 2026-08-08
project: BIBLE
tags: [eschatology-framework, methodology, terminology]
---

# ADR-0005: Epistemological Cycle — Doorway-Agnostic

## Terminology
**Doorway** — how a question first enters an investigation (Scripture, observation, history, experience, testimony, an anomaly, a hypothesis). Epistemologically neutral — the doorway is not the foundation, and doesn't determine the answer's authority.
**Scripture-foundational** (vs. "Scripture-first-chronologically") — Scripture is the authority everything is ultimately tested against, but that doesn't require every question to have originated in Scripture. A question can start anywhere; the method is what governs what's done with it afterward.

## Context
ADR-0002 recorded a working model — Scripture → Prayer → Ruach → Investigation → Discernment → Testing → Humility → Correction — as a linear chain. That phrasing accidentally implied every investigation must begin with Scripture chronologically, which isn't how real investigation happens (an architectural observation, a historical claim, a dream, a contradiction noticed between two verses can all be the actual starting point). The fix isn't cosmetic — a genuinely doorway-agnostic model changes how claims starting outside Scripture (historical/architectural material, the Tartaria-adjacent hypotheses) get handled: they don't need an apologetic "sorry this didn't start in Scripture," they need to be classified and run through the same test as everything else.

## Decision
Replace the linear working model in `00b-biblical-epistemology.md` with two paired models:

**Model A — The Doorway.** An investigation enters through one of: Scripture, Observation, History, Experience, Testimony, Question, Anomaly, Hypothesis. None of these automatically carries truth on entry.

**Model B — The Epistemological Cycle** (cyclical, not linear):
**Encounter → Classify → Seek → Examine → Compare → Test → Discern → Hold Provisionally → Re-examine ↺**
— with reverence for Yahweh and dependence on the Ruach surrounding the *entire* cycle, not confined to a single "Discern" box.

Each step:
1. **Encounter** — something enters, from any doorway.
2. **Classify** — what kind of thing is this (explicit Scripture, textual variant, interpretation, physical observation, historical document, testimony, tradition, archaeological evidence, hypothesis, spiritual impression, speculation)? Different evidence kinds don't carry the same evidentiary weight — classifying before interpreting prevents smuggling one kind's authority onto another.
3. **Seek** — pursue understanding actively (Proverbs 2), including evidence *against* the idea, not just for it (Proverbs 18:17).
4. **Examine** — the actual evidence, not just the interpretation already attached to it (what the text says / what the artifact is / a photograph's provenance and date / which manuscript and textual tradition).
5. **Compare** — Scripture with Scripture, translation with source language, interpretation with context, historical claim with historical evidence, hypothesis with competing explanations, observation with what should be observable if the hypothesis is true.
6. **Test** (1 Thessalonians 5:21) — not "can I make this fit" but "what would demonstrate I'm mistaken." Refined further: does the evidence **contradict** the hypothesis, merely **permit** it, actively **support** it, or actually **require** it? These four are not equivalent, and claims should be labeled with which one they've actually earned.
7. **Discern** — Ruach-dependence, prayer, wisdom, conscience — not one box in the sequence but present throughout Encounter↔Seek↔Examine↔Compare↔Test, while still subject to the command to test (not a replacement for the prior steps or a rubber stamp after them).
8. **Hold provisionally** — 1 Thessalonians 5:21's "hold fast what is good," with "provisionally" added deliberately for interpretations (not for explicit biblical statements) — holding a position ≠ declaring it incapable of error.
9. **Re-examine** — new evidence, an exposed contextual error, a manuscript discovery, a stronger competing explanation reopens the cycle. Proverbs 18:17 in perpetual operation.

This wraps around, not replaces, the existing 7-step passage test (ADR-0002) — that test operates specifically within Examine/Compare when the classified item is a Scripture passage. Model B is the broader cycle any doorway's claim moves through; the 7-step test is what happens specifically inside it when Scripture is what's being examined.

**Reverence sequence, connecting the "limits of understanding" section to the "pursuit of wisdom" section**: I cannot encompass the mind of Yahweh (Romans 11:33–34, Isaiah 40:13) → therefore I approach Him with reverence (Proverbs 9:10, 1:7 — "the fear of the LORD is the beginning of wisdom/knowledge") → reverence becomes the beginning of knowledge and wisdom → therefore I seek what He permits me to understand (Proverbs 2:1–6, 4:7, 8:17, 18:17, 25:2).

## Consequences
- `00b-biblical-epistemology.md`'s "Working Model" section is superseded by this cycle — ADR-0002's decision text (which cited the old linear chain) is not rewritten, but is understood as amended by this ADR going forward.
- Claims arising from a non-Scripture doorway (historical/architectural observations, the Tartaria-adjacent material in [[03-hypotheses]]) get evaluated the same way as any other claim — classified, examined, compared, tested — not treated as inherently suspect for not originating in a verse.
- The contradicts/permits/supports/requires distinction becomes the standard for stating how strong a claim in [[03-hypotheses]] actually is — "the evidence permits this" is a different, weaker claim than "the evidence requires this," and both are different from "this is my present interpretation" in [[01-convictions]] section B.
