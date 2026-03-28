# Orchestration Contract

## Purpose
Define the runtime contract for the hardened orchestration engine.

## Required fields
- `task_id`
- `step_id`
- `state_version`
- `role`
- `allowed_actions`
- `selected_action`
- `checkpoint_id`
- `verification_status`
- `stop_reason`
- `escalation_target`
- `telemetry_event_ids`

## Validation rules
- `selected_action` must be within `allowed_actions`
- `checkpoint_id` must exist before continuation
- `verification_status` must be recorded
- `stop_reason` must be present on stop
- `escalation_target` must exist when escalation occurs

## Suggested contract shape
```json
{
  "task_id": "string",
  "step_id": "string",
  "state_version": 1,
  "role": "string",
  "allowed_actions": [],
  "selected_action": "string",
  "checkpoint_id": "string",
  "verification_status": "pending|pass|fail",
  "stop_reason": "string",
  "escalation_target": "string",
  "telemetry_event_ids": []
}
```
