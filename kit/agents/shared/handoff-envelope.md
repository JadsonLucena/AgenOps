# Handoff Envelope

## Purpose

Provide a stable, machine-readable packet for sub-agent dispatch and return.

## Required fields

- session_id
- task_id
- source_agent
- target_agent
- parent_workflow
- phase
- current_chunk
- task_state_path
- task_state_version
- upstream_contract
- downstream_contract
- inputs
- outputs
- blockers
- assumptions
- artifacts_created
- verification_needed
- state_updates
- status
- updated_at

## Usage

- The source agent prepares the envelope before dispatch.
- The target agent reads the envelope as the execution contract.
- The target agent returns the same envelope with outputs, findings, and updated status.
- The orchestrator persists the envelope in the harness state.

## Example

```yaml
session_id: egk-20260325-001
source_agent: orchestrator
target_agent: requirements-engineer
parent_workflow: default-development-flow
phase: brainstorm
current_chunk: null
upstream_contract: kit/agents/orchestrator/contract.md
downstream_contract: kit/agents/requirements/contract.md
inputs:
  objective: Clarify the request and expose gaps
  context: [requirements, constraints, policies]
outputs:
  brainstorm_brief: ...
  assumptions_log: ...
blockers: []
assumptions: []
artifacts_created: []
verification_needed: requirements_spec
state_updates:
  current_subagent: requirements-engineer
  handoff_status: dispatched
status: dispatched
updated_at: 2026-03-25T00:00:00Z
```

## Rule

A handoff is invalid if the target agent, the phase, or the updated state is missing.
