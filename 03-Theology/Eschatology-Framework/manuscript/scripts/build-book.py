#!/usr/bin/env python3
"""Assemble the whole book, one PDF per language (BIBLE-493).

    python3 scripts/build-book.py --lang en
    python3 scripts/build-book.py --lang es
    python3 scripts/build-book.py --lang en --final     # also writes the release file name

Order follows FRONT-BACK-MATTER-DECISIONS.md Table 1 and 2: cover, title page,
copyright, dedication, foreword, note to the reader, the five orientation pages,
contents, Parts I-IX (each with its own title page), Appendices A-G,
acknowledgments, about the author.

Chapter files are read, never edited. Appendices E and D2 are regenerated here
with page numbers: a first render maps every reference and glossed word to the
pages it actually falls on, the indexes are rewritten, and the book is rendered
again until the page count stops changing. Reference lookups are confined to the
chapters the text-based index already found them in, so a common word or a
reference in a running head cannot spread an entry across the book.

Release names are fixed by PUBLISHING-PREP-NOTES.md (author, 2026-10-18).
"""
import argparse
import importlib.util
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

import pypdf
from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bm = load("bm", "build-manuscript.py")
si = load("si", "build-scripture-index.py")
wi = load("wi", "build-word-index.py")

OUT = ROOT / "_build" / "book"
READER = bm.READER
BOOK_CSS = (HERE / "book-v1.css").read_text(encoding="utf-8")
COVER = {"en": ROOT / "cover/front/front-cover-en.png", "es": ROOT / "cover/front/front-cover-es.png"}
RELEASE = {"en": "the-promise-and-the-little-season-en.pdf", "es": "the-promise-and-the-little-season-es.pdf"}
REVIEW_DIR = {"en": "en", "es": "es"}

META = {
    "en": {"title": "The Promise and the Little Season",
           "title_lines": "The Promise<br>and the Little Season",
           "subtitle": "An investigation into prophecy, the great commission, and the thousand years",
           "contents": "Contents", "author": "Marcelo Mario Berta Silva",
           "imprint": "Bright Forest Publishing", "site": "kollabs.ai",
           "front": ["00b-copyright", "00-dedication", "@00a-", "@00b-a-note", "00c-", "00d-", "00e-", "00f-", "00g-"],
           "back": ["zz-appendix-a-", "zz-appendix-b-", "zz-appendix-c-", "zz-appendix-d-", "zz-appendix-e-",
                    "zz-appendix-f-", "zz-appendix-g-", "zz-acknowledgments", "zz-about-the-author"],
           "index_by_chapters": "with the chapters where it appears", "index_by_pages": "with the pages where it appears"},
    "es": {"title": "La promesa y el poco de tiempo",
           "title_lines": "La promesa<br>y el poco de tiempo",
           "subtitle": "Una investigación sobre la profecía, la gran comisión y los mil años",
           "contents": "Índice general", "author": "Marcelo Mario Berta Silva",
           "imprint": "Bright Forest Publishing", "site": "kollabs.ai",
           "front": ["00b-derechos", "00-dedicatoria", "@00a-", "@00b-", "00c-", "00d-", "00e-", "00f-", "00g-"],
           "back": ["zz-apendice-a-", "zz-apendice-b-", "zz-apendice-c-", "zz-apendice-d-", "zz-apendice-e-",
                    "zz-apendice-f-", "zz-apendice-g-", "zz-agradecimientos", "zz-sobre-el-autor"],
           "index_by_chapters": "con los capítulos donde aparecen", "index_by_pages": "con las páginas donde aparecen"},
}


def find(lang, prefix):
    """'@00a-' = chapter folder (en/, es/); otherwise matter-drafts/<lang>/."""
    if prefix.startswith("@"):
        hits = sorted((ROOT / lang).glob(prefix[1:] + "*.md"))
    else:
        hits = sorted((ROOT / "matter-drafts" / lang).glob(prefix + "*.md"))
    if len(hits) != 1:
        sys.exit(f"expected one file for {prefix!r} in {lang}, found {len(hits)}")
    return hits[0]


