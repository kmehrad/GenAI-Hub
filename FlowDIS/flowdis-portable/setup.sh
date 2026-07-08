#!/usr/bin/env bash
# FlowDIS environment setup for a fresh Linux workstation (GPU or CPU-only).
#
# Usage:  ./setup.sh [gpu|cpu]
#   gpu  -> installs the CUDA build of torch  (needs an NVIDIA GPU; ~48GB VRAM for 1024px)
#   cpu  -> installs the CPU-only build        (needs ~40GB free RAM for the weights)
#   (no arg) -> auto-detects via nvidia-smi
#
# No sudo required: uses `uv` (auto-installed to ~/.local/bin) which also fetches
# Python 3.12 if the system doesn't have it. Creates a venv next to this script.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${VENV_DIR:-$SCRIPT_DIR/flowdis-venv}"

MODE="${1:-auto}"
if [ "$MODE" = "auto" ]; then
  if command -v nvidia-smi >/dev/null 2>&1 && nvidia-smi -L >/dev/null 2>&1; then
    MODE="gpu"
  else
    MODE="cpu"
  fi
fi
echo ">> Setup mode: $MODE"

# 1. Ensure uv is available (installs to ~/.local/bin, no sudo).
if ! command -v uv >/dev/null 2>&1; then
  echo ">> Installing uv (no sudo)..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi
export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
command -v uv >/dev/null 2>&1 || { echo "ERROR: uv not on PATH after install"; exit 1; }

# 2. Create the venv with Python 3.12 (uv downloads it if the system lacks it).
echo ">> Creating venv at $VENV_DIR"
uv venv "$VENV_DIR" --python 3.12
PY="$VENV_DIR/bin/python"

# 3. Install torch (build depends on mode), then the FlowDIS package (editable).
if [ "$MODE" = "gpu" ]; then
  echo ">> Installing CUDA build of torch..."
  uv pip install --python "$PY" torch torchvision
else
  echo ">> Installing CPU-only build of torch..."
  uv pip install --python "$PY" torch torchvision --index-url https://download.pytorch.org/whl/cpu
fi
uv pip install --python "$PY" -e "$SCRIPT_DIR/FlowDIS"

# 4. Verify.
echo ">> Verifying torch..."
"$PY" -c "import torch; print('torch', torch.__version__, '| cuda available:', torch.cuda.is_available())"

cat <<EOF

>> Setup complete ($MODE).
   Activate the environment with:
       source "$VENV_DIR/bin/activate"
   Then see README.md for how to run inference.
EOF
