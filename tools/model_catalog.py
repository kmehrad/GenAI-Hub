#!/usr/bin/env python3
"""Catalog data and helpers for GenAI-Hub model notebooks."""

from __future__ import annotations

import ast
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CATEGORIES = {
    "llm",
    "vlm",
    "retrieval-embedding",
    "detection",
    "segmentation-matting",
    "depth-3d",
    "generation",
    "classification-representation",
    "anomaly",
}

ENVIRONMENTS = {
    "hf-transformers": {
        "path": "envs/hf-transformers",
        "python": ">=3.10,<3.13",
        "description": "Common Hugging Face Transformers vision, text, and multimodal notebooks.",
    },
    "diffusers": {
        "path": "envs/diffusers",
        "python": ">=3.10,<3.13",
        "description": "Diffusers-based text/image/video generation notebooks.",
    },
    "timm": {
        "path": "envs/timm",
        "python": ">=3.10,<3.13",
        "description": "timm and lightweight representation model notebooks.",
    },
    "retrieval": {
        "path": "envs/retrieval",
        "python": ">=3.10,<3.13",
        "description": "Embedding, CLIP/SigLIP, and retrieval notebooks.",
    },
    "haystack": {
        "path": "envs/haystack",
        "python": ">=3.10,<3.13",
        "description": "Haystack question-answering notebook.",
    },
    "sam3": {
        "path": "envs/sam3",
        "python": ">=3.12,<3.13",
        "description": "SAM-3 notebook with Python 3.12 and a CUDA-oriented Torch stack.",
    },
    "model-specific": {
        "path": None,
        "python": "see setup_notes",
        "description": "Notebook requires a project clone, pinned CUDA stack, Docker image, or other custom setup.",
    },
}

CATEGORY_BY_MODEL = {
    "AEMatter": "segmentation-matting",
    "Alfie": "generation",
    "AnimateDiff": "generation",
    "AnomalyCLIP": "anomaly",
    "AuraSR": "generation",
    "BART": "llm",
    "BEN2": "segmentation-matting",
    "BERT-deepset": "llm",
    "BLIP": "vlm",
    "BiRefNet": "segmentation-matting",
    "CAT-Seg": "segmentation-matting",
    "CLIP": "retrieval-embedding",
    "CLIPseg": "segmentation-matting",
    "CogVLM": "vlm",
    "ControlNet": "generation",
    "DETR": "detection",
    "DINOv3": "classification-representation",
    "DPT": "depth-3d",
    "DepthAnything": "depth-3d",
    "DepthPro": "depth-3d",
    "DiffDIS": "segmentation-matting",
    "EVA": "classification-representation",
    "EoMT": "classification-representation",
    "EssentialAI": "llm",
    "FLAVA": "retrieval-embedding",
    "FLUX": "generation",
    "FaceParsing": "segmentation-matting",
    "Ferret": "vlm",
    "FineGrain": "segmentation-matting",
    "GCL": "retrieval-embedding",
    "GLIDE": "generation",
    "GLIP": "detection",
    "Gemma3": "llm",
    "GroundingDINO": "detection",
    "ImageGPT": "generation",
    "InternVL": "vlm",
    "Janus": "vlm",
    "LISA": "segmentation-matting",
    "LLaMA2": "llm",
    "LLaVA": "vlm",
    "LLaVA-NeXT": "vlm",
    "LLaVA-OneVision": "vlm",
    "LeViT": "classification-representation",
    "Leffa": "generation",
    "Mask2Former": "segmentation-matting",
    "OV-DINO": "detection",
    "OVSeg": "segmentation-matting",
    "OWL-ViT": "detection",
    "OWL-v2": "detection",
    "OneFormer": "segmentation-matting",
    "PoolFormer": "classification-representation",
    "PromptDepthAnything": "depth-3d",
    "QLIP": "retrieval-embedding",
    "SA2VA": "vlm",
    "SAM": "segmentation-matting",
    "SAM-2": "segmentation-matting",
    "SAM-3": "segmentation-matting",
    "SAM-HQ": "segmentation-matting",
    "SAMRefiner": "segmentation-matting",
    "SAN": "segmentation-matting",
    "SD2": "generation",
    "SegFormer": "segmentation-matting",
    "SegZero": "segmentation-matting",
    "SigLIP": "retrieval-embedding",
    "SmolVLM": "vlm",
    "UNO": "generation",
    "UperNet": "segmentation-matting",
    "VGGT": "depth-3d",
    "VisionReasoner": "vlm",
    "WebSSL": "retrieval-embedding",
    "YOLO-World": "detection",
    "YOLOS4Fashion": "detection",
    "xLAM": "llm",
}

