# Human-in-the-Loop Policy

## Purpose
Define when human intervention is mandatory in an AI-assisted governance system.

## Mandatory Triggers
Human approval is required when any of the following apply:
- irreversible decisions
- high systemic impact
- security-sensitive changes
- budget exceeded
- validation ambiguity
- policy exceptions
- high drift

## Enforcement
- The system must block execution if human approval is required.
- No agent may self-approve.
- All approvals must be traceable.

## Telemetry
Must emit:
- `intervention_triggered`
- `intervention_reason`
- `intervention_role`
- `intervention_outcome`
