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
               ["ch13-", "ch14-", "ch15-", "ch16-", "ch17-", "ch18-", "ch19-"]),
           4: ("Part IV: Israel, the Nations, and the Commission",
               ["ch20-", "ch21-", "ch22-", "ch23-", "ch24-"]),
           5: ("Part V: Ages, Resurrection, and the Door into Revelation",
               ["ch25-", "ch26-", "ch27-", "ch28-", "ch29-"]),
           6: ("Part VI: Revelation, Read Through Earlier Scripture",
               ["ch30-", "ch31-", "ch32-", "ch33-", "ch34-",
                "ch35-", "ch36-", "ch37-", "ch38-", "ch39-"]),
           7: ("Part VII: Testing the Case Against Itself",
               ["ch40-", "ch41-", "ch42-", "ch43-",
                "ch44-", "ch45-", "ch46-"]),
           8: ("Part VIII: The Millennium and the Open Horizon",
               ["ch47-", "ch48-", "ch49-",
                "ch50-", "ch51-", "ch52-"]),
           9: ("Part IX: What I Can Actually Defend",
               ["ch53-", "ch54-"])},
    "es": {1: ("Parte I: La pregunta que no se quedó pequeña",
               ["00a-", "00b-", "ch01-", "ch02-", "ch03-", "ch04-", "ch05-", "ch06-"]),
           2: ("Parte II: El discurso del Monte de los Olivos, leído en su propio siglo",
               ["ch07-", "ch08-", "ch09-", "ch10-", "ch11-", "ch12-"]),
           3: ("Parte III: Lo que el nuevo pacto cambió realmente",
               ["ch13-", "ch14-", "ch15-", "ch16-", "ch17-", "ch18-", "ch19-"]),
           4: ("Parte IV: Israel, las naciones y la comisión",
               ["ch20-", "ch21-", "ch22-", "ch23-", "ch24-"]),
           5: ("Parte V: Las edades, la resurrección y la puerta a Apocalipsis",
               ["ch25-", "ch26-", "ch27-", "ch28-", "ch29-"]),
           6: ("Parte VI: Apocalipsis, leído a través de la Escritura anterior",
               ["ch30-", "ch31-", "ch32-", "ch33-", "ch34-",
                "ch35-", "ch36-", "ch37-", "ch38-", "ch39-"]),
           7: ("Parte VII: Poniendo a prueba el caso contra sí mismo",
               ["ch40-", "ch41-", "ch42-", "ch43-",
                "ch44-", "ch45-", "ch46-"]),
           8: ("Parte VIII: El milenio y el horizonte abierto",
               ["ch47-", "ch48-", "ch49-",
                "ch50-", "ch51-", "ch52-"]),
           9: ("Parte IX: Lo que de verdad puedo defender",
               ["ch53-", "ch54-"])},
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


# Book One normalization checks (2026-10-13, BIBLE-3c7). Parts VIII-IX set the
# standard; Parts I-VII were drafted before it existed. Each rule below was applied
# by hand in the Part VIII revision (EDITORIAL-RULES.md: TYPOGRAPHY-002, GLOSS-001,
# RESEARCH-PROCESS-002). Hand-applied rules come back, so they are checked here.
# REPORT-ONLY while Part I pilots them: if a check flags legitimate text, the
# checker is refined, not the prose. Calibrated to report zero on Parts VIII-IX.
# Arrows are notation, not decoration: Parts VIII-IX use → and ↓, and Part IV ch21
# writes Paul's chain "call ← believe ← hear". ← was wrongly included at first (2026-10-13).
DECOR = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆⬇⭕↩↪️]")
GRADE_WORDS = re.compile(r"\b(SUPPORTS|PERMITS|REQUIRES|CONTRADICTS|DOES NOT ESTABLISH|"
                         r"APOYA|PERMITE|EXIGE|CONTRADICE|NO ESTABLECE)\b")
# Research-process bookkeeping that must not print: stage numbers, ledger and
# ticket ids, bead ids, and the scope labels that now live in HTML comments.
LABELS = re.compile(r"\b(Stage|Etapa)s? \d|\bSYNC-\d|\bPR-\d{3}|\bq\d{3}\b|\bBIBLE-[a-z0-9]{3}\b|"
                    r"SPANISH-SPECIFIC|SOURCE-LANGUAGE|ESPEC[IÍ]FICO DEL ESPA[NÑ]OL|"
                    r"\bTier [A-D]\b|\bNivel [A-D]\b")
