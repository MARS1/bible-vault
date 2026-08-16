# Session Log — BIBLE

Running log of working sessions. Append after every session — never overwrite.

---

## 2026-04-10

**Session:** Initial vault scaffold

**What was done:**
- Created vault structure at `/Volumes/VM/OBSIDIAN/BIBLE/`
- Generated CLAUDE.md, LLM-CONTEXT-GUIDE.md, SESSION-LOG.md, MODS.md
- Created .claude/settings.local.json (vault-safe permissions)
- Created .gitignore, _credentials/, _templates/
- Created .obsidian/app.json (minimal Obsidian config)
- Wired Notion workspace
- Initialized git repository
- Created initial commit

**Next steps:**
- Open vault in Obsidian
- Start systematic Bible reading plan
- Push to GitHub

---

## 2026-08-06 — Eschatology Framework: seed + tranche 2

**What we did:**
- Built `03-Theology/Eschatology-Framework/` — a 5-file structure for organizing Mars's ongoing preterist eschatology research, fed in as pasted ChatGPT-conversation tranches across sessions (source model's own context window runs out, this vault is the persistence layer)
- Structure: `00-index.md` (system explainer + governing principle), `01-convictions.md` (split explicit-Scripture vs. personal-synthesis), `02-historical-observations.md`, `03-hypotheses.md`, `04-open-questions.md`, `05-scripture-index.md` (thematic citation appendix added in tranche 2, specifically so no verse silently drops between tranches)
- Merged 2 tranches: seed (millennium/Rev 20 origin story, Nephilim, Tartaria/architecture, geocentrism) + tranche 2 (Great Commission verse set, Yeshua HaMashiach name study, Messianic Israelite identity, covenant-continuity verses, Ruach HaKodesh guidance)
- Deliberately kept 3 things out of Convictions and flagged unconfirmed rather than guessed: the "respawn after millennium" verse, where believers are during the millennial reign per this reading, and the Solomon "test/search all things" verse (candidates only: Prov 25:2, Eccl 7:23)

**Key decisions:**
- 4-tier certainty split (Convictions/Observations/Hypotheses/Open Questions) instead of one running doc — prevents inference and speculation from silently reading as scriptural fact
- Geocentrism/enclosed-earth cosmology placed in Hypotheses, not Convictions — the firmament/four-corners text itself is a conviction, the cosmological model built on it is Mars's reading, not the historic consensus reading of those same verses
- bd (BIBLE-2tj) + `bd remember` is the cross-session continuity mechanism, not a separate MemPalace tool — matches this vault's existing "bd, not MEMORY.md" rule

**KodeArk extraction:** `02-Patterns/Graduated-Certainty-Note-Structure.md` — generalized the 4-tier + citation-index structure as a reusable pattern for any incremental research/belief-documentation project, not just this one

**Tests:** n/a (vault, no code)

---

## 2026-08-16 — Eschatology Framework: Stages 14–22 (Torah → covenant → Israel)

> ⚠️ **Log gap acknowledged:** Stages 3–13 were built across intervening sessions that never appended here. The narrative spine (`00a-narrative-spine.md`) and git history are complete; this file is not. Recovering those entries is *not* worth doing retroactively — the spine already carries the sequence, which is the thing that mattered. Noted so a future reader doesn't mistake the gap for lost work.

**What we did — nine stages, one continuous argument:**
- **14** Matthew 5:17–18 — the two "untils", `plēroō` vs `katalyō`, and a six-way distinction the passage forces
- **15** What actually changes in the New Covenant. Key refinement from Mars mid-tranche: *"one covenantal story containing multiple covenants, culminating in Messiah"* — replacing the earlier, sloppier "one covenant"
- **16 / 16½** Sacrifice and priesthood; then a late-numbered `00r-what-is-a-covenant.md` written *after* Stage 17 but numbered before it, because the definition turned out to be load-bearing upstream
- **17** Circumcision — covenant sign and heart, §1–40
- **18 / 18.5 / 18.6** Clean and unclean, Noah → Messiah; Romans 14; 1 Timothy 4 under full pressure
- **18.7 / 18.8 / 18.9** Acts 15's four requirements; Acts 21 and the two groups; Numbers 6 — *"and the convenient answer that failed"*
- **18.10** Colossians 2 — shadow and body
- **19 / 20** Sabbath (creation, covenant sign, shadow, rest); Hebrews 4 and `sabbatismos`
- **21 / 21½** Who are the people of God — then **Recentering the Map**, an orientation stage that freezes the project's actual destination
- **22** Romans 9, read as an argument rather than a slogan — explicitly *not* backward through Romans 11, Calvinism, replacement theology, or dispensationalism

