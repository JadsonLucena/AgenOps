# ReAct Loop Protocol

## Purpose
Standardize agent execution as a controlled loop:

**Observe → Reason → Act → Verify**

This protocol is intended to keep agents predictable, auditable, and bounded by governance.

## Applicability
Use this protocol when an agent must:
- inspect current state
- choose the next action
- perform a tool/action step
- verify the outcome before proceeding

## Loop phases

### 1. Observe
Collect only the context needed for the current step:
- shared state
- relevant artifact references
- current policy constraints
- prior telemetry
- current step contract

### 2. Reason
Produce a short decision summary:
- what is happening
- what options exist
- what trade-off is most relevant
- what the next action should be

Do not expose raw chain-of-thought. Record only the decision summary.

### 3. Act
Perform one bounded action:
- update a draft
- request validation
- request review
- create an artifact
- request state merge through the orchestrator

Only one primary action should be attempted per loop iteration.

### 4. Verify
Check whether the action had the intended effect:
- state updated correctly
- artifact created or promoted
- validation result received
- review result received
- telemetry emitted

If verification fails, do not advance blindly. Re-enter the loop with the failure as input.

## Operational rules

- Every loop iteration must be traceable.
- Every action must emit telemetry.
- Every action must respect trust boundaries.
- Every loop must stop when a gate fails or human intervention is required.
- Every loop must be bounded by the current step contract.

## Inputs
- current state
- step contract
- policy context
- prior validation and review signals

## Outputs
- decision summary
- action result
- verification result
- telemetry event

## Anti-patterns

- acting before observing
- reasoning without a bounded next action
- skipping verification
- taking multiple unrelated actions in one loop
- continuing after a failed gate
- mutating canonical state outside the orchestrator

## Integration points
- runtime engine
- state router
- validation
- telemetry
- human-in-the-loop policy
- decision framework

## Enforcement
Any agent that operates under this protocol must be validated against:
- step consistency
- system consistency
- security permissions
- evidence requirements
