# ADR-0008 — Source-Language-First Localization (English and Spanish Editions)

**Status:** Accepted
**Date:** 2026-08-12
**Context stage:** Stage 17 (circumcision), prompted by the citation burden accumulating across Stages 13–16

---

## Context

The Eschatology Framework is intended to produce a book in **English and Spanish**. Since ADR-0003, three translations have been carried as standing witnesses: **CJB, ESV, and RVR1960**, with originals (Hebrew/Aramaic/Greek) taking priority when wording is the question.

By Stage 16 this had become a practical problem. Every substantive verse was being retrieved in all three translations, which:

- **roughly tripled the retrieval and citation burden** per stage;
- caused repeated partial-fetch failures requiring individual re-retrieval (Hebrews 7:27, Ezekiel 37:26, Leviticus 16:10, and others);
- **distracted from the actual exegesis**, which is conducted at the source-language level anyway.

At the same time, dropping RVR1960 entirely would create a worse problem later. The Spanish edition would arrive with **no record of which passages were translation-sensitive** — and the temptation would be to produce Spanish scripture quotations by rendering the English manuscript, which would make the Spanish edition a translation of a translation.

This is not hypothetical. It has already occurred as a live finding: at Genesis 17:13, ESV and CJB render *berit olam* "**everlasting** covenant" while RVR1960 reads "pacto **perpetuo**." *Everlasting* leans metaphysical; *perpetuo* leans durational. **The Spanish witness frames the *olam* question differently before any analysis begins** — a fact that would have been invisible if RVR1960 had simply been deferred wholesale.

## Decision

**Research once at the source-language level; render separately into each publication language.**

### 1. The evidence layer stores, for important passages:

```
original language → lexical / transliteration note → textual claim → research witness(es) used
```

### 2. English research witnesses are **ESV + CJB** by default.

### 3. RVR1960 is pulled **selectively during research**, when any one of these applies:

- the Spanish wording **materially differs** from the English witnesses;
- a **translation choice is itself part of the argument**;
- the verse is **central enough that it will appear prominently in both editions**;
- Spanish terminology **creates a distinctive theological assumption** worth recording.

Otherwise the full RVR1960 pass is **deferred to the Spanish edition**.

### 4. Every stage file carries a `localization:` frontmatter field:

```yaml
localization: "English research witnesses: verified (ESV/CJB).
  Spanish witness: deferred | checked | materially relevant.
  Original-language basis: Hebrew | Aramaic | Greek.
  Translation-sensitive: yes/no"
```

### 5. The binding rule for the Spanish manuscript:

> **The Spanish manuscript must be localized from the source-of-truth research, not translated mechanically from the English manuscript. Biblical quotations must be taken from the designated Spanish Bible edition (RVR1960); explanatory prose may be translated and adapted. Where an argument depends on Hebrew, Aramaic, or Greek wording, that original-language analysis is preserved identically across editions, and each edition explains how its respective translation renders it.**

## Consequences

**Positive**

- Research velocity increases; retrieval failures drop.
- Translation-sensitive passages are **recorded at the moment they are noticed**, not reconstructed months later.
- The Spanish edition is a genuine edition rather than a derivative translation.
- A Spanish rendering that creates **its own interpretive issue** — one the English never raised — gets caught, because the source-language basis is preserved rather than the English wording.

**Negative / accepted costs**

- Stages 13–16 were produced under the older all-three-translations practice. They are **over-covered**, not under-covered, so no backfill is required for them — but their `localization:` fields are absent and would need adding if the field is ever queried programmatically.
- Judging "materially differs" requires **at least a glance** at the Spanish rendering, so the saving is retrieval-and-recording effort rather than zero attention.
- Some translation-sensitive passages will be missed during research and surface during the Spanish pass. Accepted: the `localization:` field makes that recoverable rather than silent.

## Supersedes / relates to

- **Extends ADR-0003** (translation and textual-source policy). ADR-0003 established *which* witnesses and their priority; this ADR establishes *when* each is consulted and how the two editions relate. **ADR-0003's core rules are unchanged** — originals first when wording is the question, and never write "planet Earth."
- Recorded operationally in `00-methodology-current.md` §Localization Policy (version 1.1).
