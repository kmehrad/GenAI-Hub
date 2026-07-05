# ImageGPT

Run the notebook from the repository root with the standard executor:

```bash
uv run python tools/execute_notebooks.py --model ImageGPT --allow-large-downloads
```

To build the local notebook environment for interactive use:

```bash
cd ImageGPT
uv sync
```

Then select `ImageGPT/.venv/bin/python` as the notebook kernel.
