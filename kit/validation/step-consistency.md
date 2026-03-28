# Step Consistency

## Purpose
Ensure each workflow step is predictable, valid, and well-defined.

## Step Contract

Each step must define:

### Inputs
- required data
- required artifacts
- required approvals

### Outputs
- produced artifacts
- state changes
- decisions (if any)

### Exit Criteria
- validation passed
- required reviews completed
- evidence bundle present (if applicable)

### Allowed Next Steps
- explicitly defined next phases

### Forbidden Transitions
- skipping mandatory steps
- bypassing validation or review

## Example

Step: "review"

Inputs:
- completed implementation
- test results

Outputs:
- review report
- approval/rejection

Exit Criteria:
- QA review completed
- security review completed

Next:
- approve
- rework

## Validation Rules

- No step executes without required inputs
- No step completes without exit criteria
- No transition allowed outside defined flow

## Exploration Requirements

Steps may require structured exploration:

- artifact generation → SHOULD use SoT when the artifact is complex
- high-impact decision → SHOULD use ToT when the decision has multiple viable branches

A step is INVALID if:
- required exploration protocol is explicitly mandated by policy and skipped

## Enforcement

Workflow is INVALID if:
- step executed without inputs
- step skipped validation
- undefined transition detected

## Integration

This must integrate with:
- state-machine
- runtime engine
- validator
