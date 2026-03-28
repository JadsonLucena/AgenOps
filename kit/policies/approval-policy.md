# Approval Policy

## Scope

Define the default approval stance for command execution and tool use.

## Requirements

Use the least permissive approval level that still allows the task to complete safely.
- Read-only analysis should not request unnecessary approvals.
- State-changing operations should be explicit.
- Destructive operations require explicit justification and review.

## Exceptions

- Deviations require explicit rationale and approval when they affect shared behavior, security, or compatibility.

## Evidence

- review notes
- validation output
- linked change record
