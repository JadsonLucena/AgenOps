#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

try:
    import jsonschema
except Exception as exc:  # pragma: no cover
    print(f"jsonschema is required: {exc}")
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parent

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    schema_path = ROOT / "governance.meta.schema.json"
    example_path = ROOT / "governance.meta.example.json"

    schema = load_json(schema_path)
    example = load_json(example_path)

    jsonschema.validate(instance=example, schema=schema)

    required_paths = [
        "governance.meta.schema.json",
        "governance.meta.example.json",
        "README.md",
        "MERGE_NOTES.md",
        "integration-map.md",
        "rules.md",
        "validator.py",
        "governance/decision/decision-template.md",
        "governance/economics/execution-budget.schema.json",
        "governance/gitops/gitflow.md",
        "governance/topology/ownership-map.yaml",
        "runtime/telemetry/events.schema.json",
        "learning/pattern-evolution.md",
        "security/threat-model.md",
        "kit/core/README.md",
        "kit/agents/shared/dispatch-protocol.md",
        "kit/state/shared_task_state.schema.yaml",
        "kit/validation/validate_kit.py",
        "kit/experience/state-router.py",
        "scripts/experience/state-router.py",
        "docs/README.md",
        "planning_artifacts/README.md",
    ]
    for rel in required_paths:
        if not (ROOT / rel).exists():
            raise SystemExit(f"missing file: {rel}")

    if (ROOT / "integrations").exists() or (ROOT / "examples").exists():
        raise SystemExit("excluded scopes must not be present in v2")

    if (ROOT / "config").exists():
        raise SystemExit("config profiles/examples were intentionally excluded from v2")

    inv_ids = {item["id"] for item in example["invariants"]}
    if len(inv_ids) != len(example["invariants"]):
        raise SystemExit("duplicate invariant ids detected")

    rels = example["relationships"]
    if not any(r["from"] == "core" and r["to"] == "state" and r["mode"] == "writes" and r["allowed"] is False for r in rels):
        raise SystemExit("missing disallowed core->state write relationship")

    if not any(r["from"] == "governance" and r["to"] == "kit" and r["mode"] == "governs" and r["allowed"] is True for r in rels):
        raise SystemExit("missing governance->kit governance relationship")

    promotion = example["artifact_lifecycle"]["promotion_rule"]
    if "planning_artifacts/" not in promotion or "docs/" not in promotion:
        raise SystemExit("promotion rule must mention planning_artifacts/ and docs/")

    print("governance system v2 validation: pass")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