def body(path):
    t = bm.declutter(bm.strip_frontmatter(path.read_text(encoding="utf-8"))).strip()
    # Images in matter drafts are relative to the drafts folder; the book HTML lives in _build.
    t = re.sub(r'src="\.\./img/', 'src="' + (ROOT / "matter-drafts/img").as_uri() + "/", t)
    return t


def with_id(text, ident, cls=None):
    """Give the file's first '# Title' an id (and class) so contents can link to it."""
    attrs = f"#{ident}" + (f" .{cls}" if cls else "")
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            lines[i] = f"{ln} {{{attrs}}}"
            return "\n".join(lines), ln[2:].strip()
    sys.exit(f"no '# ' heading for {ident}")


def cover_image(lang):
    """Crop the 0.125in print bleed off the 6.25x9.25in cover: the digital page is 6x9."""
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"cover-{lang}.jpg"
    img = Image.open(COVER[lang]).convert("RGB")
    w, h = img.size
    b = round(w * 0.125 / 6.25)
    img.crop((b, b, w - b, h - b)).save(out, quality=92, dpi=(300, 300))
    return out


def assemble(lang, index_override=None):
    """Return (markdown, sections). sections: list of (id, title, kind, chapter_label, path)."""
    m = META[lang]
    parts_md, sections = [], []
    parts_md.append(f'::: cover\n<img src="{cover_image(lang).as_uri()}" alt="">\n:::')
    parts_md.append(
        "::: titlepage\n"
        f'<p class="t1">{m["title_lines"]}</p>\n\n<p class="t2">{m["subtitle"]}</p>\n\n'
        f'<p class="au">{m["author"]}</p>\n\n<p class="im">{m["imprint"]}</p>\n\n<p class="si">{m["site"]}</p>\n:::')

    front = []
    for pre in m["front"]:
        p = find(lang, pre)
        text = body(p)
        if p.stem.startswith(("00b-copyright", "00b-derechos")):
            parts_md.append(text)  # already a ::: copyright div
            continue
        if p.stem.startswith(("00-dedication", "00-dedicatoria")):
            parts_md.append("::: dedication\n" + text + "\n:::")
            continue
        ident = "fm-" + re.sub(r"^\d+[a-z]?-", "", p.stem)[:40]
        text, title = with_id(text, ident)
        front.append(text)
        sections.append((ident, title, "front", "FM" if lang == "en" else "PP", p))

    sections.append(("contents", m["contents"], "toc", "TOC", None))
    chapters_by_part = []
    for n in sorted(bm.PARTS[lang]):
        ptitle, prefixes = bm.PARTS[lang][n]
        label, _, name = ptitle.partition(": ")
        part_id = f"part-{n}"
        block = [f'::: partpage\n# {label} <span class="partname">{name}</span> {{#{part_id} .part}}\n:::']
        sections.append((part_id, ptitle, "part", None, None))
        for pre in prefixes:
            if pre in ("00a-", "00b-"):
                continue  # foreword and note to the reader are front matter in the book
            p = sorted((ROOT / lang).glob(pre + "*.md"))[0]
            num = int(re.match(r"ch(\d+)", p.name).group(1))
            ident = f"ch-{num:02d}"
            text, title = with_id(body(p), ident, "chapter")
            sections.append((ident, title, "chapter", str(num), p))
            # A further top-level heading inside a chapter file (Chapter 54's Coda) is
            # its own entry in the contents and the outline, nested under the Part.
            lines, first = text.split("\n"), True
            for i, ln in enumerate(lines):
                if ln.startswith("# "):
                    if first:
                        first = False
                        continue
                    sub = f"{ident}-{i}"
                    lines[i] = f"{ln} {{#{sub} .chapter}}"
                    sections.append((sub, ln[2:].strip(), "chapter", str(num), p))
            block.append("\n".join(lines))
        chapters_by_part.append("\n\n".join(block))

    back = []
    for pre in m["back"]:
        p = find(lang, pre)
        if index_override and p.stem in index_override:
            raw = index_override[p.stem]
        else:
            raw = p.read_text(encoding="utf-8")
        text = bm.declutter(bm.strip_frontmatter(raw)).strip()
        text = re.sub(r'src="\.\./img/', 'src="' + (ROOT / "matter-drafts/img").as_uri() + "/", text)
        am = re.match(r"zz-(?:appendix|apendice)-([a-g])-", p.name)
        ident = f"app-{am.group(1)}" if am else "bm-" + p.stem[3:]
        text, title = with_id(text, ident)
        back.append(text)
        sections.append((ident, title, "back", am.group(1).upper() if am else None, p))

    toc = [f"::: toc\n# {m['contents']} {{#contents}}\n"]
    for ident, title, kind, _, _ in sections:
        if kind == "toc":
            continue
        cls = {"part": "tpart", "chapter": "tch"}.get(kind, "")
        attr = f"{{.{cls}}}" if cls else ""
        shown = title.replace(": ", " — ", 1) if kind == "part" else title
        toc.append(f"- [{shown}](#{ident})")
    toc_md = "\n".join(toc) + "\n:::"
    # pandoc puts classes on spans, not list items; mark items by a trailing span the CSS can't see,
    # so instead tag them after conversion (see render()).
    md = "\n\n".join(parts_md + front + [toc_md] + chapters_by_part + back) + "\n"
    return md, sections


