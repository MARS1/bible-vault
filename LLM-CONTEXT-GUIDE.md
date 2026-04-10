---
created: 2026-04-10
---

# Bible Vault — LLM Context

This vault belongs to Marcelo Mario Berta (Mars).
It stores Bible study notes, theological insights, and spiritual reflections.

## Purpose

Deep Bible study and theological reflection. This vault captures:
- Scripture study and commentary
- Theological concepts and doctrine
- Character studies from the Bible
- Practical application and devotional thoughts

## Bible Categories

| Folder | What goes here |
|--------|----------------|
| `01-Old-Testament/` | Pentateuch, Historical Books, Wisdom Literature, Prophets |
| `02-New-Testament/` | Gospels, Acts, Epistles, Revelation |
| `03-Theology/` | Systematic theology, doctrine, theological concepts |
| `04-Characters/` | People studies — Abraham, Moses, David, Paul, Jesus, etc. |
| `05-References/` | Cross-references, maps, concordances, study tools |
| `06-Archive/` | Deduplicated or superseded notes |

## Old Testament Structure

Within `01-Old-Testament/`, organize by section:
- `01-Pentateuch/` — Genesis, Exodus, Leviticus, Numbers, Deuteronomy
- `02-Historical/` — Joshua through Esther
- `03-Wisdom/` — Job, Psalms, Proverbs, Ecclesiastes, Song of Solomon
- `04-Prophets/` — Isaiah through Malachi

## New Testament Structure

Within `02-New-Testament/`, organize by section:
- `01-Gospels/` — Matthew, Mark, Luke, John
- `02-Acts/`
- `03-Pauline-Epistles/` — Romans through Philemon
- `04-General-Epistles/` — Hebrews through Jude
- `05-Revelation/`

## Cross-Vault Queries

- **MARS-LIFE** — personal spiritual journey and devotional life
- **MARKETING** — integrating faith into business and work
- **KodeArk** — for any theological frameworks referenced in projects

## Current Focus

- Building systematic study framework
- Identifying key theological themes
- Cross-referencing Old and New Testament

## Frontmatter Standard

All new notes use YAML frontmatter:

```yaml
---
title: Descriptive title
type: study | theology | devotional | character | reference
category: old-testament | new-testament | theology | character
tags: []
reference: Genesis 1:1 | Romans 3:23 | etc.
created: YYYY-MM-DD
status: inbox | active | archived
related: "[[other-note]]"
---

# Title

## Scripture

[Relevant Bible passages]

## Notes

[Study notes, commentary, insights]

## Application

[Practical application]

## Related

- [[]]
```

**File naming:** Book chapter format or descriptive title
- Book study: `genesis--chapter-01.md`, `psalm-023.md`
- Character study: `abraham--father-of-faith.md`
- Theology: `doctrine-of-grace.md`
