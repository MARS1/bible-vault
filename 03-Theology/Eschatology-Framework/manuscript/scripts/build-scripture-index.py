#!/usr/bin/env python3
"""Build Appendix E (scripture index) from the chapter and matter files.

    python3 scripts/build-scripture-index.py en  > matter-drafts/en/zz-appendix-e-scripture-index.md
    python3 scripts/build-scripture-index.py es  > matter-drafts/es/zz-apendice-e-indice-biblico.md
    python3 scripts/build-scripture-index.py en --check   # parse report only

Only references that name their book are indexed ("Revelation 20:3", and the
continuations that follow it: ", 8", "; 21:1"). A bare "20:3" inside a chapter
is not indexed, because the book cannot be attributed reliably. Locations are
chapter numbers and appendix letters for now; assembly (BIBLE-493) replaces
them with page numbers.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (canonical EN, canonical ES, EN aliases, ES aliases, testament)
BOOKS = [
    ("Genesis", "Génesis", [], ["Gn"], "OT"), ("Exodus", "Éxodo", [], [], "OT"),
    ("Leviticus", "Levítico", [], [], "OT"), ("Numbers", "Números", [], [], "OT"),
    ("Deuteronomy", "Deuteronomio", [], [], "OT"), ("Joshua", "Josué", [], [], "OT"),
    ("Judges", "Jueces", [], [], "OT"), ("Ruth", "Rut", [], [], "OT"),
    ("1 Samuel", "1 Samuel", [], [], "OT"), ("2 Samuel", "2 Samuel", [], [], "OT"),
    ("1 Kings", "1 Reyes", ["3 Kingdoms"], ["3 Reinos"], "OT"),
    ("2 Kings", "2 Reyes", ["4 Kingdoms"], ["4 Reinos", "2 R"], "OT"),
    ("1 Chronicles", "1 Crónicas", [], [], "OT"), ("2 Chronicles", "2 Crónicas", [], [], "OT"),
    ("Ezra", "Esdras", [], [], "OT"), ("Nehemiah", "Nehemías", [], [], "OT"),
    ("Esther", "Ester", [], [], "OT"), ("Job", "Job", [], [], "OT"),
    ("Psalms", "Salmos", ["Psalm", "Ps"], ["Salmo", "Sal"], "OT"),
    ("Proverbs", "Proverbios", [], [], "OT"), ("Ecclesiastes", "Eclesiastés", [], [], "OT"),
    ("Song of Songs", "Cantares", [], [], "OT"), ("Isaiah", "Isaías", [], [], "OT"),
    ("Jeremiah", "Jeremías", [], [], "OT"), ("Lamentations", "Lamentaciones", [], [], "OT"),
    ("Ezekiel", "Ezequiel", [], ["Ez"], "OT"), ("Daniel", "Daniel", [], [], "OT"),
    ("Hosea", "Oseas", [], [], "OT"), ("Joel", "Joel", [], [], "OT"),
    ("Amos", "Amós", [], [], "OT"), ("Obadiah", "Abdías", [], [], "OT"),
    ("Jonah", "Jonás", [], [], "OT"), ("Micah", "Miqueas", [], [], "OT"),
    ("Nahum", "Nahúm", [], [], "OT"), ("Habakkuk", "Habacuc", [], [], "OT"),
    ("Zephaniah", "Sofonías", [], [], "OT"), ("Haggai", "Hageo", [], [], "OT"),
    ("Zechariah", "Zacarías", [], [], "OT"), ("Malachi", "Malaquías", [], [], "OT"),
    ("Matthew", "Mateo", [], ["Mt"], "NT"), ("Mark", "Marcos", [], [], "NT"),
    ("Luke", "Lucas", [], [], "NT"), ("John", "Juan", [], [], "NT"),
    ("Acts", "Hechos", [], [], "NT"), ("Romans", "Romanos", [], [], "NT"),
    ("1 Corinthians", "1 Corintios", ["1 Cor"], [], "NT"),
    ("2 Corinthians", "2 Corintios", ["2 Cor"], [], "NT"),
    ("Galatians", "Gálatas", [], [], "NT"), ("Ephesians", "Efesios", ["Eph"], [], "NT"),
    ("Philippians", "Filipenses", [], [], "NT"), ("Colossians", "Colosenses", [], [], "NT"),
    ("1 Thessalonians", "1 Tesalonicenses", ["1 Thess"], ["1 Ts"], "NT"),
    ("2 Thessalonians", "2 Tesalonicenses", ["2 Thess"], ["2 Ts"], "NT"),
    ("1 Timothy", "1 Timoteo", [], [], "NT"), ("2 Timothy", "2 Timoteo", [], [], "NT"),
    ("Titus", "Tito", [], [], "NT"), ("Philemon", "Filemón", [], [], "NT"),
    ("Hebrews", "Hebreos", [], ["Heb"], "NT"), ("James", "Santiago", [], [], "NT"),
    ("1 Peter", "1 Pedro", [], [], "NT"), ("2 Peter", "2 Pedro", [], ["2 P"], "NT"),
    ("1 John", "1 Juan", [], [], "NT"), ("2 John", "2 Juan", [], [], "NT"),
    ("3 John", "3 Juan", [], [], "NT"), ("Jude", "Judas", [], [], "NT"),
    ("Revelation", "Apocalipsis", ["Rev"], ["Ap"], "NT"),
    ("1 Maccabees", "1 Macabeos", [], [], "X"), ("2 Maccabees", "2 Macabeos", [], [], "X"),
    ("1 Enoch", "1 Enoc", [], [], "X"), ("Jubilees", "Jubileos", [], [], "X"),
]

TEXT = {
    "en": {
        "title": "Appendix E — Scripture index",
        "heads": {"OT": "Hebrew Scriptures", "NT": "New Testament", "X": "Other ancient writings"},
        "intro": (
            "Every passage of Scripture this book cites by name, in canonical order, with the "
            "chapters where it appears. Numbers are chapters; letters are appendices; *FM* is the "
            "front matter. A verse discussed inside a chapter about its own book is sometimes "
            "cited without the book's name (\"20:3\"); those mentions are not listed separately. "
            "Psalms follow the Hebrew and English numbering. The Septuagint's 3 and 4 Kingdoms "
            "are listed under 1 and 2 Kings."),
    },
    "es": {
        "title": "Apéndice E — Índice bíblico",
        "heads": {"OT": "Escrituras hebreas", "NT": "Nuevo Testamento", "X": "Otros escritos antiguos"},
        "intro": (
            "Cada pasaje de las Escrituras que este libro cita por su nombre, en orden canónico, "
            "con los capítulos donde aparece. Los números son capítulos; las letras, apéndices; "
            "*PP* son las páginas preliminares. Un versículo comentado dentro de un capítulo "
            "dedicado a su propio libro a veces se cita sin el nombre del libro («20:3»); esas "
            "menciones no se enumeran por separado. Los Salmos siguen la numeración hebrea y de la "
            "Reina-Valera. Los libros 3 y 4 Reinos de la Septuaginta figuran como 1 y 2 Reyes."),
    },
}


def sources(lang: str):
    """(label, path) for every file the index covers, in book order."""
    fm = "FM" if lang == "en" else "PP"
    out = []
    for p in sorted((ROOT / lang).glob("00*.md")):
        out.append((fm, p))
    for p in sorted((ROOT / "matter-drafts" / lang).glob("00*.md")):
        out.append((fm, p))
    for p in sorted((ROOT / lang).glob("ch*.md")):
        out.append((str(int(re.match(r"ch(\d+)", p.name).group(1))), p))
    for p in sorted((ROOT / "matter-drafts" / lang).glob("zz-*.md")):
        m = re.match(r"zz-(?:appendix|apendice)-([a-g])-", p.name)
        if m:
            out.append((m.group(1).upper(), p))
    return out


def clean(text: str) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<[^>]+>", "", text)
    return text.replace(" ", " ").replace("*", "")


def book_pattern(lang: str):
    names = {}
    for en, es, en_al, es_al, _ in BOOKS:
        canon = en
        for n in ([en] + en_al) if lang == "en" else ([es] + es_al):
            names[n] = canon
    alts = sorted(names, key=len, reverse=True)
    return names, re.compile(r"(?<![\w])(" + "|".join(re.escape(a) for a in alts) + r")\.? (?=\d)")


SINGLE_CHAPTER = {"Obadiah", "Philemon", "2 John", "3 John", "Jude"}

DASH = "[–-]"
CV = re.compile(r"(\d{1,3})(?::(\d{1,3})[a-c]?(?:" + DASH + r"(\d{1,3})(?::(\d{1,3}))?)?)?(?:" + DASH + r"(\d{1,3}))?")


def parse_run(text: str, pos: int):
    """Parse '20:3, 8; 21:1–4' starting at pos. Returns list of (ch, v1, v2_or_None, ch_end) and end pos."""
    refs = []
    m = CV.match(text, pos)
    if not m:
        return refs, pos
    ch = int(m.group(1))
    refs.append(_ref(m))
    pos = m.end()
    while True:
        # same chapter: ", 8" (no colon), not followed by a capitalised word (another book)
        mv = re.match(r",\s?(\d{1,3})(?:" + DASH + r"(\d{1,3}))?(?![\d:])(?!\s*(?:[A-ZÁÉÍÓÚ]|\d+ [A-Z]))", text[pos:])
        if mv and refs[-1][1] is not None:
            refs.append((refs[-1][0], int(mv.group(1)), int(mv.group(2)) if mv.group(2) else None, None))
            pos += mv.end()
            continue
        mc = re.match(r"(?:;|,| and| y| ·)\s?(\d{1,3}):(\d{1,3})", text[pos:])
        if mc:
            m2 = CV.match(text, pos + mc.start(1))
            refs.append(_ref(m2))
            pos = m2.end()
            continue
        break
    return refs, pos


def _ref(m):
    ch = int(m.group(1))
    if m.group(2):  # ch:v[–v | –ch:v]
        v1 = int(m.group(2))
        if m.group(4):
            return (ch, v1, None, (int(m.group(3)), int(m.group(4))))
        return (ch, v1, int(m.group(3)) if m.group(3) else None, None)
    return (ch, None, None, (int(m.group(5)), None) if m.group(5) else None)  # chapter or ch–ch


def label(ref) -> str:
    ch, v1, v2, end = ref
    if v1 is None:
        return f"{ch}" if not end else f"{ch}–{end[0]}"
    if end:
        return f"{ch}:{v1}–{end[0]}:{end[1]}"
    return f"{ch}:{v1}" + (f"–{v2}" if v2 else "")


def sort_key(ref):
    ch, v1, v2, end = ref
    return (ch, v1 if v1 is not None else -1, v2 or 0, end or (0, 0))


def collect(lang: str):
    names, pat = book_pattern(lang)
    index = defaultdict(lambda: defaultdict(list))
    for lab, path in sources(lang):
        text = clean(path.read_text(encoding="utf-8"))
        for m in pat.finditer(text):
            canon = names[m.group(1)]
            refs, _ = parse_run(text, m.end())
            for r in refs:
                if canon in SINGLE_CHAPTER and r[1] is None:  # "Jude 23" is verse 23
                    r = (1, r[0], None, None)
                if r[0] > 150 or r[0] == 0:
                    continue
                locs = index[canon][r]
                if lab not in locs:
                    locs.append(lab)
    return index


def order_key(lab: str):
    if lab in ("FM", "PP"):
        return (0, 0)
    if lab.isdigit():
        return (1, int(lab))
    return (2, ord(lab))


def render(lang: str, index) -> str:
    t = TEXT[lang]
    out = ["---", f'title: "{t["title"]}"',
           "status: generated by scripts/build-scripture-index.py — do not edit by hand", "---", "",
           f"# {t['title']}", "", t["intro"], ""]
    for test in ("OT", "NT", "X"):
        books = [b for b in BOOKS if b[4] == test and b[0] in index]
        if not books:
            continue
        out += [f"## {t['heads'][test]}", ""]
        for en, es, *_ in books:
            name = en if lang == "en" else es
            entries = sorted(index[en], key=sort_key)
            lab = (lambda r: label(r)[2:]) if en in SINGLE_CHAPTER else label
            parts = [f"{lab(r)} ({', '.join(sorted(index[en][r], key=order_key))})" for r in entries]
            if len(entries) <= 25:
                out += [f"**{name}** — " + "; ".join(parts), ""]
                continue
            # long books: one line per biblical chapter, so the entry can be scanned
            out += [f"**{name}**", ""]
            by_ch = defaultdict(list)
            for r, part in zip(entries, parts):
                by_ch[r[0]].append(part)
            for ch in sorted(by_ch):
                out += [f"- " + "; ".join(by_ch[ch])]
            out += [""]
    return "\n".join(out)


def main():
    lang = sys.argv[1]
    index = collect(lang)
    if "--check" in sys.argv:
        n = sum(len(v) for v in index.values())
        print(f"{lang}: {len(index)} books, {n} distinct references")
        for en, *_ in BOOKS:
            if en in index:
                print(f"  {en}: {len(index[en])}")
        return
    sys.stdout.write(render(lang, index) + "\n")


if __name__ == "__main__":
    main()
