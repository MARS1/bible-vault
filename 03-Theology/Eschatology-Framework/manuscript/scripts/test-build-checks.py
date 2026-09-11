#!/usr/bin/env python3
"""Regression tests for build-manuscript.py's verification checks.

Every test here exists because a check was WRONG once, in a way that would have
either shipped a defect or blocked a correct chapter. Run: python3 scripts/test-build-checks.py
"""
import importlib.util, tempfile, sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("bm", str(Path(__file__).with_name("build-manuscript.py")))
bm = importlib.util.module_from_spec(spec); spec.loader.exec_module(bm)

FAILS = []

def check(name, got, want):
    if got != want:
        FAILS.append(f"{name}: got {got!r}, want {want!r}")
    print(f"  {'PASS' if got == want else 'FAIL <<<'}  {name}")

def in_tmp(text):
    fh = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
    fh.write(text); fh.close()
    return Path(fh.name)

print("\n_norm — smart quotes must not cause a false MISSING SECTION")
# 2026-09-11: Part III ch19's approved title contains straight quotes. Pandoc renders
# them curly, so the byte-for-byte comparison reported the chapter missing from its
# own PDF. The checker was wrong; the chapter was correct.
src   = 'Chapter 19: who are "the people of God"? - and what are we trying to determine?'
pdfed = 'Chapter 19: who are “the people of God”? — and what are we trying to determine?'
check("curly-quote heading matches straight-quote source", bm._norm(src) in bm._norm(pdfed), True)
check("em dash normalizes to hyphen", bm._norm("a — b"), "a - b")
check("apostrophe normalizes", bm._norm("Peter’s"), "Peter's")
check("unrelated text still fails to match", bm._norm("a different heading") in bm._norm(pdfed), False)

print("\ncheck_terminology — no modern cosmology in a lexical explanation (both editions)")
# 2026-09-11: the rule lived only in frontmatter strings and was enforced by memory.
# Three violations reached Spanish Part II AND one reached the cleared English baseline.
for label, line, want in [
    ("ES 'el planeta entero'",     "Puede significar el planeta entero.", True),
    ("EN 'on the planet'",         "every nation on the planet", True),
    ("'global'",                   "a global reading", True),
    ("'mundial'",                  "un alcance mundial", True),
    ("'worldwide'",                "preached worldwide", True),
    ("RVR quote 'todo el mundo'",  "> en todo el mundo, para testimonio", False),
    ("prose 'todo el mundo'",      "predicado en todo el mundo", False),
    ("'de la tierra'",             "todas las naciones de la tierra", False),
    ("frontmatter stating rule",   'localization: "TERMINOLOGIA: no planeta"', False),
]:
    p = in_tmp(line); check(label, bool(bm.check_terminology([p])), want); p.unlink()

print("\ncheck_prose_vosotros — narration only; RVR1960 quotations are untouched")
for label, line, want in [
    ("prose vosotros flagged",        "y vosotros sabéis que", True),
    ("quoted vosotros NOT flagged",   "> desde ahora veréis, vosotros", False),
    ("mention of the pronoun flagged","ese *vosotros* se desplaza", True),
]:
    p = in_tmp(line); check(label, bool(bm.check_prose_vosotros([p])), want); p.unlink()

print("\ncheck_es_register — regionalisms in prose only")
for label, line, want in [
    ("'acá' flagged",              "vine acá para decirlo", True),
    ("'acá' inside a quotation",   "> y vino acá", False),
    ("clean prose",                "vine aquí para decirlo", False),
]:
    p = in_tmp(line); check(label, bool(bm.check_es_register([p])), want); p.unlink()

print()
if FAILS:
    print("FAILURES:"); [print("  " + f) for f in FAILS]; sys.exit(1)
print("all build-check regression tests pass")