def to_html(lang, md, extra_css=""):
    frag = subprocess.run(["pandoc", "-f", "markdown+fenced_divs+bracketed_spans", "-t", "html5"],
                          input=md, capture_output=True, text=True, check=True).stdout
    frag = frag.replace("︎", "")
    # contents: class the list items by what they link to
    frag = re.sub(r'<li><a href="#(part-\d+)"', r'<li class="tpart"><a href="#\1"', frag)
    frag = re.sub(r'<li><a href="#(ch-[\d-]+)"', r'<li class="tch"><a href="#\1"', frag)
    title = META[lang]["title"]
    return (f'<!doctype html>\n<html lang="{lang}"><head><meta charset="utf-8"><title>{title}</title>'
            f'<meta name="author" content="{META[lang]["author"]}">'
            f"<style>{bm.CSS}\n{BOOK_CSS}\n{extra_css}</style></head><body>\n{frag}\n</body></html>\n")


def render(lang, md, stem, extra_css=""):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{stem}.md").write_text(md, encoding="utf-8")
    html = OUT / f"{stem}.html"
    html.write_text(to_html(lang, md, extra_css), encoding="utf-8")
    pdf = OUT / f"{stem}.pdf"
    subprocess.run(["weasyprint", "-e", "utf-8", str(html), str(pdf)], check=True,
                   stderr=subprocess.DEVNULL)
    return pdf


def page_texts(pdf):
    raw = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
    pages = raw.split("\f")
    out = []
    for pg in pages:
        pg = re.sub(r"[‐­]\s*\n\s*", "", pg)  # rejoin hyphenated line ends
        out.append(re.sub(r"\s+", " ", pg))
    return out  # index 0 = page 1


def section_starts(pdf, sections):
    """Page (1-based) where each section begins, from the PDF outline."""
    r = pypdf.PdfReader(str(pdf))
    starts = {}

    def walk(items):
        for it in items:
            if isinstance(it, list):
                walk(it)
            else:
                starts.setdefault(it.title.strip(), r.get_destination_page_number(it) + 1)
    walk(r.outline)
    out = {}
    for ident, title, kind, lab, _ in sections:
        key = title if kind != "part" else None
        hit = None
        for t, pg in starts.items():
            if kind == "part" and bm._norm(t).startswith(title.split(":")[0] + " "):
                hit = pg
                break
            if key and bm._norm(t) == bm._norm(title):
                hit = pg
                break
        if hit is None:
            sys.exit(f"outline has no entry for {title!r}")
        out[ident] = hit
    return out, len(r.pages)


def ranges(sections, starts, npages):
    """label -> list of page numbers (chapters, appendices, front matter)."""
    order = sorted(((starts[i], i, lab) for i, _, _, lab, _ in sections), key=lambda x: x[0])
    by_label = defaultdict(list)
    for k, (s, ident, lab) in enumerate(order):
        e = order[k + 1][0] - 1 if k + 1 < len(order) else npages
        if lab:
            by_label[lab].extend(range(s, e + 1))
    return by_label


