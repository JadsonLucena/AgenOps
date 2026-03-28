# ReAct Telemetry Events

## Event types
- `react_observed`
- `react_reasoned`
- `react_action_started`
- `react_action_completed`
- `react_verified`
- `react_blocked`

## Required common fields
- timestamp
- task_id
- step_id
- role
- state_version
- event_type
- severity
- trace_id
- span_id

## Event meanings

### react_observed
A runtime snapshot has been assembled.

### react_reasoned
A bounded decision summary has been produced.

### react_action_started
A single action is about to execute.

### react_action_completed
The action finished.

### react_verified
The runtime confirmed the action produced the expected effect.

### react_blocked
The runtime stopped due to policy, validation, security, budget, or human approval requirements.
