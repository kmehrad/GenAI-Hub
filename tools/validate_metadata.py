#!/usr/bin/env python3
"""Validate model metadata files and environment references."""

from __future__ import annotations

from pathlib import Path

from model_catalog import CATEGORIES, ENVIRONMENTS, ROOT, load_metadata, notebooks


def main() -> int:
    errors: list[str] = []
    notebook_by_model = {info.model: info.notebook for info in notebooks()}

    for model, notebook_path in notebook_by_model.items():
        metadata_path = ROOT / model / "metadata.json"
        if not metadata_path.exists():
            errors.append(f"{model}: missing metadata.json")

    for data in load_metadata():
        model = data.get("model") or "<unknown>"
        if "metadata_error" in data:
            errors.append(f"{model}: invalid JSON: {data['metadata_error']}")
            continue
        for key in ["model", "category", "tasks", "notebook", "notebooks", "environment", "python", "test_status"]:
            if key not in data:
                errors.append(f"{model}: missing required key {key}")
        category = data.get("category")
        if category not in CATEGORIES:
            errors.append(f"{model}: unknown category {category!r}")
        environment = data.get("environment")
        if environment not in ENVIRONMENTS:
            errors.append(f"{model}: unknown environment {environment!r}")
        notebook = data.get("notebook")
        if notebook and not (ROOT / notebook).exists():
            errors.append(f"{model}: notebook does not exist: {notebook}")
        notebooks_list = data.get("notebooks")
        if not isinstance(notebooks_list, list) or not notebooks_list:
            errors.append(f"{model}: notebooks must be a non-empty list")
        else:
            for item in notebooks_list:
                if not (ROOT / item).exists():
                    errors.append(f"{model}: notebook does not exist: {item}")
        if not isinstance(data.get("tasks"), list) or not data.get("tasks"):
            errors.append(f"{model}: tasks must be a non-empty list")
        env_path = data.get("environment_path")
        if env_path and not (ROOT / env_path / "pyproject.toml").exists():
            errors.append(f"{model}: environment_path missing pyproject.toml: {env_path}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"metadata valid for {len(load_metadata())} model folders")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
