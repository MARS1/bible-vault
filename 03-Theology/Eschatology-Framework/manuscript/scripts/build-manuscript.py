#!/usr/bin/env python3
"""Build reader-facing and review-facing outputs for the manuscript.

Governed by ADR-0011 (manuscript production architecture) in docs/adr/.
The three non-obvious behaviors below are decisions recorded there, not
implementation details: snapshots refuse to overwrite, Spanish is a sibling
edition rather than a translation, and appearance lives in the stylesheet
rather than in the prose.

Canonical source is manuscript/<lang>/, one file per chapter. This script never
edits it. Everything it writes is derived.

  build-manuscript.py --part 1                      # English, current build
  build-manuscript.py --part 1 --lang es            # Spanish
  build-manuscript.py --part 1 --snapshot d1-initial
  build-manuscript.py --all --lang en

_build/  is disposable and gets overwritten.
_snapshots/ is permanent. A snapshot records the git commit it came from and
refuses to overwrite an existing milestone, because the whole point of a
snapshot is that you can still open the exact thing that was reviewed.
"""
import argparse, re, shutil, subprocess, sys
from datetime import date
from pathlib import Path
try:
    import pypdf
except ImportError:
    pypdf = None

ROOT = Path(__file__).resolve().parent.parent
BUILD, SNAPS = ROOT / "_build", ROOT / "_snapshots"
READER = Path("/Users/MARS/Desktop/7-MARS/Bible Study")

LANGS = {
    "en": {"dir": "en", "label": "English", "reader": "en", "part_word": "Part"},
    "es": {"dir": "es", "label": "Español", "reader": "es", "part_word": "Parte"},
}

PARTS = {
    "en": {1: ("Part I: The Question That Would Not Stay Small",
               ["00a-", "00b-", "ch01-", "ch02-", "ch03-", "ch04-", "ch05-", "ch06-"]),
           2: ("Part II: The Olivet Discourse, Read in Its Own Century",
               ["ch07-", "ch08-", "ch09-", "ch10-", "ch11-", "ch12-"]),
           3: ("Part III: What the New Covenant Actually Changed",
               ["ch13-", "ch14-", "ch15-", "ch16-", "ch17-", "ch18-", "ch19-"])},
    "es": {1: ("Parte I: La pregunta que no se quedó pequeña",
               ["00a-", "00b-", "ch01-", "ch02-", "ch03-", "ch04-", "ch05-", "ch06-"]),
           2: ("Parte II: El discurso del Monte de los Olivos, leído en su propio siglo",
               ["ch07-", "ch08-", "ch09-", "ch10-", "ch11-", "ch12-"])},
}

CSS = (Path(__file__).resolve().parent / "design-system-v1.css").read_text()

# Spanish register standard. Kept in step with ES-REGISTER.md, which is the
# document; this is the enforcement. Add a row there, add a pattern here.
ES_REGISTER = [
    (r"\bac[áa]\b", "aquí"),
    (r"demasiado chic[oa]", "demasiado pequeño"),
    (r"despareja", "desigual  /  no ... por igual"),
    (r"\bdarse vuelta\b", "volverse"),
    (r"est[áa] por [a-z]+r\b", "está a punto de ..."),
    (r"apretaba", "presionaba"),
    (r"quedaron con el lugar", "se apoderaron del lugar"),
    (r"le queda libre", "rewrite the construction"),
    (r"\b(pibe|laburo|che)\b", "never"),
    (r"\bvos\b(?! )", "no voseo"),
]


def check_es_register(files):
    """Regionalism scan. Skips quotation lines: RVR1960 wording is never touched."""
    hits = []
    for f in files:
        for i, ln in enumerate(f.read_text().split("\n"), 1):
            if ln.lstrip().startswith(">") or ln.lstrip().startswith("---"):
                continue
            for pat, suggest in ES_REGISTER:
                for m in re.finditer(pat, ln, re.I):
                    hits.append((f.name, i, m.group(0), suggest))
    return hits


# Cosmological terminology. Declared in every chapter's frontmatter since Part I
# ("no globe/global/globally/globular/planet/planetary/worldwide") and enforced only
# by memory until 2026-09-11, when an ES Part II review found three violations in
# Spanish AND one in the already-cleared English baseline. A rule that lives in a
# frontmatter string is not enforced. Applies to BOTH languages.
TERMINOLOGY = [
    (r"\bplanet(a|ary|arios?|as?)?\b", "the earth / la tierra — not a modern cosmological model"),
    (r"\bglobal(ly|mente)?\b", "avoid; say what is actually meant"),
    (r"\bglobular\b", "avoid"),
    (r"\bworldwide\b", "avoid"),
    (r"\bmundial(es)?\b", "avoid; 'todo el mundo' in RVR1960 quotations is fine"),
]


