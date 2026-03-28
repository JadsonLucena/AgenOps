# Next-Step Guidance

## Goal

Make the next action obvious and deterministic.

## Routing rules

- Missing or conflicting requirements -> Requirements Engineer sub-agent
- Brainstorm not complete -> Requirements Engineer sub-agent
- Spec document design not complete -> Engineer Orchestrator
- Design not yet split into baby steps -> Engineer Orchestrator
- Architectural uncertainty -> Software Architect sub-agent
- Missing tests -> Quality Engineer sub-agent
- Risk in quality gates -> Quality Engineer sub-agent
- Security concerns -> Security Reviewer sub-agent
- Code review concerns -> Code Reviewer sub-agent
- Infra or release concerns -> DevOps Reviewer sub-agent
- Documentation drift -> documentation playbooks
- Context budget warning -> compact and snapshot before the next major step
- Context budget exceeded -> compact immediately
- Small and clear change -> quick flow
- Any blocker -> resolve the blocker first

## Output style

Return one next action, one reason, and one blocker if present.
Do not emit a long plan unless the current phase requires it.
If the harness state exists, prefer it over ad hoc phase guesses.
