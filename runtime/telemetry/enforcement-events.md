# Enforcement Telemetry Events

## Event meanings

### enforcement_started
Cross-layer enforcement has begun.

### enforcement_passed
All required checks passed.

### enforcement_warned
A non-blocking issue was found and recorded.

### enforcement_blocked
A blocking issue was found and execution stopped.

### enforcement_escalated
The issue was routed to a human approver or higher-level control.

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
- affected_layers

## Notes
These events must be emitted in addition to the existing runtime telemetry events.
