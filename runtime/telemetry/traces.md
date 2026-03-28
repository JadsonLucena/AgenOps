# Traces

Tracing exists to show how decisions flow through the system in production.

## What to trace

### 1. Planning trace
Capture:
- intake
- requirement shaping
- scope decisions
- assumptions
- open questions

### 2. Decision trace
Capture:
- which agent made the decision
- what input was consumed
- what alternative paths were considered
- why one path was selected
- whether a human approved or overrode it

### 3. Validation trace
Capture:
- which contract was checked
- which validator ran
- which rule failed or passed
- how the state changed after the check

### 4. Artifact promotion trace
Capture:
- source path
- target path
- gate result
- reviewer
- evidence bundle reference
- version increment

## Span model

A trace should usually contain:
- one parent span for the task
- child spans per phase
- nested spans per gate or decision

## Traceability rule

Every important promotion, rejection, merge, or exception must emit a trace event.

## Debugging rule

If something is accepted in docs but rejected in runtime, the trace should show where the divergence started.
