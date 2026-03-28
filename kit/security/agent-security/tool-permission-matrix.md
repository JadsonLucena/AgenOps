# Tool Permission Matrix

## Scope

Define which agent role may use which tool category.

## Requirements

Limit tool access by role and approval level.

- read-only roles cannot write or execute destructive operations
- write roles can only modify their scoped workspace
- privileged tools require explicit approval
- sensitive commands should be prompt-gated by default

## Exceptions

- temporary escalation must be recorded and time-bounded

## Evidence

- approved matrix
- role-to-tool mapping
- exception log
