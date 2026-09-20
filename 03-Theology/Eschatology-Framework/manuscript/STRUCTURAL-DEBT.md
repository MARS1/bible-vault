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
| **Symptom A — table crosses the rule** | Part VI EN, **p. 72**: the two-column table under *"Reading in sequence separated them:"* starts left of the surrounding body-text alignment and crosses the vertical left rule of its containing block. Reported from the rendered PDF, with a screenshot. ✅ **CONFIRMED A SECOND TIME 2026-09-20 — Part VI EN p. 134** *(`ch36`, the `THE BEAST'S PEOPLE / YAHWEH'S PEOPLE` table under "Not hardware. Worship.")*, with a screenshot. **This is the instance the row below had predicted from the stylesheet and flagged as never visually flagged. The prediction held.** |
| **Symptom B — prose sits flush ON the rule** | ❗ **NOT RECORDED WHEN THIS ENTRY WAS FIRST WRITTEN.** The same p. 134 screenshot shows the block's *body text* — "Not hardware. Worship." — beginning essentially **on** the 3px rule, with no inset at all. ✅ **Independently observed 2026-09-20 in Part VIII EN p. 111** *(`ch52`'s "A counting question, not a definitional one" — a `commentary` block containing **no table at all**)*, so this is not a side effect of Symptom A. |
| **Root cause — found, not guessed** | `design-system-v1.css` has two lists that **disagree about `commentary`**. The shared callout frame at §*shared callout frame* gives eleven components `padding: 0.85em 1em 0.9em` — and **`div.commentary` is not in that list**, so it has no padding at all, only a 3px left rule. But the in-callout table rule **does** include `div.commentary table` in the set pulled outward by `margin-left: -0.8em; width: calc(100% + 1.6em)`, whose comment explains it is *reclaiming the callout's own side padding*. A `commentary` table therefore reclaims padding that was never there and lands 0.8em **outside** the rule. |
| **Scope of Symptom A** | 45 EN / 46 ES tables sit inside component blocks, but only the `commentary` ones can collide, because every other component in the reclaim list has the 1em padding the rule assumes. **Four instances, symmetric across editions, all in Part VI:** EN `ch33` L180 and `ch36` L310; ES `ch33` L182 and `ch36` L292. ✅ Two of the four are now visually confirmed *(EN `ch33` p. 72, EN `ch36` p. 134)*; the two Spanish siblings are the same construction and are not separately confirmed. |
| ❗ **Scope of Symptom B — far wider, and it reaches OPEN Parts** | **Every `commentary` block in the manuscript, in every Part, in both editions**, because the cause is a missing property on the component itself rather than anything about tables. ⚠️ **This includes Parts that are not closed** — Part VIII shipped its `d1` snapshot with it. It was not a Part VIII drafting error and no Part VIII source is involved; it is the same stylesheet gap, visible wherever the component is used. |
| ⚠️ **Fix — the recommendation has CHANGED, and Symptom B is why** | **The narrow fix no longer suffices.** Dropping `div.commentary table` from the negative-margin rule resolves Symptom A and **would leave every `commentary` block's prose flush against the rule** *(predicted from reading the stylesheet — the padding it would need is still absent)*. ✅ **Adding `div.commentary` to the shared callout padding list resolves BOTH**, because the negative-margin rule then reclaims padding that genuinely exists, which is precisely what its own comment says it is for: *"Reclaim the callout's own side padding."* ❗ **That comment is itself evidence the stylesheet's author believed `commentary` had padding — so its absence reads as the original oversight, not as an intentional flush-left look.** ⚠️ **But it changes the appearance of every `commentary` block in all Parts, so it is a design decision and not mine to make unilaterally. Put it to the author at repair time.** |
| **Check at the same time** | ✅ EN `ch36` — **done 2026-09-20, defect confirmed** · ES `ch33` and ES `ch36`, still unconfirmed and the same construction · ✅ whether any Part VII/VIII chapter introduced a `commentary` table — **checked 2026-09-19: none did**, Part VIII's tables sit only in `finding` / `evidence` / `textualnote` / `wordstudy`, all of which carry the padding the reclaim rule assumes. |
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
## LAYOUT-003 — comparison-table rows fragment across page breaks

| | |
|---|---|
| **Status** | ❗ **OPEN — logged 2026-09-20, not fixed. Part VI is closed and is not being reopened for it.** |
| ⚠️ **Numbering note** | **Reported as "LAYOUT-002" in review.** That identifier was already taken on 2026-09-19 by the `.gr` uppercase-corruption defect, so this is filed as **LAYOUT-003**. Renumbering the earlier entry would break the commit that references it. |
| **Symptom** | Part VI EN, **pp. 160–161**: row **7** of the trumpet/bowl comparison table splits across the page boundary. The row number `7` and its Bowl cell *("It is done")* stay on p. 160; the Trumpet cell *("loud voices: the kingdom has come")* continues on p. 161 **beneath a repeated header and with no row number or Bowl counterpart beside it.** Reported from the rendered PDF, with a screenshot. |
| **Why it matters more than it looks** | ❗ **The text is all present, so every automated gate passes** — word recovery, section presence and mojibake checks all read this as correct. **What breaks is the semantic relationship the layout creates.** A comparison table's meaning lives in the row: the reader is being asked to see *trumpet 7* against *bowl 7*. Split across a page, the orphaned cell reads as a new fragment, and the reader has to reconstruct a correspondence the table exists to present. |
| **Required behaviour** | A logical row must stay intact across a page boundary. If a complete row will not fit, **the whole row moves to the next page.** Repeating the header on the continuation page is fine and should stay. |
| **Likely fix, when the pass comes** | `break-inside: avoid` / `page-break-inside: avoid` on `tr`, applied at the stylesheet level rather than by forcing a break at this one table. ⚠️ **This is a prediction from the defect's shape, not an observed result** — WeasyPrint's support for row-level break control needs confirming against real output before the fix is called done, and a `tr` taller than a page cannot be honoured at all. |
| **Check at the same time** | Every multi-row comparison table in **all** Parts and **both** editions, not just this one — the cause is a global stylesheet omission, so any sufficiently long table can hit it. ★ **And re-inspect visually, not by text extraction:** `pdftotext` reports this page pair as complete and correct. |
| **Class** | **Presentation only.** No lexical, theological, evidentiary, citation, component-type or structural content is involved. |
| **The lesson it shares with LAYOUT-002** | ❗❗ **This is the second defect in two days that every automated gate passed and only a rendered image caught.** LAYOUT-002 was source text that was correctly wrapped and still rendered wrong; this is content that is all present and still reads wrong. **Extraction confirms presence. It cannot confirm layout, and layout is carrying meaning in both cases.** |

---
---

> ### 📐 **A note on why this register exists at all.** The alternative was a sentence in a session report, which is where structural gaps go to be forgotten. The `sabbatismos` verification gap, the RVR1960 retrieval debt in SYNC-006 and this checkpoint are all the same species of item: **known, bounded, and not yet done.** Each one is cheaper to carry visibly than to rediscover.
