# BIBLE Vault — Audit Conventions

Used by `vault-audit` to enforce quality standards for this vault.
This vault contains Bible study notes, theological research, and character studies.

---

## Valid Status Values

| Status | Meaning |
|--------|---------|
| `inbox` | Raw capture or stub |
| `seedling` | Initial notes, early study |
| `growing` | Being developed with cross-references |
| `evergreen` | Complete, well-cross-referenced |
| `reference` | Static reference material (concordance entries, etc.) |

**Progression:** `inbox` → `seedling` → `growing` → `evergreen`

---

## Required Frontmatter Fields

All notes must have:
- `title`
- `date` (or `captured`)
- `status`
- `category`
- `tags`

---

## Valid Categories

| Category | Folder |
|----------|--------|
| `old-testament` | 01-Old-Testament |
| `new-testament` | 02-New-Testament |
| `theology` | 03-Theology |
| `characters` | 04-Characters |
| `references` | 05-References |
| `inbox` | 00-Inbox |

---

## Naming Convention

`{category}--{slug}.md`

Examples:
```
theology--grace-and-justification.md
characters--paul-apostle-overview.md
old-testament--psalms-23-study.md
new-testament--sermon-on-the-mount.md
```

---

## FAIL Conditions (block session close)

- Missing `title` or `date`/`captured`
- No frontmatter block at all

---

## WARN Conditions (flag, offer to fix)

- `status: inbox` with substantive content (should be promoted)
- `tags: []` — theological topics benefit from tags for cross-referencing
- `category` missing or blank
- Character or passage notes with no scripture references in body

---

## Exclusions

Do not audit:
- `docs/` — governance files
- `_templates/` — templates
- `06-Archive/` — archived notes, relaxed standards
- `README.md`, `CLAUDE.md`, `SESSION-LOG.md`

---

## Note

`source` field is not required for personal Bible study notes — the source is the scripture itself. Scripture references in the note body serve as the citation.
