#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

@dataclass
class Finding:
    severity: str  # error | warning
    code: str
    message: str
    path: str | None = None

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def load_json(path: Path) -> Any:
    return json.loads(load_text(path))

def exists(root: Path, rel: str) -> bool:
    return (root / rel).exists()

def must_exist(findings: list[Finding], root: Path, rel: str) -> None:
    if not exists(root, rel):
        findings.append(Finding("error", "MISSING_FILE", f"Missing required file: {rel}", rel))

def contains_all(text: str, required: Iterable[str]) -> list[str]:
    missing = []
    low = text.lower()
    for token in required:
        if token.lower() not in low:
            missing.append(token)
    return missing

def validate_text_file(findings: list[Finding], root: Path, rel: str, required_tokens: list[str]) -> None:
    path = root / rel
    must_exist(findings, root, rel)
    if not path.exists():
        return
    try:
        text = load_text(path)
    except Exception as exc:
        findings.append(Finding("error", "TEXT_READ", f"Failed to read {rel}: {exc}", rel))
        return
    missing = contains_all(text, required_tokens)
    if missing:
        findings.append(Finding("error", "TEXT_CONTENT", f"{rel} missing required terms: {', '.join(missing)}", rel))

def validate_meta_model(root: Path, findings: list[Finding]) -> dict[str, Any] | None:
    schema_path = root / "governance.meta.schema.json"
    example_path = root / "governance.meta.example.json"

    must_exist(findings, root, "governance.meta.schema.json")
    must_exist(findings, root, "governance.meta.example.json")
    if not schema_path.exists() or not example_path.exists():
        return None

    try:
        schema = load_json(schema_path)
        example = load_json(example_path)
    except Exception as exc:
        findings.append(Finding("error", "JSON_PARSE", f"Failed to parse meta-model JSON: {exc}"))
        return None

    required_top = schema.get("required", [])
    missing_top = [k for k in required_top if k not in example]
    if missing_top:
        findings.append(Finding("error", "META_REQUIRED_FIELD", f"Meta-model missing required fields: {', '.join(missing_top)}"))

    layers = example.get("layers", {})
    required_layers = [
        "core","state","runtime","validation","security","judging","experience","templates","policies",
        "topology","decision","telemetry","economics","gitops","learning"
    ]
    for layer in required_layers:
        if layer not in layers:
            findings.append(Finding("error", "META_LAYER_MISSING", f"Meta-model missing layer: {layer}", f"layers.{layer}"))

    invariants = example.get("invariants", [])
    if not invariants:
        findings.append(Finding("error", "META_INVARIANTS_EMPTY", "Meta-model has no invariants"))
    else:
        ids = [inv.get("id") for inv in invariants]
        dup_ids = sorted({i for i in ids if i is not None and ids.count(i) > 1})
        if dup_ids:
            findings.append(Finding("error", "META_DUP_INVARIANTS", f"Duplicate invariant ids: {', '.join(dup_ids)}"))
        for inv in invariants:
            for key in ("id", "statement", "severity", "enforcement", "evidence_required"):
                if key not in inv:
                    findings.append(Finding("error", "META_INVARIANT_FIELD", f"Invariant missing '{key}'", f"invariants.{inv.get('id','?')}"))
            if inv.get("severity") not in {"info", "warning", "error", "critical"}:
                findings.append(Finding("error", "META_INVARIANT_SEVERITY", f"Invalid invariant severity: {inv.get('severity')}", f"invariants.{inv.get('id','?')}"))

    rels = example.get("relationships", [])
    if not rels:
        findings.append(Finding("error", "META_REL_EMPTY", "Meta-model has no relationships"))
    allowed_modes = {"reads","writes","validates","governs","orchestrates","advises","routes","observes","costs","learns","deploys"}
    for rel in rels:
        for key in ("from", "to", "mode", "allowed"):
            if key not in rel:
                findings.append(Finding("error", "META_REL_FIELD", f"Relationship missing '{key}'"))
        if rel.get("mode") not in allowed_modes:
            findings.append(Finding("error", "META_REL_MODE", f"Invalid relationship mode: {rel.get('mode')}"))
    core_state_writes = [r for r in rels if r.get("from") == "core" and r.get("to") == "state" and r.get("mode") == "writes"]
    if not core_state_writes:
        findings.append(Finding("error", "META_CANONICAL_WRITE_RULE", "Missing explicit core -> state write rule"))
    elif any(r.get("allowed") is True for r in core_state_writes):
        findings.append(Finding("error", "META_CANONICAL_WRITE_RULE", "Core must not be allowed to write state directly"))

    lifecycle = example.get("artifact_lifecycle", {})
    states = lifecycle.get("states", [])
    if sorted(states) != sorted(["draft","reviewed","approved","archived"]):
        findings.append(Finding("error", "LIFECYCLE_STATES", f"Unexpected artifact lifecycle states: {states}"))
    transitions = lifecycle.get("transitions", [])
    if not transitions:
        findings.append(Finding("error", "LIFECYCLE_TRANSITIONS_EMPTY", "No artifact lifecycle transitions defined"))
    else:
        required_pairs = {("draft", "reviewed"), ("reviewed", "approved"), ("approved", "archived")}
        actual_pairs = {(t.get("from"), t.get("to")) for t in transitions}
        missing_pairs = sorted(required_pairs - actual_pairs)
        if missing_pairs:
            findings.append(Finding("error", "LIFECYCLE_TRANSITIONS_MISSING", f"Missing transitions: {missing_pairs}"))
        for t in transitions:
            requires = t.get("requires", [])
            if not isinstance(requires, list) or not requires:
                findings.append(Finding("error", "LIFECYCLE_TRANSITION_RULES", f"Transition {t.get('from')}->{t.get('to')} missing requires"))
    promo = lifecycle.get("promotion_rule", "")
    missing = contains_all(promo, ["planning_artifacts/", "docs/"])
    if missing:
        findings.append(Finding("error", "LIFECYCLE_PROMOTION_RULE", f"Promotion rule missing tokens: {', '.join(missing)}"))

    dec = example.get("decision_framework", {})
    criteria = dec.get("criteria", [])
    expected_criteria = ["cost","benefit","reversibility","systemic_impact","risk","time_to_implement","maintainability","auditability"]
    missing_criteria = [c for c in expected_criteria if c not in criteria]
    if missing_criteria:
        findings.append(Finding("error", "DECISION_CRITERIA", f"Missing decision criteria: {', '.join(missing_criteria)}"))
    if not dec.get("template"):
        findings.append(Finding("error", "DECISION_TEMPLATE", "Decision framework template path missing"))

    sec = example.get("security", {})
    if not sec.get("threat_model"):
        findings.append(Finding("error", "SEC_THREAT_MODEL", "Missing security threat model"))
    if not sec.get("agent_permissions"):
        findings.append(Finding("error", "SEC_AGENT_PERMISSIONS", "Missing agent permissions schema"))
    tb = sec.get("trust_boundaries", [])
    expected_tb_tokens = [
        "external_input_to_system",
        "planning_artifacts_to_canonical_state",
        "agent_local_context_to_shared_state",
        "shared_state_to_approved_artifacts",
        "runtime_telemetry_to_learning",
    ]
    for token in expected_tb_tokens:
        if token not in tb:
            findings.append(Finding("error", "SEC_TRUST_BOUNDARY", f"Missing trust boundary: {token}"))

    obs = example.get("observability", {})
    if not obs.get("events_schema"):
        findings.append(Finding("error", "OBS_EVENTS_SCHEMA", "Missing telemetry events schema"))
    metrics = obs.get("metrics", [])
    expected_metrics = ["contract_compliance","planning_execution_drift","review_latency_ms","retry_count","token_usage","trace_completeness"]
    for m in expected_metrics:
        if m not in metrics:
            findings.append(Finding("error", "OBS_METRIC", f"Missing observability metric: {m}"))

    econ = example.get("economics", {})
    if not econ.get("budget_schema"):
        findings.append(Finding("error", "ECON_BUDGET_SCHEMA", "Missing budget schema"))
    if not econ.get("cost_model"):
        findings.append(Finding("error", "ECON_COST_MODEL", "Missing cost model"))
    controls = econ.get("budget_controls", [])
    expected_controls = ["soft_limit_warning", "hard_limit_block", "approval_over_threshold", "drift_based_review"]
    for c in expected_controls:
        if c not in controls:
            findings.append(Finding("error", "ECON_CONTROL", f"Missing budget control: {c}"))

    gitops = example.get("gitops", {})
    for key, code in [("semantic_versioning", "GITOPS_SEMVER"), ("conventional_commits", "GITOPS_COMMITS"), ("gitflow", "GITOPS_FLOW")]:
        if not gitops.get(key):
            findings.append(Finding("error", code, f"Missing GitOps field: {key}"))

    learning = example.get("learning", {})
    for key in ("incidents", "retrospectives", "pattern_evolution"):
        if not learning.get(key):
            findings.append(Finding("error", "LEARNING_FIELD", f"Missing learning layer field: {key}"))

    return example

