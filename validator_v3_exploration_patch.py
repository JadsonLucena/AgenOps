from pathlib import Path
import json

def validate_exploration_protocols(root: Path, findings: list):
    required = [
        "kit/playbooks/skeleton-of-thought.md",
        "governance/decision/tot-guidance.md",
        "kit/core/protocols/exploration-protocol.md",
    ]
    for rel in required:
        if not (root / rel).exists():
            findings.append(("error", "EXPLORATION_MISSING_FILE", f"Missing required file: {rel}"))

    def read(rel):
        p = root / rel
        return p.read_text(encoding="utf-8").lower() if p.exists() else ""

    sot = read("kit/playbooks/skeleton-of-thought.md")
    tot = read("governance/decision/tot-guidance.md")
    proto = read("kit/core/protocols/exploration-protocol.md")

    for term in ["outline", "expand", "validate"]:
        if term not in sot:
            findings.append(("error", "SOT_INCOMPLETE", f"SoT file missing term: {term}"))

    for term in ["branches", "score", "prune", "decision record"]:
        if term not in tot:
            findings.append(("error", "TOT_INCOMPLETE", f"ToT file missing term: {term}"))

    for term in ["sot", "tot", "complementary", "not interchangeable"]:
        if term not in proto:
            findings.append(("error", "EXPLORATION_PROTOCOL_INCOMPLETE", f"Exploration protocol missing term: {term}"))

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
                    findings.append(("error", "EXPLORATION_TELEMETRY_MISSING", f"Missing telemetry event: {e}"))
        except Exception as exc:
            findings.append(("error", "EXPLORATION_SCHEMA_PARSE", f"Could not parse telemetry schema: {exc}"))
