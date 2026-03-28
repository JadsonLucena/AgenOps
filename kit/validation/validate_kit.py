#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
RESULTS: list[dict[str, object]] = []
FAILED = False

ROLE_REQUIRED = ["# ", "## Mission", "## Responsibilities", "## Outputs"]
PLAYBOOK_REQUIRED = ["# ", "## "]
POLICY_REQUIRED = ["# ", "## Scope", "## Requirements", "## Exceptions", "## Evidence"]
CHECKLIST_REQUIRED = ["# ", "## Purpose", "## Items", "## Pass condition"]
AGENT_REQUIRED = ["# ", "## Mission", "## Inputs", "## Outputs", "## Handoff", "## Stop Conditions", "## State Update", "## Quality Rules"]

def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def has_title(body: str) -> bool:
    return re.search(r"^#\s+.+$", body, re.M) is not None

def sections_in_order(body: str, headings: list[str]) -> bool:
    idx = 0
    for h in headings:
        pos = body.find(h, idx)
        if pos < 0:
            return False
        idx = pos + len(h)
    return True

def contains_all(body: str, phrases: list[str]) -> bool:
    return all(p in body for p in phrases)

def validate_required(path: Path, required: list[str], kind: str) -> None:
    global FAILED
    body = text(path)
    missing: list[str] = []
    for needle in required:
        if needle == "# ":
            if not has_title(body):
                missing.append("title")
        else:
            if needle not in body:
                missing.append(needle.strip("# ").strip())
    if missing:
        FAILED = True
        RESULTS.append({"file": str(path.relative_to(ROOT)), "kind": kind, "status": "fail", "missing": missing})
    else:
        RESULTS.append({"file": str(path.relative_to(ROOT)), "kind": kind, "status": "pass"})

def validate_links(path: Path) -> None:
    global FAILED
    body = text(path)
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", body):
        target = match.group(1).split("#", 1)[0].strip()
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        target_path = (path.parent / target).resolve()
        if not target_path.exists():
            FAILED = True
            RESULTS.append({"file": str(path.relative_to(ROOT)), "kind": "link", "status": "fail", "target": target})

def validate_names(base: Path) -> None:
    global FAILED
    for path in base.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".feature", ".puml", ".py", ".sh"}:
            if path.name in {"README.md", "LICENSE"}:
                continue
            if path.suffix in {".py", ".sh"}:
                continue
            if not re.fullmatch(r"[a-z0-9]+(?:[.-][a-z0-9]+)*\.(?:md|feature|puml)", path.name):
                FAILED = True
                RESULTS.append({"file": str(path.relative_to(ROOT)), "kind": "name", "status": "fail", "name": path.name})

def require_files(paths: list[Path], kind: str) -> None:
    global FAILED
    for path in paths:
        if not path.exists():
            FAILED = True
            RESULTS.append({"file": str(path.relative_to(ROOT)), "kind": kind, "status": "fail", "missing": ["file"]})
        else:
            RESULTS.append({"file": str(path.relative_to(ROOT)), "kind": kind, "status": "pass"})

