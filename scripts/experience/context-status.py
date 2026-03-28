#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Inspect harness context status.")
    p.add_argument("--state-file", required=True)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    state = load_json(Path(args.state_file).expanduser().resolve())
    budget = int(state.get("context_budget_tokens") or 0)
    estimated = int(state.get("estimated_context_tokens") or 0)
    ratio = float(state.get("context_budget_ratio") or ((estimated / budget) if budget else 0.0))
    status = state.get("context_status") or ("exceeded" if ratio >= 1 else "compact_now" if ratio >= 0.85 else "warning" if ratio >= 0.70 else "healthy")
    print(json.dumps({
        "context_budget_tokens": budget,
        "estimated_context_tokens": estimated,
        "context_budget_ratio": round(ratio, 4),
        "context_status": status,
        "context_snapshot_version": state.get("context_snapshot_version"),
        "context_snapshot_path": state.get("context_snapshot_path"),
        "context_summary_path": state.get("context_summary_path"),
        "last_compacted_at": state.get("last_compacted_at"),
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
