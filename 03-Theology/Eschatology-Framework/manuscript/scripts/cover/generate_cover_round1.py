#!/usr/bin/env python3
"""Cover art, round 1: 4 images each from Ideogram v3 and FLUX 1.1 Pro Ultra (Fal.ai).

Run it yourself in your own terminal:
    cd /Volumes/VM/OBSIDIAN/BIBLE/03-Theology/Eschatology-Framework/manuscript && python3 scripts/cover/generate_cover_round1.py

The Fal key is read from the FAL_KEY environment variable. If it is not set,
the script asks for it with hidden input (getpass). The key is never printed,
logged or written to disk; it only lives in this process's environment.

Images and a settings log (models, seeds, prompt, no key) go to
~/Desktop/7-MARS/Bible Study/Cover/round-1/.
Model ids and parameters checked against fal.ai API pages, 2026-10-16.
"""
import getpass
import json
import os
import random
import sys
import urllib.request
from pathlib import Path

PROMPT = (
    "Fine-art book cover illustration, portrait 2:3. A single ancient olive tree on a quiet "
    "hillside in the land of Israel at dusk: gnarled trunk, silver-green leaves, one younger "
    "branch grafted into the old trunk, slightly lighter in tone. Above it, a deep indigo evening "
    "sky with the first scattered stars appearing, and a thin warm band of ochre light along the "
    "horizon. Contemplative, reverent, still. Painterly texture like a classical oil study, "
    "restrained detail, with a generous open sky in the upper third for the title. Muted palette "
    "of indigo, olive green, warm ochre and cream. No people, no text, no letters, no symbols, "
    "no fire, no lightning, no fantasy elements."
)
NEGATIVE = ("text, letters, words, typography, watermark, signature, people, figures, fire, flames, "
            "lightning, red sky, fantasy, glowing symbols, maps, numbers")
PER_MODEL = 4
OUT = Path.home() / "Desktop" / "7-MARS" / "Bible Study" / "Cover" / "round-1"


def ensure_key() -> None:
    if not os.environ.get("FAL_KEY"):
        key = getpass.getpass("Fal API key (input hidden, not saved): ").strip()
        if not key:
            sys.exit("No key entered; nothing generated.")
        os.environ["FAL_KEY"] = key


def download(url: str, dest: Path) -> None:
    with urllib.request.urlopen(url, timeout=120) as r:  # nosec: Fal CDN URL returned by the API
        dest.write_bytes(r.read())


def run_ideogram(fal_client, n: int, log: list) -> None:
    seed = random.randint(1, 2**31 - 1)
    args = {"prompt": PROMPT, "negative_prompt": NEGATIVE, "num_images": n,
            "image_size": {"width": 1024, "height": 1536},  # 2:3
            "rendering_speed": "QUALITY", "style": "GENERAL", "expand_prompt": False, "seed": seed}
    try:
        res = fal_client.subscribe("fal-ai/ideogram/v3", arguments=args)
    except Exception as e:  # custom size rejected: fall back to the 3:4 preset
        print(f"  Ideogram custom 2:3 size failed ({type(e).__name__}); retrying with portrait_4_3")
        args["image_size"] = "portrait_4_3"
        res = fal_client.subscribe("fal-ai/ideogram/v3", arguments=args)
    save(res, "ideogram-v3", args, log)


def run_flux(fal_client, n: int, log: list) -> None:
    for i in range(n):  # one call per image so each has its own recorded seed
        seed = random.randint(1, 2**31 - 1)
        args = {"prompt": PROMPT, "num_images": 1, "aspect_ratio": "2:3",
                "output_format": "png", "raw": False, "enhance_prompt": False, "seed": seed}
        res = fal_client.subscribe("fal-ai/flux-pro/v1.1-ultra", arguments=args)
        save(res, f"flux-ultra-{i + 1}", args, log)


def save(res: dict, tag: str, args: dict, log: list) -> None:
    for j, img in enumerate(res.get("images", []), 1):
        ext = ".png" if "png" in (img.get("content_type") or img["url"]) else ".jpg"
        name = f"{tag}-{j}{ext}" if tag == "ideogram-v3" else f"{tag}{ext}"
        download(img["url"], OUT / name)
        log.append({"file": name, "model": tag, "seed": res.get("seed", args.get("seed")),
                    "width": img.get("width"), "height": img.get("height"),
                    "args": {k: v for k, v in args.items() if k != "prompt"}})
        print(f"  saved {name} ({img.get('width')}x{img.get('height')})")


def main() -> None:
    import fal_client
    ensure_key()
    OUT.mkdir(parents=True, exist_ok=True)
    log: list = []
    print("Ideogram v3 (4 images)...")
    run_ideogram(fal_client, PER_MODEL, log)
    print("FLUX 1.1 Pro Ultra (4 images)...")
    run_flux(fal_client, PER_MODEL, log)
    (OUT / "settings.json").write_text(json.dumps({"prompt": PROMPT, "negative_prompt": NEGATIVE,
                                                   "images": log}, indent=2))
    print(f"Done: {len(log)} images in {OUT}")


if __name__ == "__main__":
    main()