**Key decisions (three new ADRs):**
- **ADR-0008** — source-language-first localization. Stop carrying three English translations through every tranche; research once at the Greek/Hebrew level, ESV+CJB as default English witnesses, RVR1960 pulled selectively against four named triggers. The Spanish manuscript gets localized *from the research*, never translated from the English manuscript.
- **ADR-0009** — three content provenance layers: Main Argument / ✍️ Manuscript Voice / 🔬 Researcher's Commentary. The third exists to preserve *how* a conclusion was earned, including failed explanations. Orthogonal to ADR-0006, not a replacement.
- **ADR-0010** — unabridged research preservation. Three artifacts (research record / structured vault / manuscript) with three different requirements. Its load-bearing clause: **never collapse evidence types** — "contextually favored" must not become "lexically established", "plausible" must not become "proven", "unverified" must not become "false". Direct response to Mars: *"I want the complete unabridged version… even if it does come out to be the book explaining the book."*

**Method changes that came out of real failures:**
- **Extrabiblical Source Protocol** — after prematurely declaring "VERIFICATION FAILED" on 1 Enoch from a single 403. Material was fully verifiable; took four attempts (sacred-texts 403 → archive.org 404 → Wikisource index, TOC-only → Wikisource chapter pages ✅). Now a formal rule, and extracted to KodeArk.
- **Thesis Discipline**, locked at Stage 21½ — preterism is a hypothesis under test, never the premise. Same for "Messianic Israelite": text → synthesis → label, never label → text.
- **Methodology integrity audit** — ran grep-verified counts instead of asserting compliance. It found a real defect (a stale `*(current)*` marker on Stage 12), fixed separately as `3feaec9`. Asserting integrity would have missed it.

**Findings worth their own line:**
- **Translation divergence is now a systematic finding, not an anecdote.** Five passages where an English rendering has been quoted to this project as though it were the verse: Mark 7:19 (`katharizōn` is a participle with no stated subject; RVR1960 alone preserves the ambiguity), Colossians 2:14 (`cheirographon`, *not* `nomos` — "the Torah was nailed to the cross" substitutes a noun Paul didn't write), Hebrews 4:9 (`sabbatismos` — ESV "Sabbath rest" = a state, CJB "Shabbat-keeping" = an observance), Ephesians 2:15, Romans 9:22. **The recurrence itself is the finding.**
- **Five CJB versification offsets confirmed:** Jeremiah 31 (+1), Zechariah 2:6, Psalms superscription (+1), Hosea 2:11→2:13 (+2), Hosea 1:10→2:1.
- **Lexical escalation, run twice, opposite outcomes** — `sabbatismos` produced a documented *gap* (Thayer's cites Plutarch §3; Sabbath material found at §8, English only, Greek unconfirmed → recorded REPORTED, NOT VERIFIED). Romans 9:22–23 *succeeded*: κατηρτισμένα = perfect participle, middle **or** passive, no stated agent; προητοίμασεν = aorist **active**, God as subject. The asymmetry is established; **what it means is explicitly not.**

**Corrections made to my own earlier work** (kept, per ADR-0010, rather than silently overwritten):
- Stage 16 §9's *"yesterday's offering did not finish anything"* — overreached; Leviticus 4:20 says atonement was made and they *were* forgiven
- Stage 18 §23's *"extends well beyond avoiding Levitically unclean animals"* — true of the behavior, misleading about the reason (Daniel 1)
- Stage 18.8's accommodation framing — downgraded; paying expenses for four men is substantive, not theater
- Messiah as the final "sin offering" — too narrow; also `asham`, Yom Kippur, Passover, and He is simultaneously the priest

**Scale:** 35 files in `03-Theology/Eschatology-Framework/`, 10 ADRs, 61 numbered open questions + 24 bookmarks.

**Deferred:** BIBLE-04g (methodology backfill of Stages 1–12) — deliberately *not now* and *not at the end*; run once methodology stabilizes, before the manuscript foundation locks. Scope extended this session to also recover Researcher's Commentary.

**Next:** Stage 23 — Romans 10. Explicitly framed as **the strongest text against the project's original position**, to be run at directly rather than avoided.

**KodeArk extraction:** `07-Lessons/one-blocked-source-is-not-verification-failure.md` (`9ad0497`) — generalized the 1 Enoch incident into a source-ladder discipline for any citation/spec verification.

**Tests:** n/a (vault, no code)

**Commits:** `8933bef` `db9ea5b` `5302f71` `81a8736` `35171d8` `411b108` `3d8ba8b` `d7384b0` `3bd3bb1` `26338b7` `a8e60cd` `632df3c` `834ad85` `4530379` `2b2fae6` `628784d` `042b963` `cdeb6d6` `df3907a` `b298eea` (+ `3feaec9` stale-marker fix)

---
