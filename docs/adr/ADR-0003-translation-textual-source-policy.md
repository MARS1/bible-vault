---
title: Translation and textual-source policy — RVR1960 as Spanish witness
status: active
date: 2026-08-08
project: BIBLE
tags: [eschatology-framework, translation, terminology, spanish]
---

# ADR-0003: Translation and Textual-Source Policy

## Terminology
**Textual evidence** — the underlying Hebrew/Aramaic (OT) or Koine Greek (NT) wording itself, including manuscript variants where relevant.
**Translation evidence** — a rendering into a modern language (CJB, ESV, RVR1960). A translation is a witness to the text, not the text itself.
**Interpretation** — a conclusion drawn from the text/translations, distinguished per [[00b-biblical-epistemology]]'s existing explicit/inference/speculation split.

## Context
The project will eventually be translated into Spanish. Reina-Valera 1960 (RVR1960) needs to be part of the citation framework — but as a Spanish-language witness readers will recognize, not as a basis for settling what the Hebrew or Greek actually says. Also flagged: don't treat RVR1960 as the only Spanish rendering worth comparing when a passage's exact wording matters — other modern Spanish translations remain a future option if a specific verse is disputed.

## Decision
1. **Three translations, standard citation set going forward:** CJB (primary, Hebrew/Jewish context) → ESV (English cross-reference) → RVR1960 (Spanish witness). All three quoted per verse where feasible, same pattern already used in [[05-scripture-index]].
2. **Hierarchy when a question concerns exact wording/terminology:** original-language text (Hebrew/Aramaic/Greek) → transliteration when useful → literal/structural rendering → the three standard translations above. Go to source language first when the argument turns on a specific word, not just whichever translation happens to phrase it convenient to a conclusion.
3. **RVR1960 does not settle questions about original wording** — it's a witness alongside ESV/CJB, not an upgrade over them or a substitute for checking Hebrew/Greek when that's what the question actually requires.
4. **Existing scripture-index entries get RVR1960 backfilled** (in progress as of 2026-08-08 — see [[05-scripture-index]] for current coverage) — new entries get all three translations from creation, no separate backfill pass needed for new content.

## Consequences
- Every future verse-text fetch should request CJB + ESV + RVR1960 together, not ESV+CJB with RVR1960 added later.
- When an argument depends on a specific Hebrew/Greek term (e.g. *raqia*, *ethnos*, *nous*), that word should be named explicitly rather than relying on any one translation's rendering to carry the argument.
- Prevents "RVR1960 says X" (or any single translation) from silently becoming "therefore X is what God definitively meant" — the same discipline [[00b-biblical-epistemology]] already applies to interpretation vs. text applies here to translation vs. text.
