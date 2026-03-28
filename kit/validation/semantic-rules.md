# Semantic Rules

## Purpose

Define the semantic contracts that the validator must check in addition to structure.

## Core contracts

- The Requirements Engineer sub-agent must run deep brainstorming and elicitation before design work begins.
- The Engineer Orchestrator must use the Requirements Engineer output as the source of truth.
- The Engineer Orchestrator must generate triggered documentation only.
- The Engineer Orchestrator must follow the PDCA flow, split work into baby-step chunks, and preserve decision summaries instead of raw internal reasoning.
- Formal sub-agents must exchange work through the shared handoff envelope.
- The Quality Engineer must enforce the test design rules, including fuzz guidance, integration-double rules, and DRY timing.

## Security contracts

- Supply-chain documents must remain separated from agent-security documents.
- SBOM, dependency integrity, artifact provenance, prompt injection defense, secret handling, tool permissions, and audit evidence must exist as a coherent pack.

## Experience contracts

- The experience layer must have a state model, a state store, a state machine, and routing guidance.
- The harness must be able to derive a deterministic next action from the state.
- The harness must track the current sub-agent and the active handoff envelope.
- The quick flow may shorten deliberation, but it may not bypass security, integrity, or quality gates.

## Validation rule

When a semantic contract is missing, inconsistent, or unlinked, the kit fails validation.