def validate_system_consistency(root: Path, findings: list[Finding]) -> None:
    validate_text_file(findings, root, "meta-model/system-consistency.md", ["state", "artifacts", "decisions", "telemetry", "policies", "version"])
    validate_text_file(findings, root, "kit/validation/step-consistency.md", ["inputs", "outputs", "exit criteria", "transitions", "validation"])
    validate_text_file(findings, root, "kit/policies/human-in-the-loop-policy.md", ["irreversible", "high systemic impact", "security", "budget", "validation", "policy exceptions", "drift", "block"])
    validate_text_file(findings, root, "kit/runtime/engine/react-loop.md", ["observe", "reason", "act", "verify", "soT", "ToT"])
    validate_text_file(findings, root, "kit/judging/llm-judge.md", ["advisory", "validation", "score", "recommendation"])
    validate_text_file(findings, root, "kit/judging/judge-rubric.md", ["clarity", "completeness", "consistency", "correctness", "security_awareness", "maintainability", "performance_awareness", "cost_awareness"])
    validate_text_file(findings, root, "governance/decision/tot-guidance.md", ["branches", "score", "prune", "decision record"])
    validate_text_file(findings, root, "kit/playbooks/skeleton-of-thought.md", ["outline", "expand", "validate"])
    validate_text_file(findings, root, "kit/core/protocols/exploration-protocol.md", ["sot", "tot", "complementary", "not interchangeable"])
    validate_text_file(findings, root, "runtime/telemetry/events.schema.json", ["sot_outline_created", "tot_branch_created", "react_observed"])