def check_terminology(files):
    """Modern cosmological vocabulary must not be imported into biblical lexical
    explanation. Skips quotation lines and the frontmatter that states the rule."""
    hits = []
    for f in files:
        for i, ln in enumerate(f.read_text().split("\n"), 1):
            s = ln.lstrip()
            if s.startswith(">") or s.startswith("localization:") or "TERMINOLOG" in ln:
                continue
            for pat, suggest in TERMINOLOGY:
                for m in re.finditer(pat, ln, re.I):
                    hits.append((f.name, i, m.group(0), suggest))
    return hits


def check_prose_vosotros(files):
    """vosotros belongs to RVR1960 quotations only, never to the narration."""
    hits = []
    for f in files:
        for i, ln in enumerate(f.read_text().split("\n"), 1):
            if ln.lstrip().startswith(">"):
                continue
            m = re.search(r"\b(vosotros|habéis|estáis|sois|vuestro)\b", ln)
            if m:
                hits.append((f.name, i, m.group(0)))
    return hits


def prose_only(text):
    """Body prose with component labels and word-study lines removed.
    The design system uses an em dash as its label separator, so a raw em-dash
    count is not a measure of em-dash overuse in the writing."""
    keep = []
    for ln in text.split("\n"):
        s = ln.strip()
        if s.startswith("- **") or s.startswith("**Finding") or s.startswith("**Open question"):
            continue
        if " · " in s or s.startswith(":::") or s.startswith("#"):
            continue
        keep.append(ln)
    return "\n".join(keep)


# Typographic normalization for the render read-back check. Pandoc turns straight
# quotes into curly ones and can reshape dashes, so comparing a source heading to
# pdftotext output byte-for-byte reports a false MISSING SECTION for any title
# containing a quote or dash. Caught 2026-09-11 by Part III ch19, whose approved
# title is: Who Are "the People of God"? -- the checker was wrong, not the chapter.
def _norm(s):
    for a, b in (("\u201c", '"'), ("\u201d", '"'), ("\u2018", "'"), ("\u2019", "'"),
                 ("\u2014", "-"), ("\u2013", "-"), ("\u2026", "...")):
        s = s.replace(a, b)
    return s


def strip_frontmatter(t):
    if t.startswith("---"):
        e = t.find("\n---", 3)
        if e != -1:
            return t[e + 4:].lstrip("\n")
    return t

def declutter(t):
    t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", t)
    return re.sub(r"\[\[([^\]]+)\]\]", r"\1", t)

def git(*a):
    return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True).stdout.strip()

def collect(lang, part):
    src = ROOT / LANGS[lang]["dir"]
    title, order = PARTS[lang][part]
    files = []
    for pre in order:
        hits = sorted(src.glob(pre + "*.md"))
        if not hits:
            sys.exit(f"MISSING: nothing matching {pre}* in {src}")
        files.extend(hits)
    return title, files

