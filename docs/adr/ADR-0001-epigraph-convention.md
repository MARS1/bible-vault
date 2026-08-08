---
title: Epigraph convention for framework documents
status: active
date: 2026-08-08
project: BIBLE
tags: [eschatology-framework, writing-style, terminology]
---

# ADR-0001: Epigraph Convention for Framework Documents

## Terminology
**Epigraph** — a quotation placed at the start of a document to frame its intent. Informally described as "capping" the front of the document. No single standard term exists for the same device at the *end* of a document — referred to here as a **closing epigraph**.

## Context
Wanted every document in the Eschatology Framework (and any eventual compiled PDF) to open and close with something that sets the posture as humility before Yahweh, not confidence in conclusions — described informally as "capping both ends."

## Decision
`00-index.md` opens with 1 Thessalonians 5:19–21 ("test everything; hold fast what is good") as its epigraph, and closes with Psalm 139:23–24 ("search me, O God... lead me in the way everlasting") as its closing epigraph — both in CJB and ESV. This applies to the index file now and to any future compiled document (PDF via `book-pdf`) unchanged.

## Consequences
- Any new top-level document in this framework that serves as a "front door" (an index, or the compiled PDF) should carry this same opening/closing pair unless a deliberate reason overrides it.
- "Epigraph" / "closing epigraph" are now this project's standard terms for this device — use them going forward instead of re-describing informally each time.