def validate_cross_layer_consistency(root: Path, example: dict[str, Any], findings: list[Finding]) -> None:
    checks = [
        ("decision", "template", "governance/decision/decision-template.md"),
        ("security", "agent_permissions", "security/agent-permissions.schema.json"),
        ("security", "threat_model", "security/threat-model.md"),
        ("observability", "events_schema", "runtime/telemetry/events.schema.json"),
        ("economics", "budget_schema", "governance/economics/execution-budget.schema.json"),
        ("gitops", "semantic_versioning", "governance/gitops/semantic-versioning.md"),
        ("learning", "pattern_evolution", "learning/pattern-evolution.md"),
    ]
    for section, key, expected in checks:
        actual = example.get(section, {}).get(key)
        if actual != expected:
            findings.append(Finding("error", "META_CROSS_LINK", f"{section}.{key} must point to {expected}, got {actual}", f"{section}.{key}"))

def validate_exploration_protocols(root: Path, findings: list[Finding]) -> None:
    for rel in [
        "kit/playbooks/skeleton-of-thought.md",
        "governance/decision/tot-guidance.md",
        "kit/core/protocols/exploration-protocol.md",
    ]:
        must_exist(findings, root, rel)

    def read(rel: str) -> str:
        p = root / rel
        return p.read_text(encoding="utf-8").lower() if p.exists() else ""

    sot = read("kit/playbooks/skeleton-of-thought.md")
    tot = read("governance/decision/tot-guidance.md")
    proto = read("kit/core/protocols/exploration-protocol.md")

    for term in ["outline", "expand", "validate"]:
        if term not in sot:
            findings.append(Finding("error", "SOT_INCOMPLETE", f"SoT file missing term: {term}"))

    for term in ["branches", "score", "prune", "decision record"]:
        if term not in tot:
            findings.append(Finding("error", "TOT_INCOMPLETE", f"ToT file missing term: {term}"))

    for term in ["sot", "tot", "complementary", "not interchangeable"]:
        if term not in proto:
            findings.append(Finding("error", "EXPLORATION_PROTOCOL_INCOMPLETE", f"Exploration protocol missing term: {term}"))

    schema_path = root / "runtime/telemetry/events.schema.json"
    if schema_path.exists():
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            enum = schema["properties"]["event_type"]["enum"]
            expected = [
                "sot_outline_created",
                "sot_section_expanded",
                "sot_structure_validated",
                "sot_artifact_refined",
                "tot_branch_created",
                "tot_branch_scored",
                "tot_branch_pruned",
                "tot_branch_selected",
                "tot_decision_recorded",
            ]
            for e in expected:
                if e not in enum:
                    findings.append(Finding("error", "EXPLORATION_TELEMETRY_MISSING", f"Missing telemetry event: {e}"))
        except Exception as exc:
            findings.append(Finding("error", "EXPLORATION_SCHEMA_PARSE", f"Could not parse telemetry schema: {exc}"))

def validate_hitl_policy(root: Path, findings: list[Finding]) -> None:
    path = root / "kit/policies/human-in-the-loop-policy.md"
    if not path.exists():
        findings.append(Finding("error", "HITL_MISSING", "Human-in-the-loop policy missing", "kit/policies/human-in-the-loop-policy.md"))
        return

    text = path.read_text(encoding="utf-8").lower()
    for term in ["irreversible", "security", "budget", "validation", "policy", "drift", "block", "approval"]:
        if term not in text:
            findings.append(Finding("error", "HITL_INCOMPLETE", f"Missing term: {term}", "kit/policies/human-in-the-loop-policy.md"))

