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

    # Cross-layer sanity checks beyond schema.
    required_paths = [
        "governance.meta.schema.json",
        "governance.meta.example.json",
        "integration-map.md",
        "rules.md",
        "README.md",
    ]
    for rel in required_paths:
        if not (ROOT / rel).exists():
            raise SystemExit(f"missing file: {rel}")

    # Invariant checks.
    inv_ids = {item["id"] for item in example["invariants"]}
    if len(inv_ids) != len(example["invariants"]):
        raise SystemExit("duplicate invariant ids detected")

    # Ensure only allowed write to state is explicitly marked disallowed from core.
    rels = example["relationships"]
    if not any(r["from"] == "core" and r["to"] == "state" and r["mode"] == "writes" and r["allowed"] is False for r in rels):
        raise SystemExit("missing disallowed core->state write relationship")

    # Ensure promotion rule links planning_artifacts and docs conceptually.
    promotion_rule = example["artifact_lifecycle"]["promotion_rule"]
    if "planning_artifacts/" not in promotion_rule or "docs/" not in promotion_rule:
        raise SystemExit("promotion rule must mention planning_artifacts/ and docs/")

    print("governance meta-model validation: pass")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
