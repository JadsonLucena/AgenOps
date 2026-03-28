# Agents Manifest

## Scope

This module defines formal sub-agents for task execution.

## Agents

- orchestrator -> `kit/agents/orchestrator/contract.md`
- requirements-engineer -> `kit/agents/requirements/contract.md`
- software-architect -> `kit/agents/architecture/contract.md`
- quality-engineer -> `kit/agents/qa/contract.md`
- security-reviewer -> `kit/agents/security/contract.md`
- code-reviewer -> `kit/agents/review/contract.md`
- devops-reviewer -> `kit/agents/devops/contract.md`

## Shared contracts

- `kit/agents/shared/contract-template.md`
- `kit/agents/shared/handoff-envelope.md` — shared handoff envelope
- `kit/agents/shared/dispatch-protocol.md`

## Rule

Exactly one formal contract should exist for each named sub-agent.
Every contract must define mission, inputs, outputs, handoff, stop conditions, state update, and quality rules.
