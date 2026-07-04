# FLAVA

Run the notebook from the repository root with the standard executor:

```bash
uv run python tools/execute_notebooks.py --model FLAVA --allow-large-downloads
```

To build the local notebook environment for interactive use:

```bash
cd FLAVA
uv sync
```

Then select `FLAVA/.venv/bin/python` as the notebook kernel.