SRC_SPAN = re.compile(r'<span class="(gr|he)">(.*?)</span>(.{0,4})', re.S)
# Box labels and rules the Part VIII revision replaced: "Where we are." became
# "Where this leaves us.", "What it earned." became "The question this leaves."
# (RESEARCH-PROCESS-002 retired the bookkeeping metaphor), and the `---` rules
# around boxes were dropped. Found in Parts I-VII on 2026-10-13: 46 of each box
# label per edition, 22 rules in EN.
OLD_CONVENTION = re.compile(r"^\*\*(Where we are|What it earned|What this earned|Dónde estamos|"
                            r"Qué se ganó|Lo que (?:se )?ganó)\.\*\*|^---$")
# Generic box titles. Every Part VIII-IX box names what it shows ("The purpose
# formula, four times"); Parts II-VII reuse a fixed caption (22 "How strongly
# evidence bears", 12 "Original language", 5 "Historical context", 3 "Finding" in EN,
# counted 2026-10-13). Matched only as the whole title line, so a descriptive title
# that merely begins with "Finding —" is left alone.
GENERIC_TITLE = re.compile(r"^\*\*(How strongly evidence bears|Original language|Historical context|"
                           r"Finding|Open question|Con qué fuerza pesa la evidencia|Lengua original|"
                           r"Contexto histórico|Hallazgo|Pregunta abierta|"
                           r"Nota textual — (?:una )?deuda declarada)\*\*\s*$")
# ES Parts VIII-IX and ES-REGISTER say "el poco de tiempo" for mikron chronon;
# Parts II-VII drifted to "la pequeña temporada" (21 occurrences, 2026-10-13).
ES_TERM_DRIFT = re.compile(r"\bpequeña temporada\b", re.I)
# RESEARCH-PROCESS-002 retired the bookkeeping metaphor (debts declared, paid,
# handed forward). It survives in box captions in EN ch27/33/37/41/43 and in the
# ES "Nota textual — deuda declarada" caption in 26 chapters (counted 2026-10-13).
DEBT = re.compile(r"\b(?:debts?|deudas?)\b", re.I)
# "this project" narrates the work rather than the investigation. Caught by the
# author's reviewer in Part II ch11 (2026-10-13) after the checker passed it.
PROJECT_TALK = re.compile(r"\b(?:this|the) project\b|\beste proyecto\b", re.I)
# Stage-talk without a number ("in this stage", "five stages") is the same
# research-process leak as "Stage 61", and the numbered pattern cannot see it.
STAGE_TALK = re.compile(r"\b(?:this|that|each|every|a|the|one|two|three|four|five|six|several|many|"
                        r"\w+-\w+) stages?\b", re.I)
# Spanish 'etapa' is excluded: it is the ordinary word for a phase ("la estructura
# en dos etapas" of Rev 20:5 in ES ch53), so lowercase etapa-talk cannot be told
# from narration. Numbered "Etapa N" is still caught by LABELS.

