#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any

DEFAULT_KEEP = 10


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def save_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def compact_list(value: Any, keep: int) -> Any:
    if not isinstance(value, list):
        return value
    if len(value) <= keep:
        return value
    return value[-keep:]


def compact_state(state: dict[str, Any], keep: int, snapshot_path: Path | None) -> dict[str, Any]:
    snapshot = {
        "session_id": state.get("session_id"),
        "phase": state.get("phase"),
        "change_type": state.get("change_type"),
        "last_completed_step": state.get("last_completed_step"),
        "next_action": state.get("next_action"),
        "brainstorm_status": state.get("brainstorm_status"),
        "requirements_status": state.get("requirements_status"),
        "spec_status": state.get("spec_status"),
        "architecture_status": state.get("architecture_status"),
        "design_status": state.get("design_status"),
        "current_spec_section_index": state.get("current_spec_section_index"),
        "current_chunk_index": state.get("current_chunk_index"),
        "current_subagent": state.get("current_subagent"),
        "context_status": state.get("context_status"),
        "context_budget_ratio": state.get("context_budget_ratio"),
        "context_snapshot_version": int(state.get("context_snapshot_version") or 0) + 1,
        "open_questions": compact_list(state.get("open_questions") or [], keep),
        "blockers": compact_list(state.get("blockers") or [], keep),
        "pending_reviews": compact_list(state.get("pending_reviews") or [], keep),
        "design_chunks": compact_list(state.get("design_chunks") or [], keep),
        "documentation_triggers": compact_list(state.get("documentation_triggers") or [], keep),
        "updated_at": now_iso(),
        "compacted_at": now_iso(),
    }
    if snapshot_path is not None:
        snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        snapshot_path.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        state["context_snapshot_path"] = str(snapshot_path)
        state["context_summary_path"] = str(snapshot_path.with_suffix('.md'))
    state["context_snapshot_version"] = snapshot["context_snapshot_version"]
    state["last_compacted_at"] = now_iso()
    state["context_status"] = "healthy"
    state["estimated_context_tokens"] = min(int(state.get("estimated_context_tokens") or 0), int(state.get("context_budget_tokens") or 0))
    state["context_budget_ratio"] = round((state.get("estimated_context_tokens") or 0) / (state.get("context_budget_tokens") or 1), 4)
    for key in ("open_questions", "blockers", "pending_reviews", "design_chunks", "documentation_triggers"):
        state[key] = compact_list(state.get(key) or [], keep)
    return snapshot, state


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Compact the harness state into a smaller snapshot.")
    p.add_argument("--state-file", required=True)
    p.add_argument("--snapshot-file", default=None)
    p.add_argument("--keep", type=int, default=DEFAULT_KEEP)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    state_path = Path(args.state_file).expanduser().resolve()
    state = load_json(state_path)
    snapshot_path = Path(args.snapshot_file).expanduser().resolve() if args.snapshot_file else None
    snapshot, state = compact_state(state, args.keep, snapshot_path)
    save_json(state_path, state)
    print(json.dumps({"status": "compacted", "snapshot_version": snapshot["context_snapshot_version"], "state_file": str(state_path), "snapshot_file": str(snapshot_path) if snapshot_path else None}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
