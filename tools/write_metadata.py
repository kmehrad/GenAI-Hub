#!/usr/bin/env python3
"""Generate per-model metadata.json files from the catalog."""

from __future__ import annotations

import json

from model_catalog import ROOT, metadata_for, notebooks_by_model


def main() -> int:
    count = 0
    for model, infos in notebooks_by_model().items():
        primary = infos[0]
        path = ROOT / model / "metadata.json"
        imports = sorted({item for info in infos for item in info.imports})
        metadata = metadata_for(model, primary.notebook, tuple(imports))
        metadata["notebooks"] = [str(info.notebook.relative_to(ROOT)) for info in infos]
        rendered = json.dumps(metadata, indent=2, sort_keys=False) + "\n"
        if not path.exists() or path.read_text(encoding="utf-8") != rendered:
            path.write_text(rendered, encoding="utf-8")
            count += 1
    print(f"metadata files written/updated: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