def page_scripture_index(lang, pages, by_label, skip_pages):
    names, pat = si.book_pattern(lang)
    # Box titles are set in capitals ("MARK 7:19"), so match book names in any case.
    pat = re.compile(pat.pattern, re.I)
    names = {k.lower(): v for k, v in names.items()}
    chapter_index = si.collect(lang)
    found = defaultdict(lambda: defaultdict(set))
    for pno, txt in enumerate(pages, 1):
        if pno in skip_pages:
            continue
        for mm in pat.finditer(txt):
            canon = names[mm.group(1).lower()]
            refs, _ = si.parse_run(txt, mm.end())
            for r in refs:
                if canon in si.SINGLE_CHAPTER and r[1] is None:
                    r = (1, r[0], None, None)
                found[canon][r].add(pno)
    index, misses = defaultdict(dict), []
    for book, refs in chapter_index.items():
        for r, labs in refs.items():
            pg = set()
            for lab in labs:
                rng = set(by_label.get(lab, []))
                hits = found.get(book, {}).get(r, set()) & rng
                if not hits and r[1] is not None:
                    # tables and lists lose the book name next to a continued reference
                    # ("Matthew 11:12; 12:29"): look for the bare "12:29" in the section
                    bare = re.compile(r"(?<![\d:])" + re.escape(si.label(r)) + r"(?![\d:])")
                    hits = {p for p in rng if p not in skip_pages and bare.search(pages[p - 1])}
                if hits:
                    pg |= hits
                elif rng:
                    pg.add(min(rng))  # cited in that section, not found as page text: point to its start
                    misses.append((book, si.label(r), lab))
            index[book][r] = [str(p) for p in sorted(pg)]
    return index, misses


def scripture_md(lang, index):
    t = si.TEXT[lang]
    intro = t["intro"]
    if lang == "en":
        intro = intro.replace("with the chapters where it appears. Numbers are chapters; letters are appendices; "
                              "*FM* is the front matter.", "with the pages where it appears.")
    else:
        intro = intro.replace("con los capítulos donde aparece. Los números son capítulos; las letras, apéndices; "
                              "*PP* son las páginas preliminares.", "con las páginas donde aparece.")
    body_md = si.render(lang, index).split(f"# {t['title']}", 1)[1].split("\n\n", 2)[2]
    return f"---\ntitle: x\n---\n\n# {t['title']}\n\n{intro}\n\n{body_md}"


