# Default Development Flow

## Purpose

Provide the standard development sequence for non-trivial changes using formal sub-agents and standardized handoff envelopes.

## Flow

1. Requirements Engineer sub-agent runs deep brainstorming and elicitation.
2. Engineer Orchestrator turns the elicited request into a spec document design and file path plan.
3. Software Architect sub-agent confirms the technical direction for the first safe design slice.
4. Engineer Orchestrator splits the approved scope into baby steps.
5. Engineer Orchestrator generates the triggered documentation for the current chunk:
   - Requirements Specification
   - BDD scenarios
   - ADR
   - Activity Diagrams
   - MER
   - UML
   - OpenAPI
6. Engineer Orchestrator dispatches the required sub-agents through the shared handoff envelope:
   - Quality Engineer
   - Security Reviewer
   - Code Reviewer
   - DevOps Reviewer
7. Engineer Orchestrator writes or updates tests first.
8. Engineer Orchestrator prepares the codebase for the current chunk.
9. Engineer Orchestrator implements the smallest correct change for the chunk.
10. Engineer Orchestrator refactors for design quality.
11. Engineer Orchestrator consolidates the sub-agent findings and resolves the remaining blockers.
12. Engineer Orchestrator closes the loop or moves to the next chunk.

## Guidance

- Use the experience layer to choose the next action.
- Use the validation layer before merge or release.
- Keep decision summaries concise.
- Keep the current chunk small enough to fit one review cycle.
- Persist the handoff envelope and current sub-agent in the harness state before dispatch.

## Decision trace

Use concise decision summaries:
- what was decided
- why it was decided
- what assumptions were made
- what remains open
- which sub-agent owns the current handoff

Do not store raw internal reasoning as an artifact.
