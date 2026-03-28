# Orchestration Loop

## Purpose
Describe the hardened runtime control flow used by AgenOps.

## Loop phases

### 1. Load
Collect:
- canonical state
- step contract
- active policies
- permission envelope
- telemetry context
- budget context

### 2. Route
Select:
- role
- sub-agent
- permitted action
- next checkpoint

### 3. Execute
Perform exactly one bounded action.

### 4. Checkpoint
Record:
- action result
- state delta
- telemetry
- evidence
- stop reason if any

### 5. Verify
Determine whether the result matches the expected output and exit criteria.

### 6. Decide
Choose one of:
- continue
- pause
- escalate
- block
- merge

## Hard stop conditions
Stop immediately when:
- the action violates policy
- a required artifact is missing
- verification fails
- the budget threshold is exceeded
- the action crosses a trust boundary
- human approval is required
- the next action is undefined

## Required invariants
- one action per loop
- one checkpoint per action
- one verification before continuation
- no canonical write without orchestrator
- no implicit escalation
- no silent recovery after a block

## Suggested telemetry
- `orchestration_started`
- `orchestration_routed`
- `orchestration_checkpointed`
- `orchestration_verified`
- `orchestration_blocked`
- `orchestration_escalated`
- `orchestration_completed`

## Integration notes
This loop must cooperate with:
- ReAct
- unified enforcement
- step consistency
- human-in-the-loop
- progressive discovery
