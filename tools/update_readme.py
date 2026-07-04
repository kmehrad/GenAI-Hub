#!/usr/bin/env python3
"""Generate the README model index from metadata.json files."""

from __future__ import annotations

from collections import defaultdict
import json
from pathlib import Path

from model_catalog import ENVIRONMENTS, ROOT, execution_entries, load_metadata


MARKER_START = "<!-- AUTO-GENERATED:MODEL-INDEX:START -->"
MARKER_END = "<!-- AUTO-GENERATED:MODEL-INDEX:END -->"


def link(path: str, label: str | None = None) -> str:
    return f"[{label or path}]({path})"


def generate(entries: list[dict]) -> str:
    entries = sorted(entries, key=lambda item: item.get("model", "").lower())
    notebook_entries = sorted(execution_entries(), key=lambda item: (item.get("model", "").lower(), item.get("notebook", "")))
    by_category: dict[str, list[dict]] = defaultdict(list)
    by_task: dict[str, list[dict]] = defaultdict(list)
    by_env: dict[str, list[dict]] = defaultdict(list)
    for entry in notebook_entries:
        by_category[entry["category"]].append(entry)
        by_env[entry["environment"]].append(entry)
        for task in entry["tasks"]:
            by_task[task].append(entry)

    lines: list[str] = [MARKER_START, ""]
    lines.extend(
        [
            "### Quick Start",
            "",
            "Install uv, then use the root project for repository tooling:",
            "",
            "```bash",
            "uv sync",
            "uv run python tools/validate_metadata.py",
            "uv run python tools/update_readme.py",
            "```",
            "",
            "For notebook execution, use the environment shown in the matrix below. Shared environments live under `envs/`; models marked `model-specific` need the setup notes in their model folder metadata.",
            "",
            "Register a shared environment as a Jupyter kernel:",
            "",
            "```bash",
            "cd envs/hf-transformers",
            "uv sync",
            "uv run python -m ipykernel install --user --name genai-hf-transformers",
            "```",
            "",
            "### Index (by model)",
            "",
        ]
    )
    for entry in notebook_entries:
        tasks = ", ".join(entry["tasks"])
        label = entry["model"]
        model_count = len([row for row in notebook_entries if row["model"] == entry["model"]])
        if model_count > 1:
            label = f"{entry['model']} ({Path(entry['notebook']).name})"
        lines.append(f"* {link(entry['notebook'], label)} — {entry['category']}; {tasks}")

    lines.extend(["", "### Index (by category)", ""])
    for category in sorted(by_category):
        lines.append(f"**{category}**")
        for entry in sorted(by_category[category], key=lambda item: (item["model"].lower(), item["notebook"])):
            label = entry["model"]
            if len([row for row in notebook_entries if row["model"] == entry["model"]]) > 1:
                label = f"{entry['model']} ({Path(entry['notebook']).name})"
            lines.append(f"  * {link(entry['notebook'], label)}")
        lines.append("")

    lines.extend(["### Index (by task)", ""])
    for task in sorted(by_task, key=str.lower):
        parts = []
        for entry in sorted(by_task[task], key=lambda item: (item["model"].lower(), item["notebook"])):
            label = entry["model"]
            if len([row for row in notebook_entries if row["model"] == entry["model"]]) > 1:
                label = f"{entry['model']} ({Path(entry['notebook']).name})"
            parts.append(link(entry["notebook"], label))
        items = ", ".join(parts)
        lines.append(f"* **{task}**: {items}")

    lines.extend(["", "### Environment Matrix", ""])
    lines.append("| Model | Notebook | Environment | Python | Notes |")
    lines.append("| --- | --- | --- | --- | --- |")
    for entry in notebook_entries:
        env = entry["environment"]
        env_path = entry.get("environment_path") or "model folder setup"
        notes = entry.get("setup_notes") or ENVIRONMENTS[env]["description"]
        lines.append(
            f"| {entry['model']} | {link(entry['notebook'], Path(entry['notebook']).name)} | `{env}` ({env_path}) | `{entry['python']}` | {notes} |"
        )

    lines.extend(["", "### Testing Status", ""])
    lines.extend(testing_status_lines())
    lines.extend(
        [
            "",
            "Notebook execution results are written to `reports/notebook_uv_execution.json` by `tools/execute_notebooks.py`. Source notebook outputs are preserved unless they are explicitly inspected and proven safe to remove.",
            "",
            MARKER_END,
            "",
        ]
    )
    return "\n".join(lines)


def testing_status_lines() -> list[str]:
    report_path = ROOT / "reports" / "notebook_uv_execution.json"
    if not report_path.exists():
        return ["No notebook execution report has been generated yet."]
    rows = json.loads(report_path.read_text(encoding="utf-8"))
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row.get("status", "unknown")] += 1
    lines = [
        f"Latest report: {len(rows)} notebook entries; {counts['passed']} passed, {counts['failed']} failed, {counts['blocked']} blocked.",
        "",
        "| Status | Models |",
        "| --- | --- |",
    ]
    model_counts: dict[str, int] = defaultdict(int)
    for row in rows:
        model_counts[row["model"]] += 1
    for status in ["passed", "failed", "blocked"]:
        status_models = []
        for row in rows:
            if row.get("status") != status:
                continue
            label = row["model"]
            if model_counts[row["model"]] > 1:
                label = f"{row['model']} ({Path(row['notebook']).name})"
            status_models.append(label)
        lines.append(f"| {status} | {', '.join(status_models) if status_models else '-'} |")
    return lines


def splice(readme: str, block: str) -> str:
    if MARKER_START in readme and MARKER_END in readme:
        pre, rest = readme.split(MARKER_START, 1)
        _, post = rest.split(MARKER_END, 1)
        return f"{pre}{block}{post.lstrip()}"
    suffix = "\n\n## Models\n\n" + block
    return readme.rstrip() + suffix + "\n"


def main() -> int:
    readme_path = ROOT / "README.md"
    current = readme_path.read_text(encoding="utf-8") if readme_path.exists() else "# GenAI-Hub\n\n"
    updated = splice(current, generate(load_metadata()))
    if updated != current:
        readme_path.write_text(updated, encoding="utf-8")
        print("README updated")
    else:
        print("README already up-to-date")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
