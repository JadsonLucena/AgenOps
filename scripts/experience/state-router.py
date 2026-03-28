#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
from typing import Any

DEFAULT_SESSION_PREFIX = "egk-"
DONE_VALUES = {"done", "complete", "approved", "ready", "pass", "passed", "green"}
WARN_THRESHOLD = 0.70
COMPACT_THRESHOLD = 0.85

FIELDS = [
    "session_id",
    "phase",
    "change_type",
    "last_completed_step",
    "next_action",
    "brainstorm_status",
    "requirements_status",
    "spec_status",
    "architecture_status",
    "design_status",
    "current_spec_section_index",
    "spec_sections",
    "spec_file_plan",
    "current_chunk_index",
    "design_chunks",
    "documentation_triggers",
    "test_status",
    "validation_status",
    "security_status",
    "blockers",
    "open_questions",
    "pending_reviews",
    "current_subagent",
    "subagent_queue",
    "current_contract_path",
    "upstream_contract",
    "downstream_contract",
    "handoff_envelope_path",
    "handoff_status",
    "last_handoff_at",
    "context_budget_tokens",
    "estimated_context_tokens",
    "context_budget_ratio",
    "context_status",
    "context_snapshot_version",
    "context_snapshot_path",
    "context_summary_path",
    "context_load_order",
    "last_compacted_at",
    "updated_at",
]

def default_state_file() -> Path:
    env = os.environ.get("KIT_STATE_FILE")
    if env:
        return Path(env).expanduser().resolve()
    xdg = os.environ.get("XDG_STATE_HOME")
    if xdg:
        return Path(xdg).expanduser().resolve() / "engineering-governance-kit" / "state.json"
    return Path.home() / ".local" / "state" / "engineering-governance-kit" / "state.json"

def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))

def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")

def default_state() -> dict[str, Any]:
    return {
        "session_id": DEFAULT_SESSION_PREFIX + now_iso().replace(":", "").replace("-", "").replace("Z", ""),
        "phase": "intake",
        "change_type": "unknown",
        "last_completed_step": None,
        "next_action": "resolve requirements gaps with the Requirements Engineer sub-agent.",
        "brainstorm_status": "unknown",
        "requirements_status": "unknown",
        "spec_status": "unknown",
        "architecture_status": "unknown",
        "design_status": "unknown",
        "current_spec_section_index": 0,
        "spec_sections": [],
        "spec_file_plan": {},
        "current_chunk_index": 0,
        "design_chunks": [],
        "documentation_triggers": [],
        "test_status": "unknown",
        "validation_status": "unknown",
        "security_status": "unknown",
        "blockers": [],
        "open_questions": [],
        "pending_reviews": [],
        "current_subagent": None,
        "subagent_queue": [],
        "current_contract_path": None,
        "upstream_contract": None,
        "downstream_contract": None,
        "handoff_envelope_path": None,
        "handoff_status": "idle",
        "last_handoff_at": None,
        "context_budget_tokens": 12000,
        "estimated_context_tokens": 0,
        "context_budget_ratio": 0.0,
        "context_status": "healthy",
        "context_snapshot_version": 0,
        "context_snapshot_path": None,
        "context_summary_path": None,
        "context_load_order": ["shared_state", "approved_artifacts", "latest_summary", "handoff", "evidence"],
        "last_compacted_at": None,
        "updated_at": now_iso(),
    }

def ensure_shape(state: dict[str, Any]) -> dict[str, Any]:
    base = default_state()
    base.update(state)
    for key in ("spec_sections", "design_chunks", "documentation_triggers", "blockers", "open_questions", "pending_reviews", "subagent_queue", "context_load_order"):
        if base.get(key) is None:
            base[key] = []
    if base.get("current_chunk_index") is None:
        base["current_chunk_index"] = 0
    if base.get("current_spec_section_index") is None:
        base["current_spec_section_index"] = 0
    budget = base.get("context_budget_tokens") or 0
    estimated = base.get("estimated_context_tokens") or 0
    base["context_budget_ratio"] = round((estimated / budget), 4) if budget else 0.0
    ratio = base["context_budget_ratio"]
    if ratio >= 1.0:
        base["context_status"] = "exceeded"
    elif ratio >= COMPACT_THRESHOLD:
        base["context_status"] = "compact_now"
    elif ratio >= WARN_THRESHOLD:
        base["context_status"] = "warning"
    else:
        base["context_status"] = base.get("context_status") or "healthy"
    return base

