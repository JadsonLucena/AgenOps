# Unified Enforcement Runtime Loop

## Purpose
Describe how the runtime should apply enforcement in execution.

## Loop
1. Load task state and current step contract.
2. Determine required governance checks.
3. Validate candidate action or artifact.
4. Check cross-layer dependencies.
5. Verify evidence and telemetry.
6. Decide `pass`, `warn`, or `block`.
7. Emit enforcement telemetry.
8. If blocked, stop and route to human intervention or remediation.

## Runtime rules
- validation must be policy-aware
- validation must be cross-layer
- runtime must not continue after a block
- runtime must not auto-escalate into an unapproved action
- runtime must preserve traceability for every blocked or passed decision

## Suggested telemetry events
- `enforcement_started`
- `enforcement_passed`
- `enforcement_warned`
- `enforcement_blocked`
- `enforcement_escalated`

## Integration points
- ReAct loop
- human-in-the-loop policy
- step consistency
- system consistency
- progressive discovery
- judge output
