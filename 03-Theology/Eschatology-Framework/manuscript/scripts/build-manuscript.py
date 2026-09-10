#!/usr/bin/env python3
"""Build reader-facing and ChatGPT-facing outputs from the Draft 1 chapter files.

Source of truth stays the per-chapter markdown in manuscript/en/.
This script never edits it. It only produces derived artifacts in manuscript/_build/.

  python3 build-manuscript.py --part 1
  python3 build-manuscript.py --all
  python3 build-manuscript.py --part 1 --no-pdf
"""
import argparse, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN, BUILD = ROOT / "en", ROOT / "_build"

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

        if a.no_pdf:
            continue
        html = BUILD / f"part-{p:02d}.html"
        subprocess.run(["pandoc", str(clean), "-f", "markdown", "-t", "html5",
                        "--standalone", "--metadata", f"title={title}",
                        "-o", str(html)], check=True)
        html.write_text(html.read_text().replace("</head>", f"<style>{CSS}</style></head>"))
        pdf = BUILD / f"part-{p:02d}.pdf"
        subprocess.run(["weasyprint", "-e", "utf-8", str(html), str(pdf)], check=True)
        print(f"PDF  {pdf.relative_to(ROOT)}  ({pdf.stat().st_size//1024} KB)")

        # verification: a clean exit code is not proof the render is correct
        try:
            txt = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
            bad = sum(txt.count(m) for m in ("â€", "�", "Ã"))
            print(f"     verify: {len(txt.split()):,} words extracted, {bad} mojibake markers "
                  + ("OK" if bad == 0 else "<-- BROKEN"))
        except FileNotFoundError:
            print("     verify: SKIPPED, pdftotext not installed")

if __name__ == "__main__":
    main()
