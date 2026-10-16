#!/usr/bin/env python3
"""Typeset front-cover mockups (EN + ES) over a chosen artwork with Pillow.

Pillow, not WeasyPrint, per the KodeArk lesson on full-bleed pages.
Trim 6x9in + 0.125in bleed at 300dpi = 1875x2775px. The artwork is resized to
that size here for layout only. The print cover uses the upscaled art.

    python3 scripts/cover/make_cover_mockup.py <artwork> <out-dir> [version-tag]
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1875, 2775           # 6.25 x 9.25 in at 300dpi (trim plus bleed)
BLEED = 38                  # 0.125in
SAFE = BLEED + 112          # keep type ~0.5in inside trim
CREAM = (243, 235, 221)
SHIFT = 260  # px the art is raised for ideogram-v3-3; 0 = as generated
FONT = "/System/Library/Fonts/Supplemental/Baskerville.ttc"   # 0 Regular, 2 Italic, 4 SemiBold

EDITIONS = {
    "en": {"title": ["The Promise", "and the", "Little Season"],
           "subtitle": ["An investigation into prophecy,", "the great commission, and the thousand years"],
           "author": "Marcelo Mario Berta Silva",
           "imprint": "Bright Forest Publishing", "site": "kollabs.ai"},
    "es": {"title": ["La promesa", "y el", "poco de tiempo"],
           "subtitle": ["Una investigación sobre la profecía,", "la gran comisión y los mil años"],
           "author": "Marcelo Mario Berta Silva",
           "imprint": "Bright Forest Publishing", "site": "kollabs.ai"},
}


def font(size: int, index: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT, size, index=index)


def centered(draw: ImageDraw.ImageDraw, y: int, text: str, f: ImageFont.FreeTypeFont, fill, track: int = 0) -> int:
    if track:
        widths = [draw.textlength(c, font=f) for c in text]
        total = sum(widths) + track * (len(text) - 1)
        x = (W - total) / 2
        for c, w in zip(text, widths):
            draw.text((x, y), c, font=f, fill=fill)
            x += w + track
    else:
        draw.text(((W - draw.textlength(text, font=f)) / 2, y), text, font=f, fill=fill)
    box = f.getbbox(text)
    return y + (box[3] - box[1])


def compose(art: Path, lang: str) -> Image.Image:
    art_img = Image.open(art).convert("RGB").resize((W, H), Image.LANCZOS)
    # Raise the tree without enlarging it (author request 2026-10-16): shift the
    # art up by SHIFT px and extend the hill below with a blurred stretch of its
    # own bottom rows; the footer scrim covers that band.
    img = Image.new("RGB", (W, H))
    img.paste(art_img, (0, -SHIFT))
    if SHIFT:
        base = art_img.crop((0, H - 80, W, H)).resize((W, SHIFT), Image.LANCZOS)
        img.paste(base.filter(ImageFilter.GaussianBlur(18)), (0, H - SHIFT))
    d = ImageDraw.Draw(img)
    e = EDITIONS[lang]
    big, small = font(176, 0), font(92, 2)
    y = SAFE + 150
    y = centered(d, y, e["title"][0], big, CREAM) + 40
    y = centered(d, y, e["title"][1], small, CREAM) + 40
    y = centered(d, y, e["title"][2], big, CREAM) + 120
    rule_w = 260
    d.line([((W - rule_w) / 2, y), ((W + rule_w) / 2, y)], fill=CREAM, width=3)
    y += 70
    sub = font(58, 2)
    for line in e["subtitle"]:
        y = centered(d, y, line, sub, CREAM) + 26
    # Footer sits on a soft scrim (transparent -> deep indigo) so it reads over the hill.
    scrim_top = H - 520
    grad = Image.new("L", (1, 520))
    for i in range(520):
        grad.putpixel((0, i), int(205 * (i / 519) ** 1.6))
    shade = Image.new("RGB", (W, 520), (20, 26, 34))
    img.paste(shade, (0, scrim_top), grad.resize((W, 520)))
    d = ImageDraw.Draw(img)
    author = font(64, 4)
    y = centered(d, H - SAFE - 175, e["author"].upper(), author, CREAM, track=6) + 44
    # Imprint: a name, not a legal entity. No "Co." or "LLC" (PUBLISHING-PREP-NOTES P7).
    y = centered(d, y, e["imprint"].upper(), font(36, 0), CREAM, track=8) + 20
    centered(d, y, e["site"], font(34, 2), CREAM)
    return img


def main() -> None:
    art, out = Path(sys.argv[1]), Path(sys.argv[2])
    tag = sys.argv[3] if len(sys.argv) > 3 else "v1"
    out.mkdir(parents=True, exist_ok=True)
    for lang in EDITIONS:
        p = out / f"cover-mockup-{lang}-{tag}.png"
        if p.exists():
            sys.exit(f"{p} exists; use a new version tag")
        compose(art, lang).save(p, dpi=(300, 300))
        print("saved", p)


if __name__ == "__main__":
    main()
