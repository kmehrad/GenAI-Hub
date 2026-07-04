#!/usr/bin/env python3
"""Execute notebooks with uv environments while controlling disk usage."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

from model_catalog import ROOT, execution_entries


REPORT = ROOT / "reports" / "notebook_uv_execution.json"


def run(cmd: list[str], cwd: Path, timeout: int | None = None) -> tuple[int, str]:
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        timeout=timeout,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def free_gb(path: Path) -> float:
    usage = shutil.disk_usage(path)
    return usage.free / (1024**3)


def cache_paths() -> list[Path]:
    paths: list[Path] = []
    for name in ["UV_CACHE_DIR", "HF_HOME", "TORCH_HOME", "XDG_CACHE_HOME"]:
        value = os.environ.get(name)
        if value:
            paths.append(Path(value).expanduser())
    unique: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        probe = path if path.exists() else path.parent
        try:
            resolved = probe.resolve()
        except OSError:
            resolved = probe
        if resolved not in seen:
            seen.add(resolved)
            unique.append(probe)
    return unique


def low_cache_space(min_cache_free_gb: float) -> str | None:
    for path in cache_paths():
        path.mkdir(parents=True, exist_ok=True)
        available = free_gb(path)
        if available < min_cache_free_gb:
            return f"cache filesystem for {path} has {available:.1f} GB free, below threshold {min_cache_free_gb:.1f} GB"
    return None


def clean_venv(env_dir: Path) -> None:
    venv = env_dir / ".venv"
    if venv.exists():
        shutil.rmtree(venv)


def sanitize_text(value: str) -> str:
    home = Path.home()
    replacements = {
        str(ROOT): "<repo>",
        str(home): "<home>",
    }
    sanitized = value
    for source, target in replacements.items():
        sanitized = sanitized.replace(source, target)
    return sanitized


def load_report() -> list[dict]:
    if REPORT.exists():
        return json.loads(REPORT.read_text(encoding="utf-8"))
    return []


def save_report(rows: list[dict]) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")


def should_block_before_download(entry: dict, allow_large_downloads: bool) -> str | None:
    notes = (entry.get("setup_notes") or "").lower()
    if allow_large_downloads:
        return None
    if any(token in notes for token in ["gated", "checkpoint", "model access", "download approval"]):
        return "requires gated access, checkpoint, or explicit download approval"
    if entry["environment"] == "model-specific":
        return "model-specific environment requires manual setup verification before full download/execution"
    return None


def execute_entry(entry: dict, min_free_gb: float, min_cache_free_gb: float, timeout: int, allow_large_downloads: bool) -> dict:
    started = datetime.now(timezone.utc).isoformat()
    env_path = entry.get("environment_path")
    env_dir = ROOT / env_path if env_path else ROOT / entry["model"]
    notebook = ROOT / entry["notebook"]
    before = free_gb(ROOT)

    row = {
        "model": entry["model"],
        "notebook": entry["notebook"],
        "environment": entry["environment"],
        "environment_path": env_path,
        "started_at": started,
        "free_gb_before": round(before, 2),
        "status": "not-run",
        "reason": "",
        "duration_seconds": 0,
    }

    if before < min_free_gb:
        row.update(status="blocked", reason=f"free disk {before:.1f} GB is below threshold {min_free_gb:.1f} GB")
        return row

    cache_reason = low_cache_space(min_cache_free_gb)
    if cache_reason:
        row.update(status="blocked", reason=cache_reason)
        return row

    block_reason = should_block_before_download(entry, allow_large_downloads)
    if block_reason:
        row.update(status="blocked", reason=block_reason)
        return row

    if not (env_dir / "pyproject.toml").exists():
        row.update(status="blocked", reason=f"missing uv project at {env_dir.relative_to(ROOT)}")
        return row

    start = time.monotonic()
    try:
        sync_code, sync_out = run(["uv", "sync"], env_dir, timeout=timeout)
        if sync_code != 0:
            row.update(status="failed", reason="uv sync failed", output=sanitize_text(sync_out[-4000:]))
            return row

        output_dir = ROOT / "reports" / "executed"
        output_dir.mkdir(parents=True, exist_ok=True)
        out_name = f"{entry['model']}-{Path(entry['notebook']).stem}.executed.ipynb"
        cmd = [
            "uv",
            "run",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            str(notebook),
            "--output",
            out_name,
            "--output-dir",
            str(output_dir),
            f"--ExecutePreprocessor.cwd={notebook.parent}",
            f"--ExecutePreprocessor.timeout={timeout}",
        ]
        code, out = run(cmd, env_dir, timeout=timeout + 120)
        if code == 0:
            row.update(status="passed", reason="")
        else:
            row.update(status="failed", reason="notebook execution failed", output=sanitize_text(out[-4000:]))
    except subprocess.TimeoutExpired as exc:
        row.update(status="failed", reason=f"timeout after {exc.timeout} seconds")
    finally:
        row["duration_seconds"] = round(time.monotonic() - start, 1)
        clean_venv(env_dir)
        row["free_gb_after_cleanup"] = round(free_gb(ROOT), 2)
    return row


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", action="append", help="Model folder name to execute. May be repeated.")
    parser.add_argument("--environment", action="append", help="Environment name to execute. May be repeated.")
    parser.add_argument("--all", action="store_true", help="Execute all metadata entries.")
    parser.add_argument("--min-free-gb", type=float, default=35.0)
    parser.add_argument("--min-cache-free-gb", type=float, default=35.0)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--allow-large-downloads", action="store_true")
    args = parser.parse_args()

    entries = execution_entries()
    selected = []
    for entry in entries:
        if args.all:
            selected.append(entry)
        elif args.model and entry["model"] in args.model:
            selected.append(entry)
        elif args.environment and entry["environment"] in args.environment:
            selected.append(entry)

    if not selected:
        parser.error("select at least one notebook with --all, --model, or --environment")

    report = load_report()
    for entry in selected:
        row = execute_entry(entry, args.min_free_gb, args.min_cache_free_gb, args.timeout, args.allow_large_downloads)
        report.append(row)
        save_report(report)
        print(f"{entry['model']}: {row['status']} {row.get('reason', '')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