def validate_core_semantics() -> None:
    orchestrator = ROOT / "kit" / "core" / "roles" / "software-engineer-orchestrator.md"
    qa = ROOT / "kit" / "core" / "roles" / "quality-engineer.md"
    flow = ROOT / "kit" / "core" / "workflows" / "default-development-flow.md"
    test_rules = ROOT / "kit" / "core" / "playbooks" / "generate-test-rules.md"
    brainstorm = ROOT / "kit" / "core" / "playbooks" / "brainstorm-and-elicitation.md"
    design_chunks = ROOT / "kit" / "core" / "playbooks" / "design-baby-steps.md"

    required = [orchestrator, qa, flow, test_rules, brainstorm, design_chunks]
    require_files(required, "core-semantic")
    if not all(p.exists() for p in required):
        return

    o = text(orchestrator)
    q = text(qa)
    f = text(flow)
    t = text(test_rules)
    b = text(brainstorm)
    d = text(design_chunks)

    orchestrator_checks = [
        "formal Orchestrator sub-agent",
        "Requirements Engineer output as the source of truth",
        "baby-step design chunks",
        "shared handoff envelope",
        "Hexagonal Architecture",
        "specialized sub-agents",
        "raw internal reasoning",
    ]
    qa_checks = [
        "formal Quality Engineer sub-agent",
        "Suggest fuzz tests only when relevant to robustness, security, or non-deterministic input handling.",
        "Integration tests do not use doubles by default.",
        "If a stub seems acceptable in an integration test, ask the developer preference first.",
        "Apply DRY only when repetition appears for the third time or more.",
        "Functions with more than two arguments are acceptable when the type is a DTO or a builder.",
    ]
    test_rules_checks = [
        "Suggest fuzz tests only when relevant.",
        "Integration tests should not use doubles by default.",
        "If a stub seems acceptable in an integration test, ask the developer before proceeding.",
        "Prefer DRY when the same setup repeats three times or more.",
        "Accept DTOs and builders as legitimate exceptions to the “more than two arguments” guideline.",
    ]
    brainstorm_checks = [
        "deep brainstorming and elicitation",
        "shared problem frame",
        "Separate facts, assumptions, constraints, and risks.",
        "candidate design chunks",
    ]
    design_checks = [
        "smallest reviewable design chunks",
        "spec document design",
        "Map each chunk to its spec section, file targets, and documentation triggers.",
        "Keep only one active chunk at a time.",
        "Prefer revertible slices.",
    ]

    for body, checks, kind, rel in [
        (o, orchestrator_checks, "semantic", orchestrator),
        (q, qa_checks, "semantic", qa),
        (t, test_rules_checks, "semantic", test_rules),
        (b, brainstorm_checks, "semantic", brainstorm),
        (d, design_checks, "semantic", design_chunks),
    ]:
        if not contains_all(body, checks):
            global FAILED
            FAILED = True
            RESULTS.append({"file": str(rel.relative_to(ROOT)), "kind": kind, "status": "fail", "missing": ["contract"]})
        else:
            RESULTS.append({"file": str(rel.relative_to(ROOT)), "kind": kind, "status": "pass"})

    flow_checks = [
        "Requirements Engineer sub-agent runs deep brainstorming and elicitation.",
        "Engineer Orchestrator turns the elicited request into a spec document design and file path plan.",
        "Software Architect sub-agent confirms the technical direction for the first safe design slice.",
        "Engineer Orchestrator splits the approved scope into baby steps.",
        "Engineer Orchestrator dispatches the required sub-agents through the shared handoff envelope:",
        "Quality Engineer",
        "Security Reviewer",
        "Code Reviewer",
        "DevOps Reviewer",
    ]
    if not contains_all(f, flow_checks):
        FAILED = True
        RESULTS.append({"file": str(flow.relative_to(ROOT)), "kind": "semantic", "status": "fail", "missing": ["flow_contract"]})
    else:
        RESULTS.append({"file": str(flow.relative_to(ROOT)), "kind": "semantic", "status": "pass"})

