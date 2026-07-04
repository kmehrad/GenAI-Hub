# BEN2

Run the notebook from the repository root with the standard executor:

```bash
uv run python tools/execute_notebooks.py --model BEN2 --allow-large-downloads
```

To build the local notebook environment for interactive use:

```bash
cd BEN2
uv sync
```

Then select `BEN2/.venv/bin/python` as the notebook kernel.
