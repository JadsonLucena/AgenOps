# Command Policy

## Scope

Treat external commands as operationally sensitive and constrain them by default.

## Requirements

Treat external commands as operationally sensitive.
- Allow only the commands required by the task.
- Prompt for confirmation when a command can alter state outside the workspace.
- Forbid destructive commands unless the task explicitly requires them and the change is controlled.
- Prefer small, auditable command sequences.

## Exceptions

- Deviations require explicit rationale and approval when they affect shared behavior, security, or compatibility.

## Evidence

- review notes
- validation output
- linked change record