def render(lang, part, outdir, stem):
    title, files = collect(lang, part)
    chunks = [declutter(strip_frontmatter(f.read_text())).strip() for f in files]
    words = sum(len(c.split()) for c in chunks)
    outdir.mkdir(parents=True, exist_ok=True)

    md = outdir / f"{stem}-clean.md"
    md.write_text(f"# {title}\n\n*Draft 1. {words:,} words.*\n\n" + "\n\n---\n\n".join(chunks) + "\n")

    frag = subprocess.run(["pandoc", str(md), "-f", "markdown+fenced_divs", "-t", "html5"],
                          capture_output=True, text=True, check=True).stdout
    html = outdir / f"{stem}.html"
    html.write_text(f'<!doctype html>\n<html lang="{lang}"><head><meta charset="utf-8">'
                    f"<title>{title}</title><style>{CSS}</style></head><body>\n{frag}\n</body></html>\n")
    pdf = outdir / f"{stem}.pdf"
    subprocess.run(["weasyprint", "-e", "utf-8", str(html), str(pdf)], check=True)
    html.unlink()

    # A clean exit code from WeasyPrint is not proof the render is correct.
    raw = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
    txt = re.sub(r"^\s*\d+\s*$", "", raw, flags=re.M)
    flat = re.sub(r"\s+", " ", txt)
    got = len(txt.split())
    bad = sum(raw.count(m) for m in ("â€", "�", "Ã"))
    missing = [f.stem for f in files
               if _norm(re.sub(r"\s+", " ", declutter(strip_frontmatter(f.read_text()))
                         .strip().split("\n", 1)[0].lstrip("# "))) not in _norm(flat)]
    pages = len(pypdf.PdfReader(str(pdf)).pages) if pypdf else "?"
    ok = bad == 0 and not missing and abs(got - words) < words * 0.02
    print(f"     {pages} pages, {got:,}/{words:,} words recovered, {bad} mojibake, "
          f"{len(missing)} sections missing  " + ("OK" if ok else "<-- CHECK"))
    for m in missing:
        print(f"       MISSING SECTION: {m}")
    if not ok:
        sys.exit("render verification failed")
    return md, pdf, title, words, pages

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--lang", default="en", choices=list(LANGS))
    ap.add_argument("--snapshot", metavar="MILESTONE",
                    help="permanent milestone, e.g. d1-initial or d1-reviewed")
    ap.add_argument("--no-drop", action="store_true")
    ap.add_argument("--proof", action="store_true", help="render the design-system proof instead of a Part")
    a = ap.parse_args()
    lang = a.lang
    if a.proof:
        BUILD.mkdir(parents=True, exist_ok=True)
        src = ROOT / "design" / "design-proof-v1.md"
        html = BUILD / "design-proof-v1.html"
        frag = subprocess.run(["pandoc", str(src), "-f", "markdown+fenced_divs", "-t", "html5"],
                              capture_output=True, text=True, check=True).stdout
        html.write_text(f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
                        f"<title>Design System v1</title><style>{CSS}</style></head><body>\n{frag}\n</body></html>\n")
        pdf = BUILD / "design-proof-v1.pdf"
        subprocess.run(["weasyprint", "-e", "utf-8", str(html), str(pdf)], check=True)
        html.unlink()
        pages = len(pypdf.PdfReader(str(pdf)).pages) if pypdf else "?"
        print(f"PROOF {pdf.relative_to(ROOT)}  ({pages} pages)")
        if not a.no_drop and READER.is_dir():
            shutil.copy2(pdf, READER / pdf.name); print(f"     -> {READER / pdf.name}")
        return
    parts = sorted(PARTS[lang]) if a.all else ([a.part] if a.part in PARTS[lang] else sys.exit("use --part N or --all"))

    for p in parts:
        if a.snapshot:
            stem = f"part-{p:02d}-{lang}-{a.snapshot}"
            out = SNAPS / lang / f"part-{p:02d}"
            if (out / f"{stem}.pdf").exists():
                sys.exit(f"REFUSING to overwrite existing milestone: {out/stem}.pdf\n"
                         "Snapshots are immutable. Use a new milestone name.")
            print(f"SNAPSHOT {lang} part {p} -> {a.snapshot}")
        else:
            stem = f"part-{p:02d}-{lang}"
            out = BUILD / lang
            print(f"BUILD {lang} part {p}")

        _, files = collect(lang, p)
        term = check_terminology(files)
        print(f"     terminology: {len(term)} cosmological  "
              + ("OK" if not term else "<-- no planet/global/worldwide in either edition"))
        for n, i, hit, sug in term[:12]:
            print(f"       {n}:{i}  {hit!r} -> {sug}")

        if lang == "es":
            reg = check_es_register(files)
            vos = check_prose_vosotros(files)
            print(f"     register: {len(reg)} regional, {len(vos)} prose-vosotros  "
                  + ("OK" if not reg and not vos else "<-- see ES-REGISTER.md"))
            for n, i, hit, sug in reg[:12]:
                print(f"       {n}:{i}  {hit!r} -> {sug}")
            for n, i, hit in vos[:6]:
                print(f"       {n}:{i}  prose {hit!r} outside a quotation")

        md, pdf, title, words, pages = render(lang, p, out, stem)

        if a.snapshot:
            commit, when = git("rev-parse", "HEAD"), git("log", "-1", "--format=%cs")
            # Only the chapter source matters for provenance. An edited build script
            # does not make the snapshotted text uncommitted.
            src_dirty = git("status", "--porcelain", "--", LANGS[lang]["dir"])
            dirty = ("UNCOMMITTED CHANGES IN SOURCE" if src_dirty
                     else "source committed at this commit")
            (out / f"{stem}-MANIFEST.txt").write_text(
                f"Edition:        {LANGS[lang]['label']} ({lang})\n"
                f"Part:           {p}  {title}\n"
                f"Milestone:      {a.snapshot}\n"
                f"Source commit:  {commit}\n"
                f"Commit date:    {when}\n"
                f"Tree state:     {dirty}\n"
                f"Built:          {date.today()}\n"
                f"Extent:         {words:,} words, {pages} pages\n"
                f"\nThis snapshot is immutable. The build script refuses to overwrite it.\n"
                f"Canonical source: manuscript/{LANGS[lang]['dir']}/ at commit {commit[:7]}\n")
            print(f"     manifest written, source commit {commit[:7]} ({dirty})")

        if not a.no_drop and READER.is_dir():
            dest = READER / LANGS[lang]["reader"] / f"{LANGS[lang]['part_word']} {p:02d}"
            dest.mkdir(parents=True, exist_ok=True)
            for f in [md, pdf] + ([out / f"{stem}-MANIFEST.txt"] if a.snapshot else []):
                shutil.copy2(f, dest / f.name)
            print(f"     -> {dest}")

if __name__ == "__main__":
    main()