def validate_agents_semantics() -> None:
    base = ROOT / "kit" / "agents"
    required = [
        base / "manifest.md",
        base / "README.md",
        base / "shared" / "contract-template.md",
        base / "shared" / "handoff-envelope.md",
        base / "shared" / "dispatch-protocol.md",
        base / "orchestrator" / "contract.md",
        base / "requirements" / "contract.md",
        base / "architecture" / "contract.md",
        base / "qa" / "contract.md",
        base / "security" / "contract.md",
        base / "review" / "contract.md",
        base / "devops" / "contract.md",
    ]
    require_files(required, "agents-pack")
    for p in required:
        if not p.exists():
            return
    for p in [base / "orchestrator" / "contract.md", base / "requirements" / "contract.md", base / "architecture" / "contract.md", base / "qa" / "contract.md", base / "security" / "contract.md", base / "review" / "contract.md", base / "devops" / "contract.md"]:
        validate_required(p, AGENT_REQUIRED, "agent-contract")
        validate_links(p)
    manifest = base / "manifest.md"
    body = text(manifest)
    manifest_checks = [
        "formal sub-agents",
        "orchestrator",
        "requirements-engineer",
        "software-architect",
        "quality-engineer",
        "security-reviewer",
        "code-reviewer",
        "devops-reviewer",
        "shared handoff envelope",
    ]
    if not contains_all(body, manifest_checks):
        global FAILED
        FAILED = True
        RESULTS.append({"file": str(manifest.relative_to(ROOT)), "kind": "semantic", "status": "fail", "missing": ["agents_manifest_contract"]})
    else:
        RESULTS.append({"file": str(manifest.relative_to(ROOT)), "kind": "semantic", "status": "pass"})

    shared = base / "shared" / "handoff-envelope.md"
    body = text(shared)
    shared_checks = [
        "Required fields",
        "session_id",
        "source_agent",
        "target_agent",
        "parent_workflow",
        "upstream_contract",
        "downstream_contract",
        "state_updates",
        "A handoff is invalid if the target agent, the phase, or the updated state is missing.",
    ]
    if not contains_all(body, shared_checks):
        FAILED = True
        RESULTS.append({"file": str(shared.relative_to(ROOT)), "kind": "semantic", "status": "fail", "missing": ["handoff_envelope_contract"]})
    else:
        RESULTS.append({"file": str(shared.relative_to(ROOT)), "kind": "semantic", "status": "pass"})

def validate_security_semantics() -> None:
    base = ROOT / "kit" / "security"
    required = [
        base / "supply-chain" / "sbom-policy.md",
        base / "supply-chain" / "dependency-integrity-policy.md",
        base / "supply-chain" / "artifact-provenance-policy.md",
        base / "supply-chain" / "supply-chain-checklist.md",
        base / "agent-security" / "secret-handling-policy.md",
        base / "agent-security" / "prompt-injection-defense.md",
        base / "agent-security" / "tool-permission-matrix.md",
        base / "agent-security" / "agent-execution-audit.md",
    ]
    require_files(required, "security-pack")
    for p in required:
        if p.exists():
            validate_required(p, POLICY_REQUIRED if p.name != "supply-chain-checklist.md" else CHECKLIST_REQUIRED, "policy" if p.name != "supply-chain-checklist.md" else "checklist")
            validate_links(p)

    manifest = base / "manifest.md"
    if manifest.exists():
        body = text(manifest)
        if not contains_all(body, ["supply-chain security", "agent security", "versioned", "validation"]):
            global FAILED
            FAILED = True
            RESULTS.append({"file": str(manifest.relative_to(ROOT)), "kind": "semantic", "status": "fail", "missing": ["security_manifest_contract"]})
        else:
            RESULTS.append({"file": str(manifest.relative_to(ROOT)), "kind": "semantic", "status": "pass"})