TASKS_BY_MODEL = {
    "AEMatter": ["matting", "segmentation"],
    "Alfie": ["image-generation", "rgba-generation"],
    "AnimateDiff": ["video-generation", "diffusion"],
    "AnomalyCLIP": ["anomaly-detection", "zero-shot"],
    "AuraSR": ["super-resolution", "image-generation"],
    "BART": ["text-generation", "seq2seq"],
    "BEN2": ["segmentation", "HR-seg", "DIS"],
    "BERT-deepset": ["question-answering"],
    "BLIP": ["VLM", "captioning", "VQA", "image-text-retrieval"],
    "BiRefNet": ["matting", "segmentation", "DIS"],
    "CAT-Seg": ["segmentation", "open-vocabulary-segmentation"],
    "CLIP": ["contrastive", "image-features", "text-features", "retrieval"],
    "CLIPseg": ["segmentation", "text-prompted-segmentation"],
    "CogVLM": ["VLM", "VQA"],
    "ControlNet": ["image-generation", "conditioned-generation", "diffusion"],
    "DETR": ["detection"],
    "DINOv3": ["image-features", "representation-learning"],
    "DPT": ["depth-estimation"],
    "DepthAnything": ["depth-estimation"],
    "DepthPro": ["depth-estimation", "metric-depth"],
    "DiffDIS": ["segmentation", "HR-seg", "DIS"],
    "EVA": ["image-classification", "image-features"],
    "EoMT": ["segmentation", "image-features"],
    "EssentialAI": ["text-generation"],
    "FLAVA": ["multimodal", "retrieval", "image-text"],
    "FLUX": ["image-generation", "diffusion"],
    "FaceParsing": ["segmentation", "face-parsing"],
    "Ferret": ["VLM", "grounded-chat"],
    "FineGrain": ["segmentation", "box-prompted-segmentation"],
    "GCL": ["retrieval", "ranking", "contrastive"],
    "GLIDE": ["image-generation", "diffusion"],
    "GLIP": ["detection", "grounding"],
    "Gemma3": ["text-generation", "VLM"],
    "GroundingDINO": ["detection", "grounding", "open-vocabulary-detection"],
    "ImageGPT": ["image-generation", "pixel-modeling"],
    "InternVL": ["VLM", "VQA"],
    "Janus": ["VLM", "multimodal-generation"],
    "LISA": ["segmentation", "reasoning-segmentation", "VLM"],
    "LLaMA2": ["text-generation", "chat"],
    "LLaVA": ["VLM", "VQA"],
    "LLaVA-NeXT": ["VLM", "VQA"],
    "LLaVA-OneVision": ["VLM", "VQA"],
    "LeViT": ["image-classification"],
    "Leffa": ["person-image-generation", "virtual-try-on"],
    "Mask2Former": ["segmentation", "panoptic-segmentation"],
    "OV-DINO": ["detection", "open-vocabulary-detection"],
    "OVSeg": ["segmentation", "open-vocabulary-segmentation"],
    "OWL-ViT": ["detection", "open-vocabulary-detection"],
    "OWL-v2": ["detection", "open-vocabulary-detection"],
    "OneFormer": ["segmentation", "semantic-segmentation", "instance-segmentation", "panoptic-segmentation"],
    "PoolFormer": ["image-classification", "image-features"],
    "PromptDepthAnything": ["depth-estimation", "prompted-depth"],
    "QLIP": ["image-features", "text-aligned-tokenization"],
    "SA2VA": ["VLM", "segmentation", "grounded-understanding"],
    "SAM": ["segmentation", "prompted-segmentation"],
    "SAM-2": ["segmentation", "prompted-segmentation"],
    "SAM-3": ["segmentation", "concept-prompted-segmentation"],
    "SAM-HQ": ["segmentation", "high-quality-segmentation"],
    "SAMRefiner": ["segmentation", "seg-refinement"],
    "SAN": ["segmentation", "open-vocabulary-segmentation"],
    "SD2": ["image-generation", "diffusion"],
    "SegFormer": ["segmentation", "clothes-segmentation"],
    "SegZero": ["segmentation", "reasoning-segmentation"],
    "SigLIP": ["contrastive", "image-features", "text-features", "retrieval"],
    "SmolVLM": ["VLM", "VQA"],
    "UNO": ["image-generation", "in-context-generation"],
    "UperNet": ["segmentation", "scene-understanding"],
    "VGGT": ["3D", "visual-geometry", "depth-estimation"],
    "VisionReasoner": ["VLM", "visual-reasoning"],
    "WebSSL": ["image-features", "similarity"],
    "YOLO-World": ["detection", "open-vocabulary-detection"],
    "YOLOS4Fashion": ["detection", "fashion-detection"],
    "xLAM": ["text-generation", "agent-actions"],
}

MODEL_SPECIFIC = {
    "AEMatter",
    "Alfie",
    "AnomalyCLIP",
    "CAT-Seg",
    "CogVLM",
    "ControlNet",
    "DINOv3",
    "DepthPro",
    "DiffDIS",
    "EoMT",
    "Ferret",
    "FineGrain",
    "GLIDE",
    "GLIP",
    "InternVL",
    "LISA",
    "LLaMA2",
    "Leffa",
    "OV-DINO",
    "OVSeg",
    "QLIP",
    "SAM-2",
    "SAM-HQ",
    "SAMRefiner",
    "SAN",
    "SegZero",
    "UNO",
    "VGGT",
    "VisionReasoner",
    "YOLO-World",
}

ENV_BY_MODEL = {
    "BERT-deepset": "haystack",
    "SAM-3": "sam3",
}

