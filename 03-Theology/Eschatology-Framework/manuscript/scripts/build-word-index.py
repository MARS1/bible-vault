#!/usr/bin/env python3
"""Generate Appendix D2 (every other Hebrew, Aramaic and Greek word cited) into the D file.

    python3 scripts/build-word-index.py en
    python3 scripts/build-word-index.py es

Rewrites everything after the D2-GENERATED marker in the language's Appendix D
file. A word is any original-language span followed by its transliteration,
"<span class=gr|he>…</span> (*translit*". Words that already have a D1 entry
(their transliteration appears in a D1 heading) are left out. Locations use the
same labels as the scripture index (build-scripture-index.py).
"""
import importlib.util
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("si", ROOT / "scripts" / "build-scripture-index.py")
si = importlib.util.module_from_spec(spec)
spec.loader.exec_module(si)

D_FILE = {"en": ROOT / "matter-drafts/en/zz-appendix-d-word-studies.md",
          "es": ROOT / "matter-drafts/es/zz-apendice-d-estudios-de-palabras.md"}
MARKER = "<!-- D2-GENERATED"
HEADS = {"en": ("Hebrew and Aramaic", "Greek"), "es": ("Hebreo y arameo", "Griego")}
TERM = re.compile(r'<span class="(gr|he)">([^<]{1,60})</span>\s*\(\*([^*]{1,40})\*')


def fold(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c) and c.isalnum() or c == " ").strip()


def d1_translits(text: str) -> set:
    d1 = text.split(MARKER)[0]
    return {fold(m.group(3)) for m in TERM.finditer(d1)}


def collect(lang: str, skip: set):
    words = defaultdict(lambda: {"form": None, "cls": None, "locs": []})
    for lab, path in si.sources(lang):
        if path == D_FILE[lang]:
            continue
        text = re.sub(r"^---\n.*?\n---\n", "", path.read_text(encoding="utf-8"), flags=re.S)
        text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        for m in TERM.finditer(text):
            key = fold(m.group(3))
            if not key or key in skip:
                continue
            w = words[key]
            if w["form"] is None:
                w["form"], w["cls"], w["tr"] = m.group(2).strip(), m.group(1), m.group(3).strip()
            if lab not in w["locs"]:
                w["locs"].append(lab)
    return words


def render(lang: str, words) -> str:
    out = []
    for cls, head in zip(("he", "gr"), HEADS[lang]):
        group = sorted((k for k in words if words[k]["cls"] == cls), key=lambda k: k)
        if not group:
            continue
        out += [f"### {head}", ""]
        by_letter = defaultdict(list)
        for k in group:
            w = words[k]
            locs = ", ".join(sorted(w["locs"], key=si.order_key))
            by_letter[k[0].upper()].append(
                f'<span class="{cls}">{w["form"]}</span> (*{w["tr"]}*) {locs}')
        for letter in sorted(by_letter):
            out += [f"**{letter}** — " + "; ".join(by_letter[letter]), ""]
    return "\n".join(out)


def main():
    lang = sys.argv[1]
    path = D_FILE[lang]
    text = path.read_text(encoding="utf-8")
    if MARKER not in text:
        sys.exit(f"{path.name}: no {MARKER} marker")
    head, marker_line = text.split(MARKER)[0], MARKER + text.split(MARKER)[1].splitlines()[0]
    words = collect(lang, d1_translits(text))
    path.write_text(head + marker_line + "\n\n" + render(lang, words) + "\n", encoding="utf-8")
    print(f"{path.name}: {len(words)} D2 words")


if __name__ == "__main__":
    main()
