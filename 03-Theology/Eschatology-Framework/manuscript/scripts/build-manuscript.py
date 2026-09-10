#!/usr/bin/env python3
"""Build reader-facing and ChatGPT-facing outputs from the Draft 1 chapter files.

Source of truth stays the per-chapter markdown in manuscript/en/.
This script never edits it. It only produces derived artifacts in manuscript/_build/.

  python3 build-manuscript.py --part 1
  python3 build-manuscript.py --all
  python3 build-manuscript.py --part 1 --no-pdf
"""
import argparse, re, subprocess, sys
try:
    import pypdf
except ImportError:
    pypdf = None
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN, BUILD = ROOT / "en", ROOT / "_build"

# Human-readable drop. Derived artifacts only. The vault stays the source of
# truth; nothing here is ever edited in place or read back into the manuscript.
READER_DIR = Path("/Users/MARS/Desktop/7-MARS/Bible Study")

PARTS = {
    1: ("Part I: The Question That Would Not Stay Small",
        ["00a-foreword", "00b-a-note-to-the-reader", "ch01-", "ch02-", "ch03-", "ch04-", "ch05-", "ch06-"]),
}

def strip_frontmatter(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text

def declutter(text):
    """Remove vault-only syntax that means nothing outside Obsidian."""
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)   # [[target|label]] -> label
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)              # [[target]] -> target
    return text

def collect(part):
    title, order = PARTS[part]
    files = []
    for prefix in order:
        hits = sorted(EN.glob(prefix + "*.md"))
        if not hits:
            sys.exit(f"MISSING: no file matching {prefix}* in {EN}")
        files.extend(hits)
    return title, files

CSS = """
@page { size: 6in 9in; margin: 0.75in 0.7in 0.85in 0.7in;
        @bottom-center { content: counter(page); font-family: Georgia, serif; font-size: 9pt; color: #555; } }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 11pt; line-height: 1.55; color: #1a1a1a; hyphens: auto; }
h1 { font-size: 17pt; margin: 0 0 1.1em; line-height: 1.25; page-break-before: always; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 12.5pt; margin: 2em 0 0.6em; font-weight: normal; font-style: italic; }
p { margin: 0 0 0.75em; text-align: justify; }
blockquote { margin: 1.1em 1.4em; padding-left: 0.9em; border-left: 2px solid #bbb; font-style: italic; color: #333; }
blockquote p { text-align: left; }
hr { border: none; border-top: 1px solid #ccc; margin: 1.8em 4em; }
strong { font-weight: 600; }
.parttitle { page-break-before: always; text-align: center; margin-top: 34%; }
.parttitle h1 { page-break-before: avoid; font-size: 22pt; font-style: italic; }
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--no-pdf", action="store_true")
    ap.add_argument("--no-drop", action="store_true", help="skip copying to the reader directory")
    a = ap.parse_args()
    parts = sorted(PARTS) if a.all else ([a.part] if a.part in PARTS else sys.exit("use --part N or --all"))
    BUILD.mkdir(exist_ok=True)

    for p in parts:
        title, files = collect(p)
        chunks = [declutter(strip_frontmatter(f.read_text())).strip() for f in files]
        words = sum(len(c.split()) for c in chunks)

        clean = BUILD / f"part-{p:02d}-clean.md"
        clean.write_text(f"# {title}\n\n*Draft 1. {words:,} words.*\n\n" + "\n\n---\n\n".join(chunks) + "\n")
        print(f"MD   {clean.relative_to(ROOT)}  ({words:,} words, {len(files)} files)")

        if not a.no_drop and READER_DIR.is_dir():
            (READER_DIR / clean.name).write_bytes(clean.read_bytes())
            print(f"     -> {READER_DIR / clean.name}")

        if a.no_pdf:
            continue
        # Deliberately NOT --standalone. Pandoc's default template injects its own
        # boilerplate CSS, which this script overwrites anyway, and which WeasyPrint
        # then emits half a dozen warnings about. Take the body fragment and wrap it.
        html = BUILD / f"part-{p:02d}.html"
        frag = subprocess.run(["pandoc", str(clean), "-f", "markdown", "-t", "html5"],
                              capture_output=True, text=True, check=True).stdout
        html.write_text(f"<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
                        f"<title>{title}</title><style>{CSS}</style></head><body>\n{frag}\n</body></html>\n")
        pdf = BUILD / f"part-{p:02d}.pdf"
        subprocess.run(["weasyprint", "-e", "utf-8", str(html), str(pdf)], check=True)
        print(f"PDF  {pdf.relative_to(ROOT)}  ({pdf.stat().st_size//1024} KB)")

        # Verification. A clean exit code from WeasyPrint is not proof the render is
        # correct, so read the finished PDF back and check it against the source.
        try:
            raw = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
            txt = re.sub(r"^\s*\d+\s*$", "", raw, flags=re.M)      # drop page numbers
            flat = re.sub(r"\s+", " ", txt)                        # headings wrap; normalize
            got = len(txt.split())
            bad = sum(raw.count(m) for m in ("â€", "\ufffd", "Ã"))
            missing = [f.stem for f in files
                       if re.sub(r"\s+", " ", declutter(strip_frontmatter(f.read_text()))
                                 .strip().split("\n", 1)[0].lstrip("# ")) not in flat]
            pages = len(pypdf.PdfReader(str(pdf)).pages) if pypdf else "?"
            ok = bad == 0 and not missing and abs(got - words) < words * 0.02
            print(f"     verify: {pages} pages, {got:,}/{words:,} words recovered, "
                  f"{bad} mojibake, {len(missing)} sections missing  "
                  + ("OK" if ok else "<-- CHECK"))
            for m in missing:
                print(f"       MISSING SECTION: {m}")
        except FileNotFoundError:
            print("     verify: SKIPPED, pdftotext not installed")

        if not a.no_drop:
            if READER_DIR.is_dir():
                (READER_DIR / pdf.name).write_bytes(pdf.read_bytes())
                print(f"     -> {READER_DIR / pdf.name}")
            else:
                print(f"     drop SKIPPED, no such directory: {READER_DIR}")

if __name__ == "__main__":
    main()
