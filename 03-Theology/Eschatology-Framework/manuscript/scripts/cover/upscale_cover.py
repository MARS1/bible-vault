#!/usr/bin/env python3
"""Upscale the chosen cover art 4x with AuraSR on Fal.ai (faithful GAN upscaler, no repainting).

Run it yourself in your own terminal:
    cd /Volumes/VM/OBSIDIAN/BIBLE/03-Theology/Eschatology-Framework/manuscript && python3 scripts/cover/upscale_cover.py

The key is read from FAL_KEY, or asked for with hidden input. It is never printed,
logged or saved. Endpoint and parameters checked on fal.ai/models/fal-ai/aura-sr/api,
2026-10-16. Output: 832x1248 -> 3328x4992 (enough for 6x9in + bleed at 300dpi).
"""
import getpass
import json
import os
import sys
import urllib.request
from pathlib import Path

COVER = Path.home() / "Desktop" / "7-MARS" / "Bible Study" / "Cover"
SRC = COVER / "round-1" / "ideogram-v3-3.png"
OUT = COVER / "final" / "ideogram-v3-3-aurasr-4x.png"


def main() -> None:
    import fal_client
    if OUT.exists():
        sys.exit(f"{OUT} already exists; not overwriting.")
    if not os.environ.get("FAL_KEY"):
        key = getpass.getpass("Fal API key (input hidden, not saved): ").strip()
        if not key:
            sys.exit("No key entered; nothing uploaded.")
        os.environ["FAL_KEY"] = key
    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("Uploading source image...")
    url = fal_client.upload_file(str(SRC))
    print("Upscaling 4x with AuraSR (overlapping tiles on, takes a little longer)...")
    res = fal_client.subscribe("fal-ai/aura-sr", arguments={
        "image_url": url, "upscale_factor": 4, "overlapping_tiles": True})
    img = res["image"]
    with urllib.request.urlopen(img["url"], timeout=300) as r:  # nosec: Fal CDN URL from the API
        OUT.write_bytes(r.read())
    (OUT.parent / "upscale-settings.json").write_text(json.dumps({
        "source": str(SRC), "model": "fal-ai/aura-sr", "upscale_factor": 4,
        "overlapping_tiles": True, "width": img.get("width"), "height": img.get("height")}, indent=2))
    print(f"Saved {OUT} ({img.get('width')}x{img.get('height')})")


if __name__ == "__main__":
    main()