SETUP_NOTES = {
    "SAM-3": "Requires Python 3.12, a CUDA-oriented Torch stack, facebookresearch/sam3 editable install, and either local SAM-3 assets or latest Transformers support.",
    "GLIP": "Notebook documents a Docker image with CUDA 10.2 and PyTorch 1.9; treat as Docker/model-specific unless ported.",
    "YOLO-World": "Requires MMDetection/MMEngine stack and model checkpoint.",
    "OV-DINO": "Requires Detectron2/detrex stack and CUDA-specific Torch pins.",
    "CAT-Seg": "Requires Detectron2 and project-specific open-vocabulary segmentation dependencies.",
    "OVSeg": "Requires Detectron2 and the facebookresearch/ov-seg project setup.",
    "LLaMA2": "Requires external Llama model access/download approval.",
    "Ferret": "Uses a nested project with pinned dependencies and a git Transformers source.",
}

COMMON_DEPENDENCIES = {
    "hf-transformers": ["torch", "torchvision", "transformers", "accelerate", "pillow", "matplotlib", "numpy", "requests"],
    "diffusers": ["torch", "torchvision", "diffusers", "transformers", "accelerate", "safetensors", "pillow", "matplotlib", "numpy"],
    "timm": ["torch", "torchvision", "timm", "pillow", "matplotlib", "numpy", "requests"],
    "retrieval": ["torch", "torchvision", "transformers", "sentencepiece", "protobuf", "pillow", "matplotlib", "numpy", "requests"],
    "haystack": ["haystack-ai", "transformers[torch,sentencepiece]"],
    "sam3": ["torch==2.7.0", "torchvision", "torchaudio", "transformers", "einops", "decord", "pycocotools", "pillow", "matplotlib", "requests"],
}


@dataclass(frozen=True)
class NotebookInfo:
    model: str
    notebook: Path
    imports: tuple[str, ...]


def notebooks(root: Path = ROOT) -> list[NotebookInfo]:
    found: list[NotebookInfo] = []
    paths = tracked_notebook_paths(root)
    for path in paths:
        if path.parts[0].startswith("."):
            continue
        found.append(NotebookInfo(model=path.parent.name, notebook=path, imports=tuple(extract_imports(path))))
    return found


def tracked_notebook_paths(root: Path = ROOT) -> list[Path]:
    try:
        proc = subprocess.run(
            ["git", "ls-files", "*/*.ipynb"],
            cwd=root,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return sorted(root.glob("*/*.ipynb"))
    paths = [root / line for line in proc.stdout.splitlines() if line.strip()]
    return sorted(paths) if paths else sorted(root.glob("*/*.ipynb"))


def notebooks_by_model(root: Path = ROOT) -> dict[str, list[NotebookInfo]]:
    grouped: dict[str, list[NotebookInfo]] = {}
    for info in notebooks(root):
        grouped.setdefault(info.model, []).append(info)
    return grouped


def extract_imports(notebook_path: Path) -> list[str]:
    try:
        data = json.loads(notebook_path.read_text(encoding="utf-8"))
    except Exception:
        return []
    imports: set[str] = set()
    for cell in data.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        try:
            tree = ast.parse("".join(cell.get("source", [])))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".")[0])
    return sorted(imports)


def environment_for_model(model: str) -> str:
    if model in ENV_BY_MODEL:
        return ENV_BY_MODEL[model]
    if model in MODEL_SPECIFIC:
        return "model-specific"
    category = CATEGORY_BY_MODEL.get(model)
    if category == "generation":
        return "diffusers"
    if category == "classification-representation":
        return "timm"
    if category == "retrieval-embedding":
        return "retrieval"
    return "hf-transformers"


def metadata_for(model: str, notebook: Path, imports: tuple[str, ...] = ()) -> dict:
    env = environment_for_model(model)
    env_info = ENVIRONMENTS[env]
    dependencies = COMMON_DEPENDENCIES.get(env, [])
    return {
        "model": model,
        "category": CATEGORY_BY_MODEL.get(model, "classification-representation"),
        "tasks": TASKS_BY_MODEL.get(model, []),
        "notebook": str(notebook.relative_to(ROOT)),
        "notebooks": [str(notebook.relative_to(ROOT))],
        "environment": env,
        "environment_path": env_info["path"],
        "python": env_info["python"],
        "dependencies": dependencies,
        "imports": list(imports),
        "setup_notes": SETUP_NOTES.get(model, ""),
        "test_status": "not-run",
    }


def load_metadata(root: Path = ROOT) -> list[dict]:
    entries: list[dict] = []
    for path in sorted(root.glob("*/metadata.json")):
        try:
            entries.append(json.loads(path.read_text(encoding="utf-8")))
        except json.JSONDecodeError as exc:
            entries.append({"model": path.parent.name, "metadata_error": str(exc)})
    return entries


def execution_entries(root: Path = ROOT) -> list[dict]:
    rows: list[dict] = []
    for data in load_metadata(root):
        for notebook in data.get("notebooks") or [data.get("notebook")]:
            if not notebook:
                continue
            row = dict(data)
            row["notebook"] = notebook
            rows.append(row)
    return rows
