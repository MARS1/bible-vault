# BIBLE Vault

> Bible study vault — Scripture, theology, commentary, and spiritual growth.
> AI context file for all AI assistants.

**Type:** Obsidian vault — research and personal study

## Notion

**Bible Notion:** https://www.notion.so/Bible-33e3d8e1370080ca8bffde572463c38a
**All project Notion URLs:** See `KodeArk/notion-directories.md`

## Location

`/Volumes/VM/OBSIDIAN/BIBLE/`

## Structure

| Folder | Purpose |
|--------|---------|
| `00-Inbox/` | Raw captures, quick notes, devotional thoughts |
| `01-Old-Testament/` | Old Testament books, commentary, notes |
| `02-New-Testament/` | New Testament books, commentary, notes |
| `03-Theology/` | Doctrine, theology, systematic study |
| `04-Characters/` | Bible people — studies, timelines, relationships |
| `05-References/` | Cross-references, maps, dictionaries, tools |
| `06-Archive/` | Completed or superseded notes |
| `_templates/` | Note templates |

## Rules

- NEVER create files unless explicitly asked
- Prefer editing existing files over creating new ones
- Use `[[wiki links]]` for internal cross-references
- Follow the frontmatter standard in LLM-CONTEXT-GUIDE.md
- Cross-reference with [[MARKETING]], [[MARS-LIFE]] for spiritual/practical integration


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->

## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- For cross-module "how does X relate to Y" questions, prefer `graphify query "<question>"`, `graphify path "<A>" "<B>"`, or `graphify explain "<concept>"` over grep — these traverse the graph's EXTRACTED + INFERRED edges instead of scanning files
- After modifying code files in this session, run `graphify update .` to keep the graph current (AST-only, no API cost)
