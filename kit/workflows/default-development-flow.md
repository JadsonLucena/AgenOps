# Default Development Flow

## Purpose

Provide the standard development sequence for non-trivial changes.

## Flow

1. Requirements Engineer runs deep brainstorming and elicitation.
2. Software Architect confirms the technical direction for the first safe design slice.
3. Engineer Orchestrator splits the approved scope into baby steps.
4. Engineer Orchestrator generates the triggered documentation for the current chunk:
   - Requirements Specification
   - BDD scenarios
   - ADR
   - Activity Diagrams
   - MER
   - UML
   - OpenAPI
5. Engineer Orchestrator writes or updates tests first.
6. Engineer Orchestrator prepares the codebase for the current chunk.
7. Engineer Orchestrator implements the smallest correct change for the chunk.
8. Engineer Orchestrator refactors for design quality.
9. Parallel reviewers validate the result:
   - Quality Engineer
   - Security Reviewer
   - Code Reviewer
   - DevOps Reviewer
10. Engineer Orchestrator closes the loop by resolving findings and, if needed, moving to the next chunk.

## Guidance

- Use the experience layer to choose the next action.
- Use the validation layer before merge or release.
- Keep decision summaries concise.
- Keep the current chunk small enough to fit one review cycle.

## Decision trace

Use concise decision summaries:
- what was decided
- why it was decided
- what assumptions were made
- what remains open

Do not store raw internal reasoning as an artifact.
