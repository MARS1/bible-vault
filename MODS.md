# MODS — BIBLE Vault Config

## Location

| Location | Role |
|---|---|
| `/Volumes/VM/OBSIDIAN/BIBLE/` | Canonical Obsidian vault — Bible study |

## Notion

| Page | URL | Purpose |
|------|-----|---------|
| Bible root | https://www.notion.so/Bible-33e3d8e1370080ca8bffde572463c38a | Main Bible workspace |
| Inbox (links to extract) | https://www.notion.so/33e3d8e1370080d39a8ef1cc529b02dc | Drop URLs here to process |
| Outbox (processed links) | https://www.notion.so/33e3d8e137008087a3d7ec04049b6e3e | Archive of extracted content |

**Workflow:** Drop links into Notion Inbox. Run `/content-extract` — skill reads Inbox, processes all links, archives each when done.

## Allowed Actions — No Permission Needed

Run the following without asking MARS for confirmation:

- Read/write files inside `/Volumes/VM/OBSIDIAN/BIBLE/`
- Read files inside `/Volumes/VM/OBSIDIAN/KodeArk/` (cross-reference)

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

## Autonomy & Direct Action

- When you have direct tool access (SSH, git, Airtable MCP, Notion MCP, Bash), USE IT — do not ask the user to run manual terminal commands, paste URLs, or perform UI actions you could do yourself
- Never commit code changes without explicit user approval — stage, show diff, summarize, then wait
- For OAuth/auth links, open in Brave (not Chrome) — never ask user to open the browser manually
- When stuck after 2–3 search attempts, STOP and ask rather than continuing to grep blindly
- When a session type has an existing skill (`/content-extract`, `/session-close`, etc.), USE THE SKILL — do not write custom scripts

## Do Not

- Create new top-level directories without asking MARS
- Commit `.env` files or secrets
