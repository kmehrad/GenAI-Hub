#!/usr/bin/env bash
# End-to-end FlowDIS pipeline: resize -> segment -> green-screen composite.
#
# Usage:  ./run.sh INPUT_DIR [OUTPUT_DIR] [RESOLUTION] [NUM_STEPS]
#   INPUT_DIR   folder of raw images (jpg/jpeg/png)                 (required)
#   OUTPUT_DIR  where results go                     (default: ./run-output)
#   RESOLUTION  segmentation resolution              (default: 1024)
#   NUM_STEPS   inference steps                       (default: 2)
#
# Produces, under OUTPUT_DIR:
#   images-resized/   inputs resized so the long side is <= 1024
#   masks/            grayscale foreground masks   (<stem>.png)
#   green/            foreground on film-green     (<stem>_green.png)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${VENV_DIR:-$SCRIPT_DIR/flowdis-venv}"

INPUT_DIR="${1:?Usage: ./run.sh INPUT_DIR [OUTPUT_DIR] [RESOLUTION] [NUM_STEPS]}"
OUTPUT_DIR="${2:-$SCRIPT_DIR/run-output}"
RESOLUTION="${3:-1024}"
NUM_STEPS="${4:-2}"

RESIZED_DIR="$OUTPUT_DIR/images-resized"
MASK_DIR="$OUTPUT_DIR/masks"
GREEN_DIR="$OUTPUT_DIR/green"

PY="$VENV_DIR/bin/python"
[ -x "$PY" ] || { echo "ERROR: venv not found at $VENV_DIR. Run ./setup.sh first."; exit 1; }

mkdir -p "$RESIZED_DIR" "$MASK_DIR" "$GREEN_DIR"

echo ">> [1/3] Resizing images from $INPUT_DIR (long side <= 1024)..."
"$PY" "$SCRIPT_DIR/resize_images.py" "$INPUT_DIR" "$RESIZED_DIR" 1024

echo ">> [2/3] Running FlowDIS inference (resolution=$RESOLUTION, steps=$NUM_STEPS)..."
"$PY" "$SCRIPT_DIR/FlowDIS/inference.py" \
    --images-dir "$RESIZED_DIR" \
    --output-dir "$MASK_DIR" \
    --num-steps "$NUM_STEPS" \
    --resolution "$RESOLUTION"

echo ">> [3/3] Compositing foreground onto film-green background..."
shopt -s nullglob nocaseglob
for img in "$RESIZED_DIR"/*.jpg "$RESIZED_DIR"/*.jpeg "$RESIZED_DIR"/*.png; do
    stem="$(basename "${img%.*}")"
    mask="$MASK_DIR/$stem.png"
    if [ -f "$mask" ]; then
        "$PY" "$SCRIPT_DIR/composite_green.py" "$img" "$mask" "$GREEN_DIR"
    else
        echo "   (skip $stem: no mask found)"
    fi
done
shopt -u nocaseglob

echo ""
echo ">> Done. Results in:"
echo "     resized : $RESIZED_DIR"
echo "     masks   : $MASK_DIR"
echo "     green   : $GREEN_DIR"
