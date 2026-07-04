# AuraSR

Run the notebook from the repository root with the standard executor:

```bash
uv run python tools/execute_notebooks.py --model AuraSR --allow-large-downloads
```

To build the local notebook environment for interactive use:

```bash
cd AuraSR
uv sync
```

Then select `AuraSR/.venv/bin/python` as the notebook kernel.
