# Orchestration Telemetry Events

## Event types
- `orchestration_started`
- `orchestration_routed`
- `orchestration_checkpointed`
- `orchestration_verified`
- `orchestration_blocked`
- `orchestration_escalated`
- `orchestration_completed`

## Required fields
- timestamp
- task_id
- step_id
- role
- state_version
- event_type
- severity
- trace_id
- span_id
- reason
- checkpoint_id

## Semantics

### orchestration_started
A runtime orchestration session begins.

### orchestration_routed
A permitted role/action pair has been selected.

### orchestration_checkpointed
A bounded action has been recorded.

### orchestration_verified
The action outcome has been verified.

### orchestration_blocked
Execution stopped due to policy, validation, budget, or trust boundary issues.

### orchestration_escalated
Execution was routed to human control or a higher-level governance gate.

### orchestration_completed
The orchestration loop ended cleanly.
