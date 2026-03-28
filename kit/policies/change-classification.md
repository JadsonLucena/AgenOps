# Change Classification Policy

## Scope

Classify changes before execution so the correct workflow and documentation trigger can be selected.

## Requirements

Classify each change before execution:
- documentation-only
- bugfix
- refactor
- feature
- contract change
- data model change
- security change
- operational change
- breaking change
The class determines which documents, tests, and reviewers are triggered.

## Exceptions

- Deviations require explicit rationale and approval when they affect shared behavior, security, or compatibility.

## Evidence

- review notes
- validation output
- linked change record
