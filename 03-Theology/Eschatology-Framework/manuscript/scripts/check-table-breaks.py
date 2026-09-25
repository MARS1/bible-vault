#!/usr/bin/env python3
"""LAYOUT-003 gate: table rows must never split across a page.

Governed by ADR-0012 (docs/adr): rendered-layout integrity is part of build
correctness. This is the first gate implementing it.

Text extraction cannot see this defect -- pdftotext reports a split row as
complete, because every word is present. So this renders the Part's clean
markdown the same way build-manuscript.py does, then walks WeasyPrint's own
laid-out page boxes and reports:

  SPLIT ROW         a body <tr> whose boxes land on more than one page  -> FAIL
  ORPHAN HEADER     a page whose last table content is a header row     -> FAIL
  CONTINUED TABLE   a header repeated on a continuation page            -> fine
  TABLE PAGES       every page carrying a table, for visual inspection

Called by build-manuscript.py after every render. Also runnable alone:
  check-table-breaks.py _build/en/part-07-en-clean.md [--lang en]

Validated 2026-09-25 against the Part VII d1-integrity2 render the author had
reviewed: it found the two split rows the review reported, including the
scorecard row stranded across pp. 49-50. Exit status 1 on any FAIL.

KEEP THE HTML ASSEMBLY BELOW IN STEP WITH render() IN build-manuscript.py.
If the two drift, this checks a layout that is not the one being printed.
"""
import argparse, subprocess, sys
from collections import defaultdict
from pathlib import Path

import weasyprint

CSS = Path(__file__).resolve().parent / "design-system-v1.css"


def layout(md, lang):
    frag = subprocess.run(["pandoc", str(md), "-f", "markdown+fenced_divs", "-t", "html5"],
                          capture_output=True, text=True, check=True).stdout
    frag = frag.replace("︎", "")          # as render() does -- LAYOUT-004
    html = (f'<!doctype html>\n<html lang="{lang}"><head><meta charset="utf-8">'
            f"<style>{CSS.read_text()}</style></head><body>\n{frag}\n</body></html>\n")
    return weasyprint.HTML(string=html).render()


def walk(box):
    yield box
    for child in getattr(box, "children", None) or []:
        yield from walk(child)


def check(md, lang="en"):
    doc = layout(md, lang)
    pages, text, head = defaultdict(set), {}, {}
    table_pages, orphans = set(), []
    for n, page in enumerate(doc.pages, 1):
        last = None
        for b in walk(page._page_box):
            if type(b).__name__ != "TableRowBox" or b.element is None:
                continue
            k = id(b.element)
            pages[k].add(n)
            table_pages.add(n)
            text.setdefault(k, " ".join("".join(b.element.itertext()).split())[:80])
            cells = list(b.element)
            head[k] = bool(cells) and all(c.tag == "th" for c in cells)
            last = "head" if head[k] else "body"
        if last == "head":
            orphans.append(n)
    splits = sorted((sorted(p), text[k]) for k, p in pages.items() if len(p) > 1 and not head[k])
    repeats = sum(1 for k, p in pages.items() if len(p) > 1 and head[k])
    return len(doc.pages), sorted(table_pages), splits, orphans, repeats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("--lang", default="en")
    a = ap.parse_args()
    n, tp, splits, orphans, repeats = check(a.md, a.lang)
    ok = not splits and not orphans
    print(f"     table layout: {len(splits)} split rows, {len(orphans)} orphan headers, "
          f"{repeats} continued with header, {len(tp)} table pages  " + ("OK" if ok else "<-- CHECK"))
    for pg, t in splits:
        print(f"       SPLIT ROW pp. {pg}: {t}")
    for pg in orphans:
        print(f"       ORPHAN HEADER at foot of p. {pg}")
    print(f"       table pages: {', '.join(map(str, tp))}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
