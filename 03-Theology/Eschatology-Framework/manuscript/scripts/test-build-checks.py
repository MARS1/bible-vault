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

print("\nsource_words — count what the reader sees, not markdown")
# 2026-10-10: Part VIII reader revision failed the word-recovery band with no text
# missing. Table pipes, <span> openers and ::: fences were counted as words.
check("table row counts cells, not pipes", bm.source_words("| Verse | Said of |"), 3)
check("separator row counts nothing", bm.source_words("|------|:---:|"), 0)
check("span counts its text only", bm.source_words('<span class="gr">μικρὸν χρόνον</span> (*mikron*)'), 3)
check("fence lines count nothing", bm.source_words("::: finding\n**Label**\n:::"), 1)
check("plain prose unchanged", bm.source_words("The end is not yet."), 5)

print("\ncheck_normalization — Book One rules (BIBLE-3c7); calibrated to zero on Parts VIII-IX")
# 2026-10-13: first calibration against the approved benchmark flagged 37 legitimate
# gloss forms in Part VIII. Each form the benchmark uses is pinned here so the checker
# can never again demand that approved prose change to satisfy it.
def norm_hits(text, cat):
    p = in_tmp(text); n = len(bm.check_normalization([p])[cat]); p.unlink(); return n
GR = lambda s: f'<span class="gr">{s}</span>'
for label, text, cat, want in [
    ("emoji flagged",                       "✅ settled", "decor", 1),
    ("star flagged",                        "★ key point", "decor", 1),
    ("plain arrows NOT flagged",            "a → b ↓ c ≈ d", "decor", 0),
    ("left arrow NOT flagged (ch21 chain)", "call ← believe ← hear", "decor", 0),
    ("check mark flagged",                  "| first | earth ✓ |", "decor", 1),
    ("'Tier B' internal label flagged",     "Recorded as a Tier B inference", "label", 1),
    ("historical title with suffix flagged","::: historical\n**Historical context — the Jerusalem Council**", "convention", 1),
    ("unstyled grade flagged",              "This is at SUPPORTS.", "grade", 1),
    ("styled grade NOT flagged",            'at <span class="grade">supports</span>', "grade", 0),
    ("ES unstyled grade flagged",           "queda en APOYA", "grade", 1),
    ("lowercase 'supports' prose NOT flagged", "the text supports it", "grade", 0),
    ("visible Stage number flagged",        "As Stage 61 showed", "label", 1),
    ("visible scope label flagged",         "**SOURCE-LANGUAGE** note", "label", 1),
    ("label inside HTML comment NOT flagged","<!-- SPANISH-SPECIFIC: x -->", "label", 0),
    ("unglossed term flagged",              f"the word {GR('πόλεμος')} here", "gloss", 1),
    ("term (*translit*) accepted",          f"{GR('πόλεμος')} (*polemos*, war)", "gloss", 0),
    ("(term, *translit*) accepted",         f'"war" ({GR("πόλεμος")}, *polemos*)', "gloss", 0),
    ("*translit* (term) accepted",          f"*Armageddon* ({GR('Ἁρμαγεδών')})", "gloss", 0),
    ("3+ word clause = quotation, exempt",  f"Greek: {GR('καὶ κατέβη πῦρ')} — \"and fire\"", "gloss", 0),
    ("blockquoted verse exempt",            f"> {GR('πόλεμος')}", "gloss", 0),
    ("word-study header form accepted",     f"{GR('κοινός')} · *koinos* · common, ordinary", "gloss", 0),
    ("table row exempt",                    f"| 20:3 | {GR('μικρὸν χρόνον')} | *mikros* |", "gloss", 0),
    ("second use after gloss NOT flagged",  f"{GR('πόλεμος')} (*polemos*)\nagain {GR('πόλεμος')}", "gloss", 0),
    ("second chapter heading flagged",      "# Chapter 1: a\n\n# Chapter 2: b", "structure", 1),
    ("Coda heading allowed",                "# Chapter 54: a\n\n# Coda: b", "structure", 0),
    ("paragraph opening (a) flagged",       "text\n\n(a) First option. (b) Second.", "structure", 1),
    ("escaped \\(a) NOT flagged",            "text\n\n\\(a) First option. (b) Second.", "structure", 0),
    ("#### heading flagged",                "#### too deep", "structure", 1),
    # 2026-10-13: stage-talk without a number was invisible to the numbered pattern,
    # and it had survived even the Part VIII revision ("fifty-eight stages", ch47/ch49).
    ("'five stages' flagged",               "I had spent five stages on it", "label", 1),
    ("'fifty-eight stages' flagged",        "across the preceding fifty-eight stages", "label", 1),
    ("'two-stage structure' NOT flagged",   "the two-stage structure of 20:5", "label", 0),
    ("ES 'dos etapas' (Rev 20:5) NOT flagged", "la estructura en dos etapas del pasaje", "label", 0),
    ("old box label flagged",               "**Where we are.** text", "convention", 1),
    ("old earned label flagged",            "**What it earned.** text", "convention", 1),
    ("ES old label flagged",                "**Qué se ganó.** texto", "convention", 1),
    ("benchmark label NOT flagged",         "**Where this leaves us.** text", "convention", 0),
    ("body rule flagged",                   "text\n\n---\n\n::: whereweare", "convention", 1),
    # 2026-10-13: Parts II-VII reuse fixed captions; Part VIII-IX boxes name their content.
    ("generic evidence title flagged",      "::: evidence\n**How strongly evidence bears**", "convention", 1),
    ("generic wordstudy title flagged",     "::: wordstudy\n**Original language**", "convention", 1),
    ("ES 'deuda declarada' caption flagged","::: textualnote\n**Nota textual — deuda declarada**", "convention", 1),
    ("generic title with suffix flagged",   "::: evidence\n**Con qué fuerza pesa la evidencia — contraevidencia, impresa**", "convention", 1),
    ("descriptive 'Finding — …' NOT flagged","::: finding\n**Finding — Daniel moves between ruler and realm**", "convention", 0),
    ("benchmark descriptive title NOT flagged","::: evidence\n**The purpose formula, four times**", "convention", 0),
    ("ES 'pequeña temporada' drift flagged","la pequeña temporada se convierte en la lente", "convention", 1),
    ("ES 'el poco de tiempo' NOT flagged",  "el poco de tiempo se convierte en la lente", "convention", 0),
    ("debt metaphor flagged",               "**A debt paid before the argument leaned on it**", "label", 1),
    ("ES deuda flagged",                    "una deuda declarada", "label", 1),
    # 2026-10-13: Part II ch11 "the strongest argument this project has produced" passed
    # the checker and was caught by the reviewer.
    ("'this project' flagged",              "the strongest argument this project has produced", "label", 1),
    ("ES 'este proyecto' flagged",          "la primera frase de este proyecto", "label", 1),
    # 2026-10-14: chain titles were normalized in Part II only; Part V-VI kept the old form.
    ("old chain title flagged",             "::: chain\n**Growing Chain — Checkpoint 3**", "convention", 1),
    ("ES old chain title flagged",          "::: chain\n**Cadena creciente — Punto de control 3**", "convention", 1),
    ("benchmark chain title NOT flagged",   "::: chain\n**The growing chain — checkpoint 3**", "convention", 0),
    ("ES benchmark chain title NOT flagged","::: chain\n**La cadena creciente — punto de control 2**", "convention", 0),
]:
    check(label, norm_hits(text, cat), want)

print()
if FAILS:
    print("FAILURES:"); [print("  " + f) for f in FAILS]; sys.exit(1)
print("all build-check regression tests pass")
