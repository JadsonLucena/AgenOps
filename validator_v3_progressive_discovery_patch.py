from pathlib import Path
import json

def validate_progressive_discovery(root: Path, findings: list):
    required = [
        "governance/principles/progressive-discovery.md",
        "kit/validation/progressive-discovery.md",
        "kit/runtime/engine/discovery-loop.md",
    ]
    for rel in required:
        if not (root / rel).exists():
            findings.append(("error", "PD_MISSING_FILE", f"Missing required file: {rel}"))

    def read(rel):
        p = root / rel
        return p.read_text(encoding="utf-8").lower() if p.exists() else ""

    principle = read("governance/principles/progressive-discovery.md")
    validation = read("kit/validation/progressive-discovery.md")
    runtime = read("kit/runtime/engine/discovery-loop.md")

    for term in ["structural discovery", "decisional discovery", "operational discovery", "organizational discovery"]:
        if term not in principle:
            findings.append(("error", "PD_PRINCIPLE_INCOMPLETE", f"Missing discovery type: {term}"))

    for term in ["outline first", "candidate branches", "observe", "verify", "incident", "retrospective"]:
        if term not in validation:
            findings.append(("error", "PD_VALIDATION_INCOMPLETE", f"Validation file missing term: {term}"))

    for term in ["soT".lower(), "tot".lower(), "reAct".lower(), "telemetry"]:
        if term not in runtime:
            findings.append(("error", "PD_RUNTIME_INCOMPLETE", f"Runtime file missing term: {term}"))
