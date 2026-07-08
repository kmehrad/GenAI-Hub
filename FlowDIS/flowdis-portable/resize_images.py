#!/usr/bin/env python3
"""Resize images so the longest side is <= MAX_SIZE, preserving aspect ratio.

Usage:
    python resize_images.py [SRC_DIR] [DST_DIR] [MAX_SIZE]

Defaults: SRC_DIR=images, DST_DIR=images-resized, MAX_SIZE=1024.
Images already within the limit are copied (re-saved) unchanged in size.
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("images")
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("images-resized")
    max_size = int(sys.argv[3]) if len(sys.argv) > 3 else 1024

    dst.mkdir(parents=True, exist_ok=True)

    paths = sorted(p for p in src.iterdir() if p.is_file() and p.suffix.lower() in EXTS)
    if not paths:
        print(f"No images found in {src}/")
        return

    for path in paths:
        with Image.open(path) as im:
            # Honor EXIF orientation (phone photos) so W/H match what you see.
            im = ImageOps.exif_transpose(im)
            w, h = im.size
            scale = min(max_size / max(w, h), 1.0)  # never upscale
            new_w, new_h = max(1, round(w * scale)), max(1, round(h * scale))
            if scale < 1.0:
                im = im.resize((new_w, new_h), Image.LANCZOS)

            out_path = dst / path.name
            save_im = im.convert("RGB") if path.suffix.lower() in {".jpg", ".jpeg"} else im
            save_im.save(out_path)
            print(f"{path.name}: {w}x{h} -> {new_w}x{new_h}")

    print(f"\nDone. {len(paths)} image(s) written to {dst}/ (max side <= {max_size}px).")


if __name__ == "__main__":
    main()
