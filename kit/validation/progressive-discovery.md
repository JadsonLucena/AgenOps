# Progressive Discovery Validation

## Purpose
Ensure discovery-heavy tasks actually use progressive discovery instead of jumping directly to final output.

## Validation checks

### Structural discovery check
If the artifact is complex, it should show:
- outline first
- section expansion
- traceability markers

### Decisional discovery check
If a decision has non-trivial trade-offs, it should show:
- candidate branches
- scoring or comparison
- pruning rationale
- selected branch

### Operational discovery check
If a step is executed under ReAct, it should show:
- observe
- reason
- act
- verify

### Organizational discovery check
If a recurring issue exists, it should show:
- incident
- retrospective
- pattern update
- contract or heuristic change

## Failure conditions
Fail validation when:
- a complex artifact is produced without outline or expansion history
- a high-impact decision is recorded without alternatives
- execution advances without verification
- repeated issues are not captured in learning artifacts

## Enforcement integration
This validation must be wired into:
- validator_v3
- step consistency
- runtime telemetry review
- human-in-the-loop escalation
