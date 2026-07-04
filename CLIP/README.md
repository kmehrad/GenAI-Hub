# CLIP

Run the notebook from the repository root with the standard executor:

```bash
uv run python tools/execute_notebooks.py --model CLIP --allow-large-downloads
```

To build the local notebook environment for interactive use:

```bash
cd CLIP
uv sync
```

Then select `CLIP/.venv/bin/python` as the notebook kernel.