def check_normalization(files):
    """Returns {category: [(file, line, excerpt)]}. Quotation lines are exempt
    from the gloss rule only: a quoted verse is glossed in the sentence after it."""
    out = {k: [] for k in ("decor", "grade", "label", "gloss", "structure", "convention")}
    for f in files:
        body = strip_frontmatter(f.read_text())
        body = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), body, flags=re.S)
        glossed = set()
        h1 = 0
        prev = ""
        for i, ln in enumerate(body.split("\n"), 1):
            for m in DECOR.finditer(ln):
                out["decor"].append((f.name, i, m.group(0)))
            unspanned = re.sub(r'<span class="grade">.*?</span>', "", ln)
            for m in GRADE_WORDS.finditer(unspanned):
                out["grade"].append((f.name, i, m.group(0)))
            for m in LABELS.finditer(ln):
                out["label"].append((f.name, i, m.group(0)))
            for m in PROJECT_TALK.finditer(ln):
                out["label"].append((f.name, i, m.group(0)))
            for m in DEBT.finditer(ln):
                out["label"].append((f.name, i, m.group(0)))
            for m in STAGE_TALK.finditer(ln):
                out["label"].append((f.name, i, m.group(0)))
            if OLD_CONVENTION.match(ln):
                out["convention"].append((f.name, i, ln[:30]))
            for m in ES_TERM_DRIFT.finditer(ln):
                out["convention"].append((f.name, i, "term drift: " + m.group(0) + " -> el poco de tiempo"))
            # The generic caption with a suffix ("— contrary evidence, printed") slipped
            # past the whole-line match in ES Part III ch15 (2026-10-13).
            if re.match(r"^\*\*(How strongly evidence bears|Con qué fuerza pesa la evidencia|Historical context|"
                        r"Original language|Contexto histórico|Lengua original) — ", ln):
                out["convention"].append((f.name, i, "generic box title with suffix " + ln[:50]))
            if GENERIC_TITLE.match(ln):
                out["convention"].append((f.name, i, "generic box title " + ln[:40]))
            if ln.startswith("# ") and not re.match(r"# (Coda|Epilogue|Epílogo)\b", ln):
                h1 += 1
                if h1 > 1:
                    out["structure"].append((f.name, i, "second chapter-level heading"))
            if ln.startswith("####"):
                out["structure"].append((f.name, i, "heading deeper than ###"))
            # A paragraph opening "(a) " becomes an ordered list in Pandoc and prints
            # as "1." -- caught by the reviewer in ch14 (2026-10-13). Escape as "\(a)".
            if re.match(r"\([a-z]\) \S", ln) and (i == 1 or not prev.strip()):
                out["structure"].append((f.name, i, "paragraph opens with (a): Pandoc makes it a list"))
            prev = ln
            # Quotation lines are glossed in the next sentence; table rows carry the
            # transliteration in a neighbouring column (ch51's word table).
            if ln.lstrip().startswith((">", "|")):
                continue
            for m in SRC_SPAN.finditer(ln):
                # Transliteration-first form: "*Armageddon* (<span>Ἁρμαγεδών</span>)".
                if re.search(r"\*[^*]+\*\s*\($", ln[:m.start()]):
                    glossed.add(m.group(2).strip())
                    continue
                term = m.group(2).strip()
                # GLOSS-001 governs terms. A clause of three or more words is a
                # quotation, translated in its own sentence (2 Kgs 1:10, Ps 90:4 in ch48-49).
                if term in glossed or len(term.split()) >= 3:
                    continue
                # Both benchmark forms: "term (*translit*, gloss)" and, inside an
                # existing parenthesis, "(term, *translit*)".
                # Third form, the word-study header: "<span>…</span> · *translit* · gloss".
                if re.match(r"\s*\(\*|,\s*\*|\s*·\s*\*", m.group(3)):
                    glossed.add(term)
                else:
                    out["gloss"].append((f.name, i, term[:30]))
    return out


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
#
# Same failure, second cause, caught 2026-09-19 by Part VIII ch49, whose approved
# title carries Greek: chi-ilia ete -- The Gate Opens. Source-language runs in a
# heading must be wrapped in a .gr span or the original-language gate fails them,
# and that markup renders as bare text, so the raw heading can never match the PDF.
# Strip inline tags before comparing. The checker was wrong, not the chapter.
def _norm(s):
    s = re.sub(r"<[^>]+>", "", s)
    for a, b in (("\u201c", '"'), ("\u201d", '"'), ("\u2018", "'"), ("\u2019", "'"),
                 ("\u2014", "-"), ("\u2013", "-"), ("\u2026", "...")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()


def strip_frontmatter(t):
    if t.startswith("---"):
        e = t.find("\n---", 3)
        if e != -1:
            return t[e + 4:].lstrip("\n")
    return t

def declutter(t):
    t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", t)
    return re.sub(r"\[\[([^\]]+)\]\]", r"\1", t)

def source_words(t):
    """Words a reader can see, not markdown tokens.
    The source count used to be raw .split(), so every table pipe, `<span class=..>`
    opener and `::: finding` fence counted as a word that can never appear in the PDF.
    Emoji balanced it by accident (they count in both), so the bias stayed hidden until
    the Part VIII reader revision (2026-10-10) removed the emoji and added tables and
    transliteration spans: 19,850 recovered against 20,418 'source', a false failure
    with no text missing (markup-stripped source 19,929). Same 2% band as before --
    the count is fixed, the tolerance is not widened."""
    t = re.sub(r"<[^>]+>", " ", t)
    keep = []
    for ln in t.split("\n"):
        s = ln.strip()
        if s.startswith(":::") or s == "---" or re.fullmatch(r"\|[\s:|-]+\|", s):
            continue
        keep.append(ln.replace("|", " "))
    return len(" ".join(keep).split())

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
    words = sum(source_words(c) for c in chunks)
    outdir.mkdir(parents=True, exist_ok=True)

    md = outdir / f"{stem}-clean.md"
    # Chapters are joined by a blank line, not `---`. Every chapter title is an h1, and
    # h1 already forces a new page, so a rule between chapters adds nothing -- and when
    # the previous chapter ended near the foot of a page it was pushed onto a page of its
    # own: Part VIII rendered a blank page holding one short rule (2026-10-10).
    # No draft/word-count line on the title page: it was hard-coded "Draft 1" and
    # stayed on every later revision (Part VIII review, 2026-10-10). The extent and the
    # source commit are recorded in each snapshot's MANIFEST, which is where they belong.
    md.write_text(f"# {title}\n\n" + "\n\n".join(chunks) + "\n")

    frag = subprocess.run(["pandoc", str(md), "-f", "markdown+fenced_divs", "-t", "html5"],
                          capture_output=True, text=True, check=True).stdout
    # Pandoc appends U+FE0E (text-presentation selector) to characters that also
    # exist as emoji, such as the arrow in "1 Thessalonians 4 <-> Revelation 20".
    # WeasyPrint finds no font for the pair and falls back to .LastResort, so the
    # arrow printed as a boxed "?" -- in the Part VII scorecard, seven times, and
    # every text gate passed it. The bare character renders; the selector is
    # what breaks it. Caught 2026-09-25 by rendering the table pages to images.
    frag = frag.replace("︎", "")
    html = outdir / f"{stem}.html"
    html.write_text(f'<!doctype html>\n<html lang="{lang}"><head><meta charset="utf-8">'
                    f"<title>{title}</title><style>{CSS}</style></head><body>\n{frag}\n</body></html>\n")
    pdf = outdir / f"{stem}.pdf"
    subprocess.run(["weasyprint", "-e", "utf-8", str(html), str(pdf)], check=True)
    html.unlink()

    # A clean exit code from WeasyPrint is not proof the render is correct.
    raw = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
    txt = re.sub(r"^\s*\d+\s*$", "", raw, flags=re.M)

    # Justified body text is hyphenated at line ends, and pdftotext returns the two
    # halves as separate tokens -- so a hyphenated word counts as two words against a
    # source that counts it as one. The inflation scales with length, which means the
    # 2% band silently tightens as a Part grows and eventually reports a false failure
    # on a Part with nothing wrong with it. Caught 2026-09-20 by Part VIII after a
    # correction pass: 22,193 recovered against 21,744 source, over the band by 14
    # tokens, with 208 line-break hyphens in the document. Rejoining them lands it at
    # +241, inside the SAME 2% band -- the tolerance is not widened here, the count is
    # simply made to measure words instead of typesetting.
    #
    # WeasyPrint breaks with U+2010 HYPHEN (and U+00AD shows up too), which is why an
    # ASCII-hyphen check finds nothing. ASCII '-' is rejoined for the count as well,
    # where spelling does not matter -- but NOT in `flat`, because a genuinely
    # hyphenated word like "first-century" broken at its own hyphen must keep it to
    # match a heading.
    dehyph = lambda t, chars: re.sub(rf"[{chars}]\s*\n\s*", "", t)
    flat = re.sub(r"\s+", " ", dehyph(txt, "\u2010\u00ad"))
    got = len(dehyph(txt, "\u2010\u00ad-").split())
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
    original_language_gate(files, pdf)
    table_layout_gate(md, lang)
    return md, pdf, title, words, pages


# LAYOUT-003: a comparison table's meaning lives in the row, and a row split
# across a page passes every text gate above. This walks the rendered layout
# itself. See check-table-breaks.py for why and how it was validated.
def table_layout_gate(md, lang):
    r = subprocess.run([sys.executable, str(Path(__file__).resolve().parent / "check-table-breaks.py"),
                        str(md), "--lang", lang], capture_output=True, text=True)
    print("\n".join(ln for ln in r.stdout.splitlines() if "unicode-bidi" not in ln))
    if r.returncode != 0:
        sys.exit("table layout gate failed")

# ---------------------------------------------------------------------------
# ORIGINAL-LANGUAGE RENDER INTEGRITY GATE
#
# Build success does not establish render integrity. Part VI shipped a build
# that passed every check above while the stylesheet was silently uppercasing
# polytonic Greek -- turning KAI EZESAN into a form with its breathings and
# accents detached, inside the one aside whose entire argument is that a single
# verb appears twice. Typography was corrupting the evidence being argued from,
# and pdftotext reported the corrupted forms back as though they were the
# source. It was caught only by looking at a rendered page.
#
# The same defect then recurred in the Spanish edition for a different reason:
# the Greek had been written into tables without .gr spans, so the stylesheet
# protection did not apply to it.
#
# This gate cannot verify letterforms -- nothing in a text pipeline can. What it
# CAN do is make the inspection non-optional and cheap: it names the exact pages
# carrying source-language evidence, so a reviewer renders those pages instead of
# guessing, and it fails the build outright when source-language text reaches the
# page without the .gr/.he protection that keeps display typography off it.
#
# THE PRINCIPLE, larger than its implementation: source-language evidence must
# survive typesetting unchanged.
# ---------------------------------------------------------------------------
SRC_LANG = re.compile(r"[\u0370-\u03FF\u1F00-\u1FFF\u0590-\u05FF]")

def original_language_gate(files, pdf):
    unwrapped = []
    for f in files:
        body = declutter(strip_frontmatter(f.read_text()))
        bare = re.sub(r'<span class="(?:gr|he)">.*?</span>', "", body, flags=re.S)
        if SRC_LANG.search(bare):
            unwrapped.append(f.stem)
    if unwrapped:
        print("     original-language gate: UNPROTECTED SOURCE TEXT  <-- CHECK")
        for u in unwrapped:
            print(f"       NOT IN A .gr/.he SPAN: {u}")
        sys.exit("original-language render integrity gate failed")

    raw = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                         capture_output=True, text=True).stdout
    hits = [i for i, pg in enumerate(raw.split("\f"), 1) if SRC_LANG.search(pg)]
    if not hits:
        print("     original-language gate: no Greek/Hebrew in this Part  OK")
        return
    shown = ", ".join(str(h) for h in hits[:12]) + (" …" if len(hits) > 12 else "")
    print(f"     original-language gate: {len(hits)} page(s) carry source text, all .gr/.he wrapped  OK")
    print(f"       INSPECT VISUALLY BEFORE CLEARING THIS PART: pp. {shown}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", type=int)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--lang", default="en", choices=list(LANGS))
    ap.add_argument("--snapshot", metavar="MILESTONE",
                    help="permanent milestone, e.g. d1-initial or d1-reviewed")
    # A milestone taken AFTER a Part is closed has to say why it exists, or the
    # snapshot directory becomes a pile of names nobody can tell apart later.
    # Presentation-only repairs (whitespace, encoding, broken layout) are the
    # case this was added for: closed forbids discretionary rewriting, it does
    # not freeze a deterministic rendering defect forever.
    ap.add_argument("--note", metavar="TEXT",
                    help="free text recorded in the milestone manifest under NOTE")
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

        norm = check_normalization(files)
        counts = ", ".join(f"{len(v)} {k}" for k, v in norm.items())
        print(f"     normalization (report only): {counts}  "
              + ("OK" if not any(norm.values()) else "<-- see EDITORIAL-RULES.md"))
        for k, v in norm.items():
            for n, i, hit in v[:5]:
                print(f"       {k:9} {n}:{i}  {hit!r}")

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
                + (f"\nNOTE\n{a.note}\n" if a.note else "")
                + f"\nThis snapshot is immutable. The build script refuses to overwrite it.\n"
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
