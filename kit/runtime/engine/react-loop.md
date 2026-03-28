# Runtime Integration for ReAct Loop

## Goal
Make the ReAct protocol executable through the runtime.

The runtime should not treat agent execution as an opaque prompt cycle. It should treat it as a governed loop with checkpoints.

## Runtime behavior

### Input assembly
Before each loop iteration, the runtime should assemble:
- canonical task state
- current step contract
- allowed tools
- active policies
- latest telemetry and review results

### Execution lifecycle
1. observe current context
2. produce decision summary
3. execute one bounded action
4. verify result
5. emit telemetry
6. update local step state
7. decide whether to continue or stop

### Stop conditions
The runtime must stop the loop when:
- the step contract is satisfied
- a validation failure occurs
- a security boundary is crossed
- the budget threshold is exceeded
- human-in-the-loop approval is required
- the next action is undefined

## Runtime guarantees

- The orchestrator remains the only canonical state writer.
- Sub-agents may propose actions but do not directly mutate canonical state.
- Verification is required before advancing to the next step.
- Each loop iteration must be recorded in telemetry.

## Suggested telemetry events
- `react_observed`
- `react_reasoned`
- `react_action_started`
- `react_action_completed`
- `react_verified`
- `react_blocked`

## Suggested runtime hooks
- `before_loop(context)`
- `after_observe(snapshot)`
- `after_reason(summary)`
- `after_act(result)`
- `after_verify(status)`
- `on_block(reason)`

## Integration with state router
The state router should:
- load the current step contract
- determine whether ReAct is allowed for the role
- enforce a single bounded action per iteration
- route to validation or human review when necessary

## Integration with step consistency
The runtime must reject any action that:
- does not match the step inputs
- does not produce the expected outputs
- violates the exit criteria
- attempts an undefined transition

## Integration with system consistency
The runtime must reject any loop iteration that would:
- produce an artifact without traceability
- mutate state without the orchestrator
- bypass validation or review
- skip telemetry emission

## Integration with human-in-the-loop policy
If a loop iteration reaches a high-risk boundary, the runtime must:
- stop
- emit an intervention event
- request the appropriate human approver

## Integration with exploration protocols
Before acting, the runtime may require:
- SoT when producing complex artifacts
- ToT when making high-impact decisions

The runtime should:
- enforce SoT for large artifact generation steps
- enforce ToT for decisions above defined impact thresholds

## Minimal implementation note
A production implementation can be a thin loop wrapper around the existing state router, as long as it preserves:
- one action per iteration
- verification before continuation
- telemetry for every checkpoint
