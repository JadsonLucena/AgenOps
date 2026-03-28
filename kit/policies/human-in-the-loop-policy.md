# Human-in-the-Loop Policy

## Purpose
Define when human intervention is mandatory in an AI-assisted governance system.

## Mandatory Triggers
Human approval is REQUIRED when:

- irreversible decisions
- high systemic impact
- security-sensitive changes
- budget exceeded
- validation ambiguity
- policy exceptions
- high drift

## Enforcement
- system must block execution if human approval is required
- no agent can self-approve
- all approvals must be traceable

## Telemetry
Must emit:
- intervention_triggered
- intervention_reason
- intervention_role
- intervention_outcome