# Project Governance

This repository consumes `tools/engineering-kit` as a Git submodule.

## Mandatory rules

- Follow the requirement package before implementation.
- Use the Engineer Orchestrator flow: Plan -> Document -> Test -> Prep-Refactor -> Implement -> Refactor.
- Keep decision records as concise rationales, not raw internal reasoning.
- Generate only the documents triggered by the change.
- Keep tests atomic, deterministic, and risk-based.
- Do not introduce provider-specific assumptions in the repository root.
- Keep local overrides in the consuming repository, not in the submodule.

## Local configuration

The repository must define:
- `project-config.yaml`
- a root `AGENTS.md`
- any project-specific conventions that override the generic kit

## Priority order

1. Local repository policy
2. Submodule policy
3. Generic defaults

When a local repository policy conflicts with the submodule, the local policy wins as long as it does not violate security or compliance constraints.