def page_word_index(lang, pages, by_label, skip_pages, d_text):
    skip = wi.d1_translits(d_text)
    words = wi.collect(lang, skip)
    # every surface form seen for each word, from the source files
    forms = defaultdict(set)
    for lab, path in si.sources(lang):
        if path == wi.D_FILE[lang]:
            continue
        text = re.sub(r"<!--.*?-->", "", bm.strip_frontmatter(path.read_text(encoding="utf-8")), flags=re.S)
        for mm in wi.TERM.finditer(text):
            k = wi.fold(mm.group(3))
            if k in words:
                forms[k].add(unicodedata.normalize("NFC", mm.group(2).strip()))
    def flat(s, he):
        s = unicodedata.normalize("NFD", s.replace("\u2019", "'"))
        s = "".join(c for c in s if not unicodedata.combining(c))
        return re.sub(r"[\s\u05be]", "", s) if he else s
    # pdftotext returns Hebrew in visual order, so Hebrew is compared without vowel
    # points or spaces, in both directions.
    npages = [flat(p, False) for p in pages]
    hpages = [flat(p, True) for p in pages]
    misses = []
    for k, w in words.items():
        pg = set()
        for lab in w["locs"]:
            rng = by_label.get(lab, [])
            if w["cls"] == "he":
                # pointed Hebrew does not survive PDF text extraction intact (the glyphs
                # render correctly; the text layer is scrambled), so find the word by the
                # transliteration printed beside it
                tr = flat(w["tr"], False)
                hits = {p for p in rng if p not in skip_pages and tr in npages[p - 1]}
            else:
                fs = [flat(f, False) for f in forms[k]]
                hits = {p for p in rng if p not in skip_pages and any(f in npages[p - 1] for f in fs)}
            if hits:
                pg |= hits
            elif rng:
                pg.add(min(rng))
                misses.append((w["tr"], lab))
        w["locs"] = [str(p) for p in sorted(pg)]
    head = d_text.split(wi.MARKER)[0]
    marker = wi.MARKER + d_text.split(wi.MARKER)[1].splitlines()[0]
    m = META[lang]
    head = head.replace(m["index_by_chapters"], m["index_by_pages"])
    return head + marker + "\n\n" + wi.render(lang, words) + "\n", misses


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="en", choices=["en", "es"])
    ap.add_argument("--final", action="store_true", help="also copy to the release file name")
    ap.add_argument("--version", default="v1", help="review copy version tag")
    ap.add_argument("--review", action="store_true", help="copy to the Desktop review folder")
    a = ap.parse_args()
    lang = a.lang
    stem = f"book-{lang}"

    md, sections = assemble(lang)
    files = [s[4] for s in sections if s[4] is not None]
    term = bm.check_terminology(files)
    norm = bm.check_normalization(files)
    reg = bm.check_es_register(files) + bm.check_prose_vosotros(files) if lang == "es" else []
    print(f"BOOK {lang}: {len(files)} files; terminology {len(term)}, register {len(reg)}, "
          f"normalization {sum(len(v) for v in norm.values())}")
    for k, v in norm.items():
        for n, i, hit in v[:5]:
            print(f"   {k:9} {n}:{i} {hit!r}")
    if term or reg:
        sys.exit("text gates failed")

    # Pass 1 renders with running heads off: margin boxes do not move text, and a
    # title in a running head would otherwise count as a reference on every page.
    no_heads = "@page { @top-center { content: none; } }"
    e_file = find(lang, META[lang]["back"][4])
    d_file = find(lang, META[lang]["back"][3])
    override = None
    prev = None
    for attempt in range(1, 5):
        pdf = render(lang, assemble(lang, override)[0], stem + "-map", no_heads)
        starts, npages = section_starts(pdf, sections)
        by_label = ranges(sections, starts, npages)
        pages = page_texts(pdf)
        skip_e = set(by_label.get("E", [])) | set(by_label.get("TOC", []))
        skip_d = skip_e | set(by_label.get("D", []))
        e_index, e_miss = page_scripture_index(lang, pages, by_label, skip_e)
        e_md = scripture_md(lang, e_index)
        d_md, d_miss = page_word_index(lang, pages, by_label, skip_d, d_file.read_text(encoding="utf-8"))
        override = {e_file.stem: e_md, d_file.stem: d_md}
        sig = (npages, tuple(sorted(starts.items())))
        print(f"   pass {attempt}: {npages} pages; scripture refs not found as page text {len(e_miss)}, "
              f"words not found {len(d_miss)}")
        if sig == prev:
            break
        prev = sig
    else:
        sys.exit("pagination did not settle in 4 passes")

    final_md = assemble(lang, override)[0]
    pdf = render(lang, final_md, stem)
    raw = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
    bad = sum(raw.count(x) for x in ("â€", "�", "Ã"))
    n = len(pypdf.PdfReader(str(pdf)).pages)
    print(f"   final: {n} pages, {bad} mojibake")
    if bad:
        sys.exit("mojibake in final render")
    (OUT / f"{stem}-index-misses.txt").write_text(
        "scripture (book, ref, section)\n" + "\n".join(map(str, e_miss)) +
        "\n\nwords (translit, section)\n" + "\n".join(map(str, d_miss)) + "\n", encoding="utf-8")

    rev = READER / REVIEW_DIR[lang] / f"{RELEASE[lang][:-4]}-{a.version}.pdf"
    if not a.review:
        print(f"   built {pdf} (no review copy; pass --review)")
    elif rev.exists():
        sys.exit(f"{rev} exists; use a new --version")
    else:
        shutil.copy2(pdf, rev)
        print(f"   review copy -> {rev}")
    if a.final:
        shutil.copy2(pdf, OUT / RELEASE[lang])
        print(f"   release file -> {OUT / RELEASE[lang]}")
        # The fixed release names are the R2 keys, so they always hold the latest build
        # (author, 2026-10-19). The only Desktop files this script overwrites; the
        # numbered review copies above are never replaced.
        if a.review:
            dest = READER / REVIEW_DIR[lang] / RELEASE[lang]
            shutil.copy2(pdf, dest)
            print(f"   release file -> {dest}")


if __name__ == "__main__":
    main()
