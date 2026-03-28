# Structured Logging Contract

All runtime logs should be structured and machine-readable.

## Required fields
- timestamp
- level
- system
- run_id
- task_id
- actor
- phase
- event_type
- message

## Recommended fields
- trace_id
- span_id
- state_version
- artifact_id
- contract_id
- gate_status
- metrics
- details

## Rules
- No free-form logs for critical events.
- No silent failures.
- No approval without traceable evidence.
- No merge without state version.
