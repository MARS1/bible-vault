#!/usr/bin/env python3
"""Proof checks on an assembled book PDF (BIBLE-493 step 3).

    python3 scripts/proof-check.py _build/book/book-en.pdf --lang en

Reports, page by page:
  SPLIT    a word broken across a line end with no hyphen (WeasyPrint splits
           italic or Hebrew words nested in bold; found in Appendix F, 2026-10-18)
  STRANDED a heading or short bold label as the last line of a page, cut off
           from what it introduces (the "20:7" labels in Appendix C)
  BLANK    a page with no text that is not one of the deliberate plain pages
  MOJIBAKE encoding damage
Text is compared against the words of the source files, so a break that leaves
two real words (an ordinary line end) is not reported.
"""
import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def words_in_sources(lang):
    words = set()
    files = list((ROOT / lang).glob("*.md")) + list((ROOT / "matter-drafts" / lang).glob("*.md"))
    for f in files:
        t = re.sub(r"<[^>]+>", " ", f.read_text(encoding="utf-8"))
        for w in re.findall(r"[^\W\d_]+", t):
            words.add(unicodedata.normalize("NFC", w).lower())
    return words


def headings_in_sources(lang):
    heads = set()
    files = list((ROOT / lang).glob("*.md")) + list((ROOT / "matter-drafts" / lang).glob("*.md"))
    for f in files:
        for ln in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"#{2,4} (.+)", ln) or re.match(r"\*\*([^*]{1,40})\*\*\s*$", ln)
            if m:
                h = re.sub(r"[*_`{}#]|<[^>]+>|\{[^}]*\}", "", m.group(1)).strip()
                if h:
                    heads.add(re.sub(r"\s+", " ", h).lower())
    return heads


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--lang", default="en")
    a = ap.parse_args()
    raw = subprocess.run(["pdftotext", a.pdf, "-"], capture_output=True, text=True).stdout
    pages = raw.split("\f")
    known = words_in_sources(a.lang)
    heads = headings_in_sources(a.lang)
    found = {"SPLIT": [], "STRANDED": [], "BLANK": [], "MOJIBAKE": []}

    for pno, pg in enumerate(pages, 1):
        if any(x in pg for x in ("â€", "�", "Ã")):
            found["MOJIBAKE"].append((pno, ""))
        lines = [ln.strip() for ln in pg.splitlines() if ln.strip()]
        if not lines and pno < len(pages):
            found["BLANK"].append((pno, ""))
            continue
        for i in range(len(lines) - 1):
            a_ln, b_ln = lines[i], lines[i + 1]
            if a_ln.endswith(("‐", "-", "­")):
                continue
            ma = re.search(r"([^\W\d_]+)$", a_ln)
            mb = re.match(r"([^\W\d_]+)", b_ln)
            if not ma or not mb:
                continue
            left, right = ma.group(1), mb.group(1)
            joined = unicodedata.normalize("NFC", left + right).lower()
            l_ok = unicodedata.normalize("NFC", left).lower() in known
            r_ok = unicodedata.normalize("NFC", right).lower() in known
            if joined in known and not (l_ok and r_ok):
                found["SPLIT"].append((pno, f"{left}|{right}"))
        # last text line on the page (ignore a trailing page number)
        body = [ln for ln in lines if not re.fullmatch(r"\d{1,4}", ln)]
        if body:
            last = re.sub(r"\s+", " ", body[-1]).lower()
            if last in heads or re.fullmatch(r"\d{1,2}:\d{1,3}", last):
                found["STRANDED"].append((pno, body[-1][:60]))

    for k, v in found.items():
        print(f"{k:9} {len(v)}")
        for pno, s in v[:40]:
            print(f"   p.{pno}  {s}")
    sys.exit(1 if any(found[k] for k in ("SPLIT", "MOJIBAKE")) else 0)


if __name__ == "__main__":
    main()
