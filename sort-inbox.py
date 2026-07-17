#!/usr/bin/env python3
"""
BIBLE Vault — Inbox Sorter
Run: python3 sort-inbox.py

Routes 00-Inbox files to the correct destination based on:
  1. frontmatter `status` field (always wins)
     - archived  → 06-Archive/
  2. frontmatter `category` or `type` field
  3. filename prefix  (book--slug.md  or  category--slug.md)
  4. no match → stays in inbox for manual review

Pipeline folders:
  01-Old-Testament/
    01-Pentateuch/     — Genesis through Deuteronomy
    02-Historical/     — Joshua through Esther
    03-Wisdom/         — Job, Psalms, Proverbs, Ecclesiastes, Song of Solomon
    04-Prophets/       — Isaiah through Malachi
  02-New-Testament/
    01-Gospels/        — Matthew, Mark, Luke, John
    02-Acts/
    03-Pauline-Epistles/   — Romans through Philemon
    04-General-Epistles/   — Hebrews through Jude
    05-Revelation/
  03-Theology/         — Doctrine, systematic theology
  04-Characters/       — Bible people studies
  05-References/       — Maps, concordances, study tools
  06-Archive/          — Completed or superseded notes
"""

import os
import re
import shutil

VAULT = os.path.dirname(os.path.abspath(__file__))
INBOX = os.path.join(VAULT, '00-Inbox')

OT = '01-Old-Testament'
NT = '02-New-Testament'

# Frontmatter status: only 'archived' forces a destination.
# 'inbox' and 'active' fall through to prefix/category routing.
STATUS_OVERRIDE = {
    'archived': '06-Archive',
}

# Frontmatter category/type → top-level folder fallback
# Used when prefix matching doesn't fire.
CATEGORY_MAP = {
    'old-testament': OT,
    'new-testament': NT,
    'theology': '03-Theology',
    'character': '04-Characters',
    'reference': '05-References',
}

TYPE_MAP = {
    'study': None,           # not enough information — needs prefix or category
    'theology': '03-Theology',
    'devotional': None,      # keep in inbox for manual review
    'character': '04-Characters',
    'reference': '05-References',
}

# Filename prefix → destination folder (relative to VAULT)
# Order matters: more specific rules first.
PREFIX_RULES = [
    # ── Old Testament ──────────────────────────────────────────
    # Pentateuch
    (['genesis--', 'exodus--', 'leviticus--', 'numbers--', 'deuteronomy--'],
     os.path.join(OT, '01-Pentateuch')),
    # Historical books
    (['joshua--', 'judges--', 'ruth--',
      '1samuel--', '2samuel--', '1kings--', '2kings--',
      '1chronicles--', '2chronicles--',
      'ezra--', 'nehemiah--', 'esther--'],
     os.path.join(OT, '02-Historical')),
    # Wisdom literature
    (['job--', 'psalm--', 'psalms--', 'proverbs--',
      'ecclesiastes--', 'song-of-solomon--', 'song--'],
     os.path.join(OT, '03-Wisdom')),
    # Prophets
    (['isaiah--', 'jeremiah--', 'lamentations--', 'ezekiel--', 'daniel--',
      'hosea--', 'joel--', 'amos--', 'obadiah--', 'jonah--', 'micah--',
      'nahum--', 'habakkuk--', 'zephaniah--', 'haggai--',
      'zechariah--', 'malachi--'],
     os.path.join(OT, '04-Prophets')),
    # General OT catch-all prefix
    (['old-testament--', 'ot--'],
     OT),

    # ── New Testament ──────────────────────────────────────────
    # Gospels (john-- must come before 1john-- / 2john-- / 3john--)
    (['matthew--', 'mark--', 'luke--', 'john--'],
     os.path.join(NT, '01-Gospels')),
    # Acts
    (['acts--'],
     os.path.join(NT, '02-Acts')),
    # Pauline Epistles
    (['romans--',
      '1corinthians--', '2corinthians--',
      'galatians--', 'ephesians--', 'philippians--', 'colossians--',
      '1thessalonians--', '2thessalonians--',
      '1timothy--', '2timothy--', 'titus--', 'philemon--'],
     os.path.join(NT, '03-Pauline-Epistles')),
    # General Epistles (1john/2john/3john must NOT match john-- above — prefix is different)
    (['hebrews--', 'james--', '1peter--', '2peter--',
      '1john--', '2john--', '3john--', 'jude--'],
     os.path.join(NT, '04-General-Epistles')),
    # Revelation
    (['revelation--', 'rev--'],
     os.path.join(NT, '05-Revelation')),
    # General NT catch-all prefix
    (['new-testament--', 'nt--'],
     NT),

    # ── Thematic / functional ──────────────────────────────────
    (['theology--', 'doctrine--', 'systematic--', 'doctrinal--'],
     '03-Theology'),
    (['character--', 'abraham--', 'moses--', 'david--', 'solomon--',
      'elijah--', 'elisha--', 'isaiah--character', 'daniel--character',
      'jesus--', 'peter--', 'paul--', 'john-the-baptist--',
      'mary--', 'joseph--', 'esther--character', 'ruth--character'],
     '04-Characters'),
    (['reference--', 'concordance--', 'map--', 'maps--',
      'dictionary--', 'lexicon--', 'study-tool--', 'timeline--'],
     '05-References'),
]


def read_frontmatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    fm = {}
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, _, v = line.partition(':')
                fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def route_file(fname, fm):
    # 1. Status override — archived always wins
    status = fm.get('status', 'inbox').strip()
    if status in STATUS_OVERRIDE:
        return STATUS_OVERRIDE[status]

    # 2. Filename prefix — most specific signal
    for prefixes, folder in PREFIX_RULES:
        for p in prefixes:
            if fname.startswith(p):
                return folder

    # 3. Frontmatter category
    category = fm.get('category', '').strip().lower()
    # category field may be pipe-separated (e.g. "old-testament | new-testament")
    for part in re.split(r'[|,]', category):
        key = part.strip()
        if key in CATEGORY_MAP and CATEGORY_MAP[key]:
            return CATEGORY_MAP[key]

    # 4. Frontmatter type
    note_type = fm.get('type', '').strip().lower()
    if note_type in TYPE_MAP and TYPE_MAP[note_type]:
        return TYPE_MAP[note_type]

    # 5. No clear destination — leave in inbox
    return None


def main():
    if not os.path.isdir(INBOX):
        print(f'Inbox not found: {INBOX}')
        return

    moved = []
    stayed = []

    for fname in sorted(os.listdir(INBOX)):
        if not fname.endswith('.md'):
            continue
        src = os.path.join(INBOX, fname)
        fm = read_frontmatter(src)
        dest_folder = route_file(fname, fm)

        if dest_folder:
            dest_dir = os.path.join(VAULT, dest_folder)
            os.makedirs(dest_dir, exist_ok=True)
            dst = os.path.join(dest_dir, fname)
            shutil.move(src, dst)
            moved.append((fname, dest_folder))
        else:
            stayed.append(fname)

    if moved:
        print(f'Sorted {len(moved)} file(s):')
        for fname, folder in moved:
            print(f'  {fname}  →  {folder}/')
    else:
        print('Nothing to sort.')

    if stayed:
        print(f'\n{len(stayed)} file(s) need a prefix or frontmatter category to be sorted:')
        for fname in stayed:
            print(f'  {fname}')


if __name__ == '__main__':
    main()