def init_state(path: Path, force: bool = False) -> dict[str, Any]:
    if path.exists() and not force:
        return load_state(path)
    state = default_state()
    save_state(path, state)
    return state

def apply_updates(state: dict[str, Any], updates: list[str]) -> dict[str, Any]:
    for update in updates:
        if "=" not in update:
            continue
        key, value = update.split("=", 1)
        key = key.strip()
        raw = value.strip()
        if raw.lower() in {"true", "false"}:
            parsed: Any = raw.lower() == "true"
        else:
            try:
                parsed = json.loads(raw)
            except Exception:
                parsed = raw
        state[key] = parsed
    state["updated_at"] = now_iso()
    return ensure_shape(state)

def update_state(path: Path, updates: list[str]) -> dict[str, Any]:
    state = ensure_shape(load_state(path) if path.exists() else default_state())
    state = apply_updates(state, updates)
    save_state(path, state)
    return state

def route_next_step(state: dict[str, Any]) -> str:
    state = ensure_shape(state)
    blockers = state.get("blockers") or []
    if blockers:
        return "resolve blockers before any further work."
    if state.get("context_status") in {"exceeded", "compact_now"}:
        return "compact and snapshot the active context before the next non-trivial step."
    if state.get("brainstorm_status") not in DONE_VALUES:
        return "dispatch the Requirements Engineer sub-agent for brainstorm and deep elicitation."
    if state.get("spec_status") not in DONE_VALUES:
        return "complete the spec document design and handoff setup."
    if state.get("architecture_status") not in DONE_VALUES:
        return "dispatch the Software Architect sub-agent for the next safe design slice."
    if state.get("design_status") not in DONE_VALUES:
        return "split the scope into a baby-step design chunk."
    if state.get("test_status") not in DONE_VALUES:
        return "dispatch the Quality Engineer sub-agent for failing tests and quality gates."
    if state.get("validation_status") not in DONE_VALUES:
        return "run validation and compact the context if the budget is tight."
    if state.get("security_status") not in DONE_VALUES:
        return "dispatch the Security Reviewer sub-agent."
    return "close the change with a concise summary and persist the final snapshot."

def render_menu(state: dict[str, Any]) -> str:
    state = ensure_shape(state)
    lines = [
        "Available commands:",
        "- init: create or reset the state file",
        "- show: print the current state",
        "- next: compute the next action",
        "- menu: show this menu",
        "- route: alias for next",
        "- update: apply key=value updates",
        "",
        f"Current phase: {state.get('phase')}",
        f"Context status: {state.get('context_status')} ({state.get('context_budget_ratio'):.2%})",
        f"Current sub-agent: {state.get('current_subagent')}",
    ]
    return "\n".join(lines)

def show_state(state: dict[str, Any]) -> str:
    state = ensure_shape(state)
    keys = [k for k in FIELDS if k in state or k in {"context_budget_tokens","estimated_context_tokens","context_budget_ratio","context_status","context_snapshot_version","context_snapshot_path","context_summary_path","context_load_order","last_compacted_at"}]
    return json.dumps({k: state.get(k) for k in keys}, indent=2, sort_keys=True)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="State router for the engineering governance kit.")
    parser.add_argument("command", nargs="?", default="next", choices={"init", "show", "next", "menu", "route", "update"})
    parser.add_argument("--file", dest="file", default=str(default_state_file()))
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--update", dest="updates", action="append", default=[])
    return parser.parse_args()

def main() -> int:
    args = parse_args()
    state_path = Path(args.file).expanduser().resolve()

    if args.command == "init":
        state = init_state(state_path, force=args.force)
        print(show_state(state))
        return 0

    if args.command == "update":
        state = update_state(state_path, args.updates)
        print(show_state(state))
        return 0

    state = ensure_shape(load_state(state_path) if state_path.exists() else default_state())
    if args.command == "show":
        print(show_state(state))
        return 0
    if args.command in {"next", "route"}:
        print(route_next_step(state))
        return 0
    if args.command == "menu":
        print(render_menu(state))
        return 0
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
