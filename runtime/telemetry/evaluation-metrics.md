# Evaluation Metrics

These metrics measure whether the system behaves correctly in practice.

## Core metrics

### Contract compliance rate
Percentage of executed steps that followed the declared contract.

Formula:
`compliant_steps / total_steps`

Target:
- high and stable
- near 1.0 for mature flows

### Planning-to-execution drift
Measures how far execution diverged from the approved plan.

Possible signals:
- skipped required artifact
- extra unplanned review
- missing evidence bundle
- changed sequence of phases
- unapproved scope expansion

Target:
- as low as possible

### Gate pass fidelity
How often gates pass for the right reason and fail for the right reason.

### Review latency
Time from review request to review completion.

### Rework rate
How often an artifact must be revised after review.

### Exception rate
How often policy exceptions are required.

### Trace completeness
Whether each critical action has an associated structured event.

## Suggested alerts

- Contract compliance drops below threshold
- Drift increases across multiple tasks
- Security review latency exceeds target
- Evidence bundle missing at approval time
- State merge without trace event
- Approved artifact without archived provenance

## Operational interpretation

A healthy system is not only one that validates correctly. It is one whose real executions are consistent with the contracts, with drift explained, measured, and reduced over time.
