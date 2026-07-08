#!/usr/bin/env python3
"""Composite a foreground object onto a film-green background using a mask.

Keeps foreground pixels (where the mask is white) and replaces the background
(where the mask is black) with film-green RGB=(0, 255, 0). Soft mask edges are
blended, so anti-aliased masks give clean edges.

Usage:
    python composite_green.py ORIG_IMAGE MASK_IMAGE OUTPUT_DIR

Writes OUTPUT_DIR/<orig-stem>_green.png
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps

GREEN = (0, 255, 0)  # film-green


def main() -> None:
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)

    orig_path = Path(sys.argv[1])
    mask_path = Path(sys.argv[2])
    out_dir = Path(sys.argv[3])
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load foreground image (respect EXIF orientation), as RGB.
    img = ImageOps.exif_transpose(Image.open(orig_path)).convert("RGB")

    # Load mask as single-channel grayscale; match it to the image size.
    mask = Image.open(mask_path).convert("L")
    if mask.size != img.size:
        mask = mask.resize(img.size, Image.LANCZOS)

    img_a = np.asarray(img, dtype=np.float32)
    alpha = np.asarray(mask, dtype=np.float32)[..., None] / 255.0  # HxWx1 in [0,1]

    bg = np.empty_like(img_a)
    bg[:] = GREEN

    comp = img_a * alpha + bg * (1.0 - alpha)
    comp_img = Image.fromarray(np.clip(comp, 0, 255).astype(np.uint8), mode="RGB")

    out_path = out_dir / f"{orig_path.stem}_green.png"
    comp_img.save(out_path)
    print(f"Wrote {out_path}  ({comp_img.width}x{comp_img.height})")


if __name__ == "__main__":
    main()
