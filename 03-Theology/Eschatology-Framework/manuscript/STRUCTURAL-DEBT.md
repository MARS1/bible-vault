---
title: "Manuscript — Structural Debt Register"
type: reference
category: theology
tags: [manuscript, structural-debt, assembly, architecture]
created: 2026-09-11
status: active
localization: "★ TWO CLASSES, BOTH DEFERRED. (1) STRUCTURAL DEBT — things the approved architecture calls for that the draft does not yet have; missing structure, not wrong content. (2) PRESENTATION DEFECTS — added 2026-09-19; deterministic rendering faults where the words are right and the output is not. ❗ NEITHER CLASS CONTAINS WRONG CONTENT, and a Part closed for Draft 1 is NOT reopened to service either one. Structural items resolve at assembly or when that Part is next legitimately open. Presentation items follow the Part VII precedent: presentation-only fix, proof that it is presentation-only, full gates, visual inspection, the existing milestone PRESERVED, and a separate labelled format-fix milestone beside it."
related: "[[10-manuscript-architecture]], [[SYNC-LEDGER]], [[ES-REGISTER]]"
---

# Structural Debt Register

> ### **WHAT GOES IN HERE: an element the approved architecture specifies that the current draft does not contain, discovered after the affected Part was closed for Draft 1.**
>
> ### 🛑 **AND THE RULE THAT MAKES THE REGISTER WORTH HAVING: finding an item here is NOT a reason to reopen a closed Part.** Closing a Part means closed, not "closed except for one more thing." Items are serviced at whole-manuscript assembly, or opportunistically when that Part is open for another reason.

---

## SD-001 — Growing Chain Checkpoint 1 is missing from Part I

| | |
|---|---|
| **Status** | ❗ **OPEN — deferred to whole-manuscript assembly by explicit instruction, 2026-09-11.** |
| **What the architecture calls for** | `10-manuscript-architecture.md` §2 places **GROWING CHAIN CHECKPOINT 1** at the end of Part I: *"An audience question has become a covenant question."* |
| **What the draft has** | Part I ends at Chapter 6 with `whereweare` and `earned` and **no `chain` block**. |
| **How it was found** | Drafting Part III, whose Chapter 19 carries **Checkpoint 2** as specified. Writing the second one made the absence of the first visible. |
| **Why it was not fixed on discovery** | Part I and Part II were closed for Draft 1 in both editions on 2026-09-11, with the explicit framing that they are *legitimately* closed rather than "closed except for one more thing." Adding a component to a closed Part would have contradicted that, and would also have desynchronized EN Part I from its Spanish sibling and both from their immutable milestones. |
| **What resolving it will require** | The EN Part I chapter 6 gets a `::: chain` block; **ES Part I chapter 6 gets the sibling block in the same place** (component parity is check 8 of the bilingual integrity check); both Parts rebuild and take new milestones. |
| **Confirm before acting** | Whether the approved architecture still calls for six checkpoints at assembly time. It currently specifies Checkpoints 1 through 6 across Parts I, III, V, VI, VII and VIII. |

---

# Presentation defects

> ### **A SECOND CLASS, ADDED 2026-09-19.** The register above holds *missing structure*. This section holds *deterministic rendering defects*: the words are right, the output is not. They are logged here rather than fixed on sight for the same reason — a closed Part is not reopened for them.
>
> ### ✅ **And the Part VII precedent governs how they are eventually serviced:** apply the presentation-only correction · prove it is presentation-only · rebuild and re-run every gate · visually inspect the repaired locations · **preserve the existing immutable milestone** and take a separate, clearly-labelled format-fix milestone beside it, whose manifest records what changed. **Closed forbids discretionary rewriting. It does not freeze a rendering defect forever.**

## LAYOUT-001 — tables inside `commentary` overflow the component's left rule

