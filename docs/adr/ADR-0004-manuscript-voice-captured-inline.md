---
title: Manuscript-voice commentary captured inline, not deferred to a later prose pass
status: active
date: 2026-08-08
project: BIBLE
tags: [eschatology-framework, writing-style, manuscript]
---

# ADR-0004: Manuscript-Voice Commentary Captured Inline

## Terminology
**Reference material** — citations, translations, sourcing (the bulk of [[05-scripture-index]], the ADRs). Exists to be checked against, not read start to finish.
**Manuscript-voice commentary** — the explanatory, reader-facing insight that makes a citation land — e.g. noticing that 1 Thessalonians 5:19–21 gives permission to investigate without either "everything I think is revelation" or "everything unconventional is false." Written the way it should actually read in the eventual book, addressed to a reader, not "our project."

## Context
Working sessions repeatedly produce genuinely good explanatory commentary — the kind of observation that makes a verse's structure click for a reader — but earlier guidance treated the vault as reference-only, with narrative prose deferred to a later manuscript-drafting phase. That's a real risk: this commentary is generated in the moment, in response to a specific back-and-forth, and is hard to regenerate authentically later once the conversation that produced it is gone. Deferring it doesn't preserve it — it loses it.

## Decision
Manuscript-voice commentary gets captured **inline, at the point it's generated**, directly under the relevant citation in whichever file it belongs to — marked clearly as reader-facing prose, not a citation. Not a separate "someday" manuscript file. This doesn't mean drafting full chapters now (still premature per the existing "don't polish prematurely" guidance) — it means the *sentences that would survive into the book* get written down the moment they're found, so a later prose pass assembles from real material instead of reinventing it.

## Consequences
- Every time a "notice X" / "here's why this verse matters" insight comes up in conversation, it gets written into the relevant vault file in the same session — not left to be reconstructed later.
- Distinguishes two kinds of content in the same file going forward: citation (what the text says) and manuscript-voice commentary (why it matters, written for a reader) — both present, clearly separated, neither missing.
- The eventual prose-drafting phase (still not now) becomes an assembly-and-transition job, not a from-scratch regeneration job.
