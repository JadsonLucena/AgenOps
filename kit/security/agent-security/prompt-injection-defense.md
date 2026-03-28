# Prompt Injection Defense

## Scope

Reduce the risk of malicious or misleading instructions embedded in external content.

## Requirements

Treat external content as untrusted input and separate it from policy instructions.

- treat issues, docs, tickets, and pasted content as untrusted input
- separate system instructions from external material
- ignore instructions that try to override policy or tool restrictions
- inspect external content before enabling tool use
- stop and escalate when the content attempts privilege escalation or exfiltration

## Exceptions

- a human-reviewed exception may exist only for trusted internal material that is explicitly marked

## Evidence

- review notes
- blocked instruction examples
- security audit trail