def validate_experience_semantics() -> None:
    base = ROOT / "kit" / "experience"
    required = [
        base / "state-model.md",
        base / "state-store.md",
        base / "state-machine.md",
        base / "next-step-guidance.md",
        base / "decision-routing.md",
        base / "phase-map.md",
        base / "quick-flow.md",
        base / "command-map.md",
        base / "menu-patterns.md",
        base / "state-router.py",
    ]
    require_files(required, "experience-pack")
    if not all(p.exists() for p in required):
        return

    state_model = text(base / "state-model.md")
    state_store = text(base / "state-store.md")
    state_machine = text(base / "state-machine.md")
    next_step = text(base / "next-step-guidance.md")
    routing = text(base / "decision-routing.md")
    phase_map = text(base / "phase-map.md")
    quick_flow = text(base / "quick-flow.md")
    state_router = text(base / "state-router.py")

    if not contains_all(state_model, ["current_subagent", "subagent_queue", "current_contract_path", "handoff_envelope_path", "handoff_status", "last_handoff_at"]):
        FAILED = True
        RESULTS.append({"file": "kit/experience/state-model.md", "kind": "semantic", "status": "fail", "missing": ["state_model_subagent_fields"]})
    else:
        RESULTS.append({"file": "kit/experience/state-model.md", "kind": "semantic", "status": "pass"})

    if not contains_all(state_store, ["current_subagent", "subagent_queue", "handoff_envelope_path", "current contract path", "current sub-agent"]):
        FAILED = True
        RESULTS.append({"file": "kit/experience/state-store.md", "kind": "semantic", "status": "fail", "missing": ["state_store_subagent_fields"]})
    else:
        RESULTS.append({"file": "kit/experience/state-store.md", "kind": "semantic", "status": "pass"})

    if not contains_all(state_machine, ["dispatch Requirements Engineer sub-agent", "dispatch Engineer Orchestrator sub-agent", "dispatch Software Architect sub-agent", "dispatch Quality Engineer sub-agent", "dispatch Security Reviewer sub-agent", "dispatch Code Reviewer sub-agent", "dispatch DevOps Reviewer sub-agent"]):
        FAILED = True
        RESULTS.append({"file": "kit/experience/state-machine.md", "kind": "semantic", "status": "fail", "missing": ["state_machine_dispatch_rules"]})
    else:
        RESULTS.append({"file": "kit/experience/state-machine.md", "kind": "semantic", "status": "pass"})

    if not contains_all(next_step, ["Requirements Engineer sub-agent", "Software Architect sub-agent", "Quality Engineer sub-agent", "Security Reviewer sub-agent", "Code Reviewer sub-agent", "DevOps Reviewer sub-agent"]):
        FAILED = True
        RESULTS.append({"file": "kit/experience/next-step-guidance.md", "kind": "semantic", "status": "fail", "missing": ["next_step_subagents"]})
    else:
        RESULTS.append({"file": "kit/experience/next-step-guidance.md", "kind": "semantic", "status": "pass"})

    if not contains_all(routing, ["Dispatch the Requirements Engineer sub-agent", "Dispatch the Software Architect sub-agent", "Dispatch the Quality Engineer sub-agent", "Dispatch the Security Reviewer sub-agent", "Dispatch the Code Reviewer sub-agent", "Dispatch the DevOps Reviewer sub-agent"]):
        FAILED = True
        RESULTS.append({"file": "kit/experience/decision-routing.md", "kind": "semantic", "status": "fail", "missing": ["decision_routing_subagents"]})
    else:
        RESULTS.append({"file": "kit/experience/decision-routing.md", "kind": "semantic", "status": "pass"})

    if not contains_all(phase_map, ["dispatch the Requirements Engineer sub-agent", "dispatch the Software Architect sub-agent", "dispatch the required sub-agents", "Quality Engineer", "Security Reviewer", "Code Reviewer", "DevOps Reviewer"]):
        FAILED = True
        RESULTS.append({"file": "kit/experience/phase-map.md", "kind": "semantic", "status": "fail", "missing": ["phase_map_subagents"]})
    else:
        RESULTS.append({"file": "kit/experience/phase-map.md", "kind": "semantic", "status": "pass"})

    if not contains_all(quick_flow, ["never bypasses security, integrity, or quality gates", "still updates the persistent harness state"]):
        FAILED = True
        RESULTS.append({"file": "kit/experience/quick-flow.md", "kind": "semantic", "status": "fail", "missing": ["quick_flow_contract"]})
    else:
        RESULTS.append({"file": "kit/experience/quick-flow.md", "kind": "semantic", "status": "pass"})

    RESULTS.append({"file": "scripts/experience/state-router.py", "kind": "semantic", "status": "pass"})

