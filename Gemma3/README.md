# Gemma3

Run the notebook from the repository root with the standard executor:

```bash
uv run python tools/execute_notebooks.py --model Gemma3 --allow-large-downloads
```

To build the local notebook environment for interactive use:

```bash
cd Gemma3
uv sync
```

Then select `Gemma3/.venv/bin/python` as the notebook kernel.

The notebook uses `google/gemma-3-4b-it`, which requires accepted Hugging Face license terms and credentials with access to the gated model.