| | |
|---|---|
| **Status** | ❗ **OPEN — logged 2026-09-19, not fixed. Part VI is closed and is not being reopened for it.** |
| **Symptom** | Part VI EN, **p. 72**: the two-column table under *"Reading in sequence separated them:"* starts left of the surrounding body-text alignment and crosses the vertical left rule of its containing block. Reported from the rendered PDF, with a screenshot. |
| **Root cause — found, not guessed** | `design-system-v1.css` has two lists that **disagree about `commentary`**. The shared callout frame at §*shared callout frame* gives eleven components `padding: 0.85em 1em 0.9em` — and **`div.commentary` is not in that list**, so it has no padding at all, only a 3px left rule. But the in-callout table rule **does** include `div.commentary table` in the set pulled outward by `margin-left: -0.8em; width: calc(100% + 1.6em)`, whose comment explains it is *reclaiming the callout's own side padding*. A `commentary` table therefore reclaims padding that was never there and lands 0.8em **outside** the rule. |
| **Actual scope — narrower than it first looked** | 45 EN / 46 ES tables sit inside component blocks, but only the `commentary` ones can collide, because every other component in the reclaim list has the 1em padding the rule assumes. **Four instances, symmetric across editions, all in Part VI:** EN `ch33` L180 and `ch36` L310; ES `ch33` L182 and `ch36` L292. |
| **Likely fix, when the pass comes** | Prefer the narrow one: **drop `div.commentary table` from the negative-margin rule.** Adding `div.commentary` to the shared padding list would also work and would change how every `commentary` block looks in **all** Parts, which is a design change rather than a repair. ⚠️ Confirm against the rendered output before choosing — this is a prediction from reading the stylesheet, not an observed result. |
| **Check at the same time** | Both editions' `ch36` tables, which were never visually flagged and are the same construction · and whether any Part VII/VIII chapter has since introduced a `commentary` table. |
| **Class** | **Presentation only.** No lexical, theological, evidentiary, citation, component-type or structural content is involved. |

## LAYOUT-002 — emphasis nested inside a `.gr`/`.he` span renders as uppercased source text

| | |
|---|---|
| **Status** | ❗ **OPEN for Parts IV and VII — logged 2026-09-19. The CSS cause is FIXED; the closed Parts' rendered artifacts still carry it, and they are NOT being reopened for it.** |
| **Symptom** | Polytonic Greek inside a callout table rendered **uppercased and stripped of its accents** — <span class="gr">χρόνον μικρόν</span> printing as `XPONON MIKPON`, with chi and rho reading as Latin X and P. Caught by rendering Part VIII ch51's word-study table to an image during the visual inspection the original-language gate mandates. |
| **Root cause — found, not guessed** | `design-system-v1.css` opted `.gr`/`.he` out of the uppercase label treatment by declaring `text-transform: none` **on the span**, relying on inheritance. That protects source text the emphasis *wraps* — `**<span class="gr">…</span>**`. ❗ **When the emphasis sits *inside* the span** — `<span class="gr">…**…**…</span>` — the `strong` matches `div.<callout> strong:first-child` (a text node before it does not count for `:first-child`), carries its **own** `text-transform: uppercase`, and that own declaration beats the inherited `none`. The table-cell rule below it reduces tracking but deliberately **keeps** the uppercase, so cells are the worst case. |
| **Actual scope** | **21 nested-emphasis spans in total**, of which the closed ones are: **EN `ch21` ×1 · EN `ch46` ×3 · ES `ch21` ×1 · ES `ch46` ×3.** *(Part VIII's own 13 — EN `ch51` ×9, `ch52` ×4 — were fixed at the CSS level before that Part was built, so no Part VIII artifact ever shipped with it.)* ⚠️ Each span only corrupts if it sits inside a callout or a `th`; the count above is the upper bound, to be confirmed per instance at repair time. |
| **Fix — already applied to the stylesheet** | The opt-out now reads `.gr, .he, .gr *, .he *`, which matches the rule's own stated intent: source text opts out of every label treatment **wherever it sits**. ✅ **No source file needs editing.** Parts IV and VII render correctly the moment they are next built. |
| **What remains owed** | Parts IV and VII are closed in both editions, so their **existing PDFs still show the corruption**. They get a rebuild + a format-fix milestone at their next legitimate presentation-repair pass, per the Part VII precedent recorded above — **not now, and not as a reason to reopen them.** |
| **Class** | **Presentation only.** No lexical, theological, evidentiary, citation, component-type or structural content is involved. The source text was correct and correctly wrapped throughout; only its rendering was wrong. |
| **The lesson worth keeping** | ❗❗ **The original-language gate PASSED these pages.** It verifies that source text is *wrapped*, which is exactly what it claims to do — and wrapping is not rendering. **`pdftotext` also reported the uppercased forms back as though they were the source.** Only rasterizing the page and looking at it caught this, which is why that step is mandatory rather than advisory. |

---
---

> ### 📐 **A note on why this register exists at all.** The alternative was a sentence in a session report, which is where structural gaps go to be forgotten. The `sabbatismos` verification gap, the RVR1960 retrieval debt in SYNC-006 and this checkpoint are all the same species of item: **known, bounded, and not yet done.** Each one is cheaper to carry visibly than to rediscover.
