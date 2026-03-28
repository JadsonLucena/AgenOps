# Discovery Loop

## Purpose
Describe how the runtime should support progressive discovery.

## Loop
1. Observe the current shape of the problem.
2. Determine whether the task is structural, decisional, operational, or organizational.
3. Select the appropriate discovery mode:
   - SoT
   - ToT
   - ReAct
   - Learning loop
4. Expand only one bounded slice.
5. Verify the result.
6. Emit telemetry.
7. Decide whether to continue or stop.

## Runtime rules
- do not treat discovery as free-form reasoning
- do not allow discovery to bypass validation
- do not finalize if evidence is incomplete
- do not skip telemetry for discovery iterations

## Suggested telemetry
- `discovery_mode_selected`
- `discovery_slice_expanded`
- `discovery_slice_validated`
- `discovery_iteration_stopped`