def validate_judge_schema(root: Path, findings: list[Finding]) -> None:
    path = root / "kit/judging/judge-output.schema.json"
    if not path.exists():
        findings.append(Finding("error", "JUDGE_SCHEMA_MISSING", "Missing judge output schema", str(path)))
        return
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        findings.append(Finding("error", "JUDGE_SCHEMA_PARSE", f"Could not parse judge schema: {exc}", str(path)))
        return

    props = schema.get("properties", {})
    score = props.get("score", {})
    if score.get("minimum") != 0 or score.get("maximum") != 100:
        findings.append(Finding("error", "JUDGE_SCORE_RANGE", "Judge score must be constrained to 0..100", str(path)))

    dims = props.get("dimensions", {})
    if dims.get("additionalProperties", True):
        findings.append(Finding("error", "JUDGE_DIMENSIONS_OPEN", "Judge dimensions must forbid additional properties", str(path)))

    expected_dims = [
        "clarity",
        "completeness",
        "consistency",
        "correctness",
        "security_awareness",
        "maintainability",
        "performance_awareness",
        "cost_awareness",
    ]
    dim_props = dims.get("properties", {})
    for d in expected_dims:
        if d not in dim_props:
            findings.append(Finding("error", "JUDGE_DIMENSION_MISSING", f"Missing judge dimension: {d}", str(path)))
        else:
            rng = dim_props[d]
            if rng.get("minimum") != 0 or rng.get("maximum") != 5:
                findings.append(Finding("error", "JUDGE_DIMENSION_RANGE", f"Dimension {d} must be 0..5", f"{path}:{d}"))

def validate_file_presence(root: Path, findings: list[Finding]) -> None:
    required = [
        "README.md",
        "governance.meta.schema.json",
        "governance.meta.example.json",
        "integration-map.md",
        "rules.md",
        "validator.py",
        "validator_v3.py",
        "meta-model/system-consistency.md",
        "kit/validation/step-consistency.md",
        "kit/policies/human-in-the-loop-policy.md",
        "kit/core/protocols/react-loop.md",
        "kit/runtime/engine/react-loop.md",
        "kit/runtime/engine/react-runtime-contract.md",
        "kit/runtime/engine/react-telemetry-events.md",
        "kit/judging/llm-judge.md",
        "kit/judging/judge-rubric.md",
        "kit/judging/judge-output.schema.json",
        "kit/judging/judge-integration.md",
        "governance/decision/tot-guidance.md",
        "governance/decision/tot-example.md",
        "kit/playbooks/skeleton-of-thought.md",
        "kit/playbooks/sot-workflow.example.md",
        "kit/core/protocols/exploration-protocol.md",
        "runtime/telemetry/events.schema.json",
        "governance/economics/execution-budget.schema.json",
        "governance/economics/cost-model.md",
        "governance/gitops/semantic-versioning.md",
        "governance/gitops/conventional-commits.md",
        "governance/gitops/gitflow.md",
        "learning/pattern-evolution.md",
        "governance/topology/team-types.md",
        "governance/topology/ownership-map.yaml",
        "governance/topology/interaction-modes.md",
        "governance/topology/flow-model.md",
        "security/threat-model.md",
        "security/trust-boundaries.md",
        "security/agent-permissions.schema.json",
    ]
    for rel in required:
        must_exist(findings, root, rel)

def report(findings: list[Finding]) -> int:
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    print("VALIDATION FAILED" if errors else "VALIDATION PASSED")
    print()
    for f in findings:
        prefix = "ERROR" if f.severity == "error" else "WARN "
        if f.path:
            print(f"[{prefix}] {f.code}: {f.message} ({f.path})")
        else:
            print(f"[{prefix}] {f.code}: {f.message}")
    print()
    print(f"Errors: {len(errors)} | Warnings: {len(warnings)}")
    return 1 if errors else 0

def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise cross-layer validator for the governance system")
    parser.add_argument("--root", default=".", help="Root directory of the governance system")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"Root path does not exist: {root}", file=sys.stderr)
        return 2

    findings: list[Finding] = []
    validate_file_presence(root, findings)
    example = validate_meta_model(root, findings)
    if example:
        validate_cross_layer_consistency(root, example, findings)
    validate_system_consistency(root, findings)
    validate_hitl_policy(root, findings)
    validate_judge_schema(root, findings)
    validate_exploration_protocols(root, findings)

    return report(findings)

if __name__ == "__main__":
    raise SystemExit(main())
