---
title: Three-layer manuscript distinction — Main Exposition, Exegetical Sidebar, Author's Reflection
status: active
date: 2026-08-09
project: BIBLE
tags: [eschatology-framework, writing-style, methodology, terminology]
---

# ADR-0006: Three-Layer Manuscript Distinction

## Terminology
**Main Exposition** — the biblical/historical argument itself. What the text says and how the case develops.
**Exegetical Sidebar** — an important secondary textual question a passage raises naturally, preserved without letting it hijack the chapter. States what the passage establishes, what it does **not** establish, then closes. **No promise of later treatment.**
**Author's Reflection** — Marcelo's own experience or prior questions, where they illuminate why a passage matters. Visibly distinct from textual evidence; never mistakable for part of the biblical argument.

## Context
Two situations produced the same problem from opposite directions. Acts 10 raised the clean/unclean food question — real, worth addressing, but not what the passage is about; left in the main flow it would read as a thesis being argued. Acts 15 raised a personal memory (wrestling years ago with whether physical circumcision was required) — genuinely illuminating for why the passage matters, but left unmarked it could be mistaken for part of Luke's argument.

The failure mode both share: **treating "chase the tangent" and "discard the tangent" as the only options.** A rigorous manuscript doesn't suppress interesting secondary questions — it classifies them correctly, so the reader can weight them correctly.

## Decision
Three permanent, visibly distinct layers in the eventual manuscript and in the vault files that feed it:

1. **Main Exposition** — default. Carries the argument.
2. **Exegetical Sidebar** — marked as such. Structure: *this question is real → here's what this passage establishes about it → here's what it does not establish → return to the argument.* Closes cleanly with no dangling commitment to a future chapter (promising follow-up creates a debt that may never be paid, which is its own form of dishonesty).
3. **Author's Reflection** — marked as such. Personal experience, clearly labeled as personal experience rather than biblical evidence.

Retroactive application: the Acts 10 food-law discussion becomes a formal **Exegetical Sidebar**; the circumcision material arising from Acts 15 becomes a formal **Author's Reflection**. Neither gets flattened into the main Acts narrative.

## Consequences
- The reader can always distinguish three different epistemic claims: *here is what the text says* / *here is what I infer from it* / *here is where it intersects something I personally wrestled with*. That distinction is what this entire project exists to teach, so the manuscript's own structure should embody it rather than merely describe it.
- Scales to the harder material still ahead. When Enoch, ancient architecture, alternative chronology, Tartaria, or geography come up, the same discipline applies: the observation can be preserved and connected without silently acquiring the epistemic weight of the main textual argument.
- Pairs with ADR-0004 (prose captured inline) — that ADR governs *capturing* explanatory voice; this one governs *which layer* it belongs to once captured.
- A sidebar that cannot state what the passage does *not* establish is not ready to be written — that clause is the load-bearing part, not a formality.
