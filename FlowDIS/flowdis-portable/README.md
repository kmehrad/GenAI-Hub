# FlowDIS — portable setup bundle

Everything needed to run **FlowDIS** (FLUX.1-schnell foreground segmentation) on a fresh
Linux workstation, with or without a GPU. Copy this whole `flowdis-portable/` folder to the
target machine and run `setup.sh`.

The FlowDIS code here is **already patched** so the same code runs on GPU *and* CPU
(upstream is CUDA-only). Only the torch build differs between the two machines — `setup.sh`
handles that.

## What's in the bundle
```
flowdis-portable/
├── setup.sh            # one-shot env setup (gpu | cpu | auto-detect)
├── run.sh              # one-command pipeline: resize -> segment -> green composite
├── FlowDIS/            # patched FlowDIS repo (installed editable)
├── resize_images.py    # batch-resize inputs so the long side is <= 1024
├── composite_green.py  # composite foreground onto film-green (0,255,0) via a mask
└── README.md           # this file
```

## Requirements (both machines)
- **Linux**, `curl` available, and **internet access** (weights download from Hugging Face on
  first run — `PAIR/FlowDIS`, ~32 GB, cached under `~/.cache/huggingface`). Apache-2.0, no token.
- **~40 GB free disk** for the weights + venv. `setup.sh` needs no sudo (uses `uv`, which also
  fetches Python 3.12 if the system lacks it).

## Setup
```bash
cd flowdis-portable

# GPU workstation:
./setup.sh gpu

# CPU-only workstation:
./setup.sh cpu

# or let it auto-detect (nvidia-smi):
./setup.sh
```
This creates `flowdis-portable/flowdis-venv/`. Activate it before running:
```bash
source flowdis-venv/bin/activate
```
(To place the venv elsewhere, e.g. on a bigger disk: `VENV_DIR=/data/flowdis-venv ./setup.sh gpu`.)

### GPU machine notes
- Upstream needs **~48 GB VRAM** for 1024px (80 GB for higher res). If the GPU has less, a
  1024px run will OOM. Options: lower `--resolution` (e.g. 768/512), or force the CPU path on
  that box by hiding the GPU: `CUDA_VISIBLE_DEVICES="" python inference.py ...`.
- Multiple GPUs are used automatically (work is split across them).

### CPU machine notes
- Needs **~40 GB free RAM** (weights load in bf16 ≈ 34 GB). Runtime ≈ **~80 s/image** at
  1024px, 2 steps (it's a distilled few-step model). Lower `--resolution` to go faster.

## One-command pipeline (`run.sh`)
Does resize -> segment -> green-screen in a single step:
```bash
source flowdis-venv/bin/activate      # or run.sh will use the venv directly
./run.sh INPUT_DIR [OUTPUT_DIR] [RESOLUTION] [NUM_STEPS]

# e.g. process a folder of raw photos at defaults (out -> ./run-output, res 1024, 2 steps):
./run.sh images/
```
Creates under `OUTPUT_DIR` (default `./run-output`):
- `images-resized/` — inputs with long side <= 1024
- `masks/` — grayscale foreground masks (`<stem>.png`)
- `green/` — foreground on film-green (`<stem>_green.png`)

For manual/step-by-step control, use the individual commands below instead.

## Running inference
```bash
source flowdis-venv/bin/activate    # if not already active

python FlowDIS/inference.py \
    --images-dir  /path/to/images-resized \
    --output-dir  /path/to/out \
    --num-steps   2 \
    --resolution  1024
```
- Processes every `.jpg/.jpeg/.png` in `--images-dir` (recursively). One grayscale mask per
  image is written to `--output-dir` as `<stem>.png` (white = foreground).
- Optional text guidance: `--prompts-json file.json` where the JSON maps `"<image filename>"`
  to a prompt string, e.g. `{"bird.jpg": "the bird"}`.
- `--num-samples N` limits how many images are processed.
- First run downloads the weights (~32 GB); later runs start immediately from cache.
  To cache elsewhere: `export HF_HOME=/data/hf` before running.

## Helper scripts
```bash
# 1) Resize inputs so the longest side is <= 1024 (keeps aspect ratio; never upscales)
python resize_images.py images/ images-resized/ 1024

# 2) Green-screen a result: keep foreground, fill background with film-green (0,255,0)
python composite_green.py  ORIG_IMAGE  MASK_IMAGE  OUTPUT_DIR
# writes OUTPUT_DIR/<orig-stem>_green.png   (mask stem matches the image, but .png)
```
`resize_images.py` and `composite_green.py` only need **Pillow + numpy**, which the venv
already has after `setup.sh` (they come in with the FlowDIS deps).

## Typical end-to-end flow
```bash
source flowdis-venv/bin/activate
python resize_images.py images/ images-resized/ 1024
python FlowDIS/inference.py --images-dir images-resized --output-dir out --num-steps 2 --resolution 1024
python composite_green.py images-resized/bird.jpg out/bird.png green/
```
