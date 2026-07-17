# Graph Report - BIBLE  (2026-07-17)

## Corpus Check
- 1 files · ~9,429 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 22 nodes · 24 edges · 4 communities detected
- Extraction: 21% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]

## God Nodes (most connected - your core abstractions)
1. `main()` - 3 edges
2. `read_frontmatter()` - 2 edges
3. `route_file()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Scripture Study & Analysis` ----> `Old Testament`  [1.0]
   →   _Bridges community 0 → community 2_
- `Scripture Study & Analysis` ----> `New Testament`  [1.0]
   →   _Bridges community 0 → community 1_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.38
Nodes (7): Bible Study Vault, Character Study, Cross-References & Tools, Devotional Practice & Reflection, Scripture Study & Analysis, Systematic Theology, Theology & Doctrine

### Community 1 - "Community 1"
Cohesion: 0.33
Nodes (6): Acts, General Epistles (Hebrews-Jude), Gospels (Matthew, Mark, Luke, John), New Testament, Pauline Epistles (Romans-Philemon), Revelation

### Community 2 - "Community 2"
Cohesion: 0.4
Nodes (5): Historical Books (Joshua-Esther), Old Testament, Pentateuch (Genesis-Deuteronomy), Prophetic Books (Isaiah-Malachi), Wisdom Books (Job, Psalms, Proverbs, Ecclesiastes, Song)

### Community 3 - "Community 3"
Cohesion: 0.83
Nodes (3): main(), read_frontmatter(), route_file()

## Suggested Questions
_Not enough signal to generate questions. This usually means the corpus has no AMBIGUOUS edges, no bridge nodes, no INFERRED relationships, and all communities are tightly cohesive. Add more files or run with --mode deep to extract richer edges._