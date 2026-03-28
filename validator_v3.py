#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Any, Iterable

@dataclass
class Finding:
    severity: str  # error | warning
    code: str
    message: str
    path: str | None = None

def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def exists(root: Path, rel: str) -> bool:
    return (root / rel).exists()

def add_missing(findings: list[Finding], root: Path, rel: str) -> None:
    if not exists(root, rel):
        findings.append(Finding("error", "MISSING_FILE", f"Missing required file: {rel}", rel))

def contains_all(text: str, required: Iterable[str]) -> list[str]:
    low = text.lower()
    return [token for token in required if token.lower() not in low]

def check_text(findings: list[Finding], root: Path, rel: str, required_tokens: list[str]) -> None:
    add_missing(findings, root, rel)
    p = root / rel
    if not p.exists():
        return
    try:
        text = load_text(p)
    except Exception as exc:
        findings.append(Finding("error", "TEXT_READ", f"Failed to read {rel}: {exc}", rel))
        return
    missing = contains_all(text, required_tokens)
    if missing:
        findings.append(Finding("error", "TEXT_CONTENT", f"{rel} missing required terms: {', '.join(missing)}", rel))

def check_json(findings: list[Finding], root: Path, rel: str) -> Any | None:
    add_missing(findings, root, rel)
    p = root / rel
    if not p.exists():
        return None
    try:
        return load_json(p)
    except Exception as exc:
        findings.append(Finding("error", "JSON_PARSE", f"Failed to parse {rel}: {exc}", rel))
        return None

def validate_meta_model(root: Path, findings: list[Finding]) -> dict[str, Any] | None:
    schema = check_json(findings, root, "governance.meta.schema.json")
    example = check_json(findings, root, "governance.meta.example.json")
    if not schema or not example:
        return None

    # Required top-level keys
    for key in schema.get("required", []):
        if key not in example:
            findings.append(Finding("error", "META_REQUIRED_FIELD", f"Meta-model missing required field: {key}"))

    # Version sanity
    if example.get("meta_version") != "3.0.0":
        findings.append(Finding("error", "META_VERSION", f"meta_version should be 3.0.0, got {example.get('meta_version')}"))

    # Canonical layers
    required_layers = [
        "core", "skills", "state", "runtime", "validation", "security", "judging",
        "experience", "templates", "policies", "topology", "decision", "telemetry",
        "economics", "gitops", "learning", "meta_model"
    ]
    layers = example.get("layers", {})
    for layer in required_layers:
        if layer not in layers:
            findings.append(Finding("error", "META_LAYER_MISSING", f"Missing canonical layer: {layer}", f"layers.{layer}"))

    # Skills registry
    skills = example.get("skills", {})
    for key in ("manifest", "contract", "catalog"):
        if key not in skills:
            findings.append(Finding("error", "SKILLS_META_MISSING", f"Missing skills metadata field: {key}", f"skills.{key}"))

    # Invariants
    invs = example.get("invariants", [])
    if not invs:
        findings.append(Finding("error", "META_INVARIANTS_EMPTY", "Meta-model has no invariants"))
    seen = set()
    for inv in invs:
        inv_id = inv.get("id")
        if not inv_id:
            findings.append(Finding("error", "META_INVARIANT_ID", "Invariant missing id"))
        if inv_id in seen:
            findings.append(Finding("error", "META_DUP_INVARIANT", f"Duplicate invariant id: {inv_id}"))
        seen.add(inv_id)
        for field in ("statement", "severity", "enforcement", "evidence_required"):
            if field not in inv:
                findings.append(Finding("error", "META_INVARIANT_FIELD", f"Invariant {inv_id} missing field: {field}", f"invariants.{inv_id}"))

    # Canonical core relationships
    rels = example.get("relationships", [])
    if not rels:
        findings.append(Finding("error", "META_REL_EMPTY", "Meta-model has no relationships"))

    core_state_writes = [r for r in rels if r.get("from") == "core" and r.get("to") == "state" and r.get("mode") == "writes"]
    if not core_state_writes:
        findings.append(Finding("error", "META_CANONICAL_WRITE_RULE", "Missing explicit core -> state write rule"))
    elif any(r.get("allowed") is True for r in core_state_writes):
        findings.append(Finding("error", "META_CANONICAL_WRITE_RULE", "Core must not be allowed to write state directly"))

    # Meta-model file references
    meta_model = example.get("meta_model", {})
    for key, expected in {
        "schema": "governance.meta.schema.json",
        "example": "governance.meta.example.json",
        "system_consistency": "meta-model/system-consistency.md",
        "validator": "validator_v3.py",
    }.items():
        if meta_model.get(key) != expected:
            findings.append(Finding("error", "META_META_MODEL_REF", f"meta_model.{key} must point to {expected}", f"meta_model.{key}"))

    return example

