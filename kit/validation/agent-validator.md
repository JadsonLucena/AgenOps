# Agent Validator

## Purpose

Validate that every formal sub-agent has a contract, a stable handoff model, and a clear state update boundary.

## Checks

- each sub-agent contract exists
- each contract contains mission, inputs, outputs, handoff, stop conditions, state update, and quality rules
- the orchestrator contract references the shared handoff envelope
- the requirements contract requires deep brainstorming and elicitation
- the architecture contract requires a safe design slice and ADR inputs
- the quality contract covers lint, test, and gate checks
- the security contract covers supply-chain and agent-security review
- the review contract covers maintainability and design quality
- the devops contract covers deployment readiness and rollback safety
- the shared handoff envelope contains required fields and state updates

## Rule

If a contract omits a required section or a handoff target is unclear, the agent pack fails validation.