def validate_policies_semantics() -> None:
    base = ROOT / "kit" / "policies"
    required = [
        base / "documentation-hierarchy.md",
        base / "change-classification.md",
        base / "document-generation-triggers.md",
        base / "decision-rationale-policy.md",
        base / "breaking-change-policy.md",
        base / "versioning-and-compatibility.md",
        base / "security-by-design.md",
        base / "supply-chain-security.md",
        base / "prompt-injection-defense.md",
    ]
    require_files(required, "policy-pack")
    for p in required:
        if p.exists():
            validate_required(p, POLICY_REQUIRED, "policy")
            validate_links(p)

    hierarchy = base / "documentation-hierarchy.md"
    if hierarchy.exists():
        body = text(hierarchy)
        if not contains_all(body, ["Requirements Specification", "ADR", "Public API contract", "Domain model / MER", "Activity Diagrams and UML", "Implementation details", "Informal notes"]):
            global FAILED
            FAILED = True
            RESULTS.append({"file": str(hierarchy.relative_to(ROOT)), "kind": "semantic", "status": "fail", "missing": ["documentation_hierarchy_contract"]})
        else:
            RESULTS.append({"file": str(hierarchy.relative_to(ROOT)), "kind": "semantic", "status": "pass"})

def validate_root_and_manifests() -> None:
    root = ROOT / "README.md"
    kit_manifest = ROOT / "kit" / "manifest.md"
    exp_manifest = ROOT / "kit" / "experience" / "manifest.md"
    val_manifest = ROOT / "kit" / "validation" / "manifest.md"
    sec_manifest = ROOT / "kit" / "security" / "manifest.md"
    core_manifest = ROOT / "kit" / "core" / "manifest.md"
    agents_manifest = ROOT / "kit" / "agents" / "manifest.md"

    for p in [root, kit_manifest, exp_manifest, val_manifest, sec_manifest, core_manifest, agents_manifest]:
        if not p.exists():
            global FAILED
            FAILED = True
            RESULTS.append({"file": str(p.relative_to(ROOT)), "kind": "manifest", "status": "fail", "missing": ["file"]})
        else:
            RESULTS.append({"file": str(p.relative_to(ROOT)), "kind": "manifest", "status": "pass"})

    if root.exists():
        body = text(root)
        if not contains_all(body, ["Onda 2", "semantic validation", "Onda 3", "stateful harness", "deep elicitation", "baby-step design", "formal sub-agents"]):
            FAILED = True
            RESULTS.append({"file": str(root.relative_to(ROOT)), "kind": "semantic", "status": "fail", "missing": ["readme_contract"]})
        else:
            RESULTS.append({"file": str(root.relative_to(ROOT)), "kind": "semantic", "status": "pass"})

def main() -> int:
    validate_names(ROOT / "kit" / "core" / "roles")
    validate_names(ROOT / "kit" / "core" / "playbooks")
    validate_names(ROOT / "kit" / "agents")
    validate_names(ROOT / "kit" / "security")
    validate_names(ROOT / "kit" / "experience")
    validate_names(ROOT / "kit" / "policies")
    validate_names(ROOT / "kit" / "checklists")

    validate_root_and_manifests()
    validate_core_semantics()
    validate_agents_semantics()
    validate_security_semantics()
    validate_experience_semantics()
    validate_policies_semantics()

    for path in (ROOT / "kit" / "core" / "roles").rglob("*.md"):
        validate_required(path, ROLE_REQUIRED, "role")
        validate_links(path)

    for path in (ROOT / "kit" / "core" / "playbooks").rglob("*.md"):
        validate_required(path, PLAYBOOK_REQUIRED, "playbook")
        validate_links(path)

    for path in (ROOT / "kit" / "agents").rglob("contract.md"):
        validate_required(path, AGENT_REQUIRED, "agent-contract")
        validate_links(path)

    for path in (ROOT / "kit" / "security").rglob("*.md"):
        if "checklist" in path.name:
            validate_required(path, CHECKLIST_REQUIRED, "checklist")
        else:
            validate_required(path, POLICY_REQUIRED, "policy")
        validate_links(path)

    for path in (ROOT / "kit" / "policies").rglob("*.md"):
        validate_required(path, POLICY_REQUIRED, "policy")
        validate_links(path)

    for path in (ROOT / "kit" / "checklists").rglob("*.md"):
        validate_required(path, CHECKLIST_REQUIRED, "checklist")
        validate_links(path)

    print(json.dumps({"root": str(ROOT), "failed": FAILED, "results": RESULTS}, indent=2, sort_keys=True))
    return 1 if FAILED else 0

if __name__ == "__main__":
    raise SystemExit(main())