def validate_cross_layer(root: Path, example: dict[str, Any], findings: list[Finding]) -> None:
    # Files that must exist in the final tree
    required_files = [
        "README.md",
        "meta-model/README.md",
        "meta-model/system-consistency.md",
        "kit/skills/README.md",
        "kit/skills/manifest.md",
        "kit/skills/skill-contract.md",
        "kit/skills/skill-catalog.md",
        "kit/policies/human-in-the-loop-policy.md",
        "kit/core/protocols/react-loop.md",
        "kit/runtime/engine/react-loop.md",
        "kit/runtime/engine/react-runtime-contract.md",
        "kit/runtime/engine/react-telemetry-events.md",
        "kit/validation/step-consistency.md",
        "kit/judging/llm-judge.md",
        "kit/judging/judge-rubric.md",
        "kit/judging/judge-output.schema.json",
        "kit/judging/judge-integration.md",
        "kit/playbooks/skeleton-of-thought.md",
        "governance/decision/tot-guidance.md",
        "kit/core/protocols/exploration-protocol.md",
        "runtime/telemetry/events.schema.json",
        "learning/pattern-evolution.md",
    ]
    for rel in required_files:
        add_missing(findings, root, rel)

    # System consistency text
    check_text(findings, root, "meta-model/system-consistency.md", ["state", "artifacts", "decisions", "telemetry", "policies", "version", "skills", "workflow"])
    # Step consistency text
    check_text(findings, root, "kit/validation/step-consistency.md", ["inputs", "outputs", "exit criteria", "exploration", "validation"])
    # HITL
    check_text(findings, root, "kit/policies/human-in-the-loop-policy.md", ["irreversible", "security", "budget", "validation", "policy", "drift", "block", "approval"])
    # ReAct
    check_text(findings, root, "kit/core/protocols/react-loop.md", ["observe", "reason", "act", "verify", "merge", "orchestrator", "exploration"])
    check_text(findings, root, "kit/runtime/engine/react-loop.md", ["observe", "reason", "act", "verify", "human", "soT".lower(), "toT".lower(), "state router"])
    # SoT / ToT
    check_text(findings, root, "kit/playbooks/skeleton-of-thought.md", ["outline", "expand", "validate", "telemetry"])
    check_text(findings, root, "governance/decision/tot-guidance.md", ["branches", "score", "prune", "decision record", "telemetry"])
    check_text(findings, root, "kit/core/protocols/exploration-protocol.md", ["sot", "tot", "complementary", "not interchangeable"])
    # Skills
    check_text(findings, root, "kit/skills/skill-contract.md", ["objective", "inputs", "outputs", "constraints", "evidence", "boundaries", "version"])
    check_text(findings, root, "kit/skills/manifest.md", ["skill", "purpose", "reusable", "versioned"])
    # Judge schema
    judge = check_json(findings, root, "kit/judging/judge-output.schema.json")
    if judge:
        required_dims = ["clarity", "completeness", "consistency", "correctness", "security_awareness", "maintainability", "performance_awareness", "cost_awareness"]
        dims = judge.get("properties", {}).get("dimensions", {}).get("required", [])
        missing_dims = [d for d in required_dims if d not in dims]
        if missing_dims:
            findings.append(Finding("error", "JUDGE_SCHEMA", f"Judge schema missing dimensions: {', '.join(missing_dims)}"))
    # Telemetry events
    tele = check_json(findings, root, "runtime/telemetry/events.schema.json")
    if tele:
        enum = tele.get("properties", {}).get("event_type", {}).get("enum", [])
        expected_events = [
            "react_observed", "react_reasoned", "react_action_started", "react_action_completed", "react_verified", "react_blocked",
            "sot_outline_created", "sot_section_expanded", "sot_structure_validated", "sot_artifact_refined",
            "tot_branch_created", "tot_branch_scored", "tot_branch_pruned", "tot_branch_selected", "tot_decision_recorded",
            "human_intervention_required", "intervention_triggered", "intervention_reason", "intervention_role", "intervention_outcome"
        ]
        missing_events = [e for e in expected_events if e not in enum]
        if missing_events:
            findings.append(Finding("error", "TELEMETRY_EVENTS", f"Telemetry schema missing events: {', '.join(missing_events)}"))
    # Meta-model layer path sanity
    expected_paths = {
        "core": "kit/core",
        "skills": "kit/skills",
        "state": "kit/state",
        "runtime": "kit/runtime",
        "validation": "kit/validation",
        "security": "security",
        "judging": "kit/judging",
        "experience": "kit/experience",
        "templates": "kit/templates",
        "policies": "kit/policies",
        "topology": "governance/topology",
        "decision": "governance/decision",
        "telemetry": "runtime/telemetry",
        "economics": "governance/economics",
        "gitops": "governance/gitops",
        "learning": "learning",
        "meta_model": "meta-model",
    }
    for layer, expected in expected_paths.items():
        actual = example.get("layers", {}).get(layer, {}).get("path")
        if actual != expected:
            findings.append(Finding("error", "LAYER_PATH", f"layers.{layer}.path must be {expected}, got {actual}", f"layers.{layer}.path"))

    # Skill paths
    for key, expected in {
        "manifest": "kit/skills/manifest.md",
        "contract": "kit/skills/skill-contract.md",
        "catalog": "kit/skills/skill-catalog.md",
    }.items():
        actual = example.get("skills", {}).get(key)
        if actual != expected:
            findings.append(Finding("error", "SKILL_REF", f"skills.{key} must point to {expected}, got {actual}", f"skills.{key}"))

def report(findings: list[Finding]) -> int:
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    if errors:
        print("VALIDATION FAILED")
    else:
        print("VALIDATION PASSED")
    print()

    for f in findings:
        prefix = "ERROR" if f.severity == "error" else "WARN "
        loc = f" ({f.path})" if f.path else ""
        print(f"[{prefix}] {f.code}: {f.message}{loc}")

    print()
    print(f"Errors: {len(errors)} | Warnings: {len(warnings)}")
    return 1 if errors else 0

def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise-grade validator for AgenOps")
    parser.add_argument("--root", default=".", help="Root directory of the project")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.exists():
        print(f"Root not found: {root}", file=sys.stderr)
        return 2

    findings: list[Finding] = []
    example = validate_meta_model(root, findings)
    if example:
        validate_cross_layer(root, example, findings)

    # Additional directories
    for d in ["kit", "governance", "runtime", "learning", "docs", "planning_artifacts", "meta-model", "security"]:
        if not (root / d).exists():
            findings.append(Finding("error", "MISSING_DIR", f"Missing required directory: {d}", d))

    return report(findings)

if __name__ == "__main__":
    raise SystemExit(main())
