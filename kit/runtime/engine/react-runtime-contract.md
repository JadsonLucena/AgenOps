# ReAct Runtime Contract

## Purpose
Define the runtime contract used when a role executes under ReAct.

## Contract fields
- `step_id`
- `role`
- `state_version`
- `inputs`
- `allowed_actions`
- `selected_action`
- `action_result`
- `verification_result`
- `telemetry_event_ids`
- `stop_reason`

## Required runtime invariants
- selected_action must be in allowed_actions
- canonical state may only be mutated by orchestrator
- verification_result must be present before continuation
- stop_reason must be present on any blocked or completed loop

## Suggested state shape
```json
{
  "step_id": "string",
  "role": "string",
  "state_version": 1,
  "inputs": [],
  "allowed_actions": [],
  "selected_action": "string",
  "action_result": {},
  "verification_result": {},
  "telemetry_event_ids": [],
  "stop_reason": "string"
}
```
