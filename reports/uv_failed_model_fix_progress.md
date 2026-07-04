# uv Failed Model Fix Progress

Branch: `fix/uv-failed-model-envs`

Source failure list: `reports/notebook_uv_execution_followup.md` `Failed` section.

## Fixed and Tested

These failed notebook environments were fixed with model-local uv projects, full notebook execution, VS Code kernel verification, and model README run instructions.

| Model | Environment commit | README commit | Notes |
| --- | --- | --- | --- |
| `AuraSR` | `462e773 Fix AuraSR uv notebook environment` | `3ec6855 Add AuraSR notebook run instructions` | Uses local `AuraSR` diffusers env plus `aura-sr`. |
| `BEN2` | `a18b974 Fix BEN2 uv notebook environment` | included in `a18b974` | Uses Git dependency `ben2 @ git+https://github.com/PramaLLC/BEN2.git` plus `opencv-python`. |
| `BERT-deepset` | `89d12da Fix BERT-deepset uv notebook environment` | `dadbe33 Add BERT-deepset notebook run instructions` | Uses local Haystack env. |
| `CLIP` | `9fb9317 Fix CLIP uv notebook environment` | `2c2ea2b Add CLIP notebook run instructions` | Pins `transformers>=4.55.0,<5.0.0` because Transformers 5 changed CLIP output behavior. |
| `DETR` | `3c0ca1e Fix DETR uv notebook environment` | `89063d7 Add DETR notebook run instructions` | Adds `timm` and `supervision`; pins `transformers>=4.55.0,<5.0.0` for notebook-compatible DETR APIs. |

## Resume Point

Continue with the remaining entries from the original `Failed (26)` list, skipping the five fixed models above.

Next model to fix: `BiRefNet`.

Remaining failed models in original order:

1. `BiRefNet` - `BiRefNet/birefnet-hr-matting_huggingface_inference.ipynb`
2. `FLAVA` - `FLAVA/flava_huggingface_inference.ipynb`
3. `FLUX` - `FLUX/flux_huggingface_inference.ipynb`
4. `Gemma3` - `Gemma3/gemma3_huggingface_inference.ipynb`
5. `GroundingDINO` - `GroundingDINO/groundingdino_huggingface_inference.ipynb`
6. `ImageGPT` - `ImageGPT/imagegpt_huggingface_inference.ipynb`
7. `Janus` - `Janus/janus_huggingface_inference.ipynb`
8. `Mask2Former` - `Mask2Former/mask2former_huggingface_inference.ipynb`
9. `OWL-ViT` - `OWL-ViT/owlvit_huggingface_inference.ipynb`
10. `OWL-ViT` - `OWL-ViT/owlvit_inference-2.ipynb`
11. `OWL-v2` - `OWL-v2/owlv2_huggingface_inference.ipynb`
12. `OneFormer` - `OneFormer/oneformer_huggingface_inference.ipynb`
13. `PoolFormer` - `PoolFormer/poolformer_huggingface_inference.ipynb`
14. `SA2VA` - `SA2VA/sa2va_huggingface_inference.ipynb`
15. `SAM` - `SAM/sam_huggingface_inference.ipynb`
16. `SAM-3` - `SAM-3/sam3_inference.ipynb`
17. `SD2` - `SD2/sd_huggingface_inference.ipynb`
18. `SmolVLM` - `SmolVLM/smolvlm_huggingface_inference.ipynb`
19. `UperNet` - `UperNet/upernet_huggingface_inference.ipynb`
20. `WebSSL` - `WebSSL/webssl_huggingface_inference.ipynb`
21. `YOLOS4Fashion` - `YOLOS4Fashion/yolos4fashion_huggingface_inference.ipynb`

## Workflow to Continue

For each remaining model:

1. Add a model-local `pyproject.toml` with `[tool.uv] package = false`.
2. Update `metadata.json` to keep the existing `environment` label, point `environment_path` at the model folder, include actual runtime dependencies, and set `test_status` to `passed` only after execution passes.
3. Add or update the model `README.md` with:

```bash
uv run python tools/execute_notebooks.py --model <MODEL> --allow-large-downloads
```

4. Run `uv sync` in the model folder.
5. Verify the local VS Code kernel exists via `<MODEL>/.venv/bin/python -m jupyter kernelspec list`.
6. Run `uv run python tools/validate_metadata.py`.
7. Run `uv run python tools/execute_notebooks.py --model <MODEL> --allow-large-downloads`.
8. Rebuild `<MODEL>/.venv` after executor cleanup if the user will test in VS Code.
9. Commit environment/notebook changes and README instructions separately unless the user asks otherwise.
