# Command Map

## Human-facing entrypoints

- `start` -> initialize or inspect the current harness state
- `brainstorm` -> run the deep elicitation flow
- `spec` -> build the spec document design and file path plan
- `design` -> split the change into baby-step design chunks
- `plan` -> requirements and architecture review
- `document` -> triggered documentation flow
- `test` -> test generation rules
- `build` -> implementation workflow
- `verify` -> quality, security, review, and devops gates
- `dispatch` -> hand off work to a formal sub-agent
- `docs` -> documentation playbooks
- `state` -> read or update the persistent harness state
- `compact` -> prune and snapshot the active context
- `status` -> inspect the current context budget
- `close` -> final delivery summary

## Shell helpers

- `scripts/experience/state-init.sh`
- `scripts/experience/state-update.sh`
- `scripts/experience/state-show.sh`
- `scripts/experience/next-step.sh`
- `scripts/experience/spec-design.sh`
- `scripts/experience/print-menu.sh`
- `scripts/experience/context-compact.sh`
- `scripts/experience/context-status.sh`
- `scripts/validation/validate-kit.sh`

## Rule

Prefer one command per intent.
Avoid command chains that hide responsibility.
