# Core Manifest

## Scope

The core module defines the standard delivery flow, role responsibilities, and operational playbooks.

## Entries

- roles
- workflows
- playbooks
- brainstorming and elicitation playbook
- spec document design playbook
- baby-step design playbook

## Boundary

The core module does not define runtime state, validation engines, security policy packs, formal sub-agent contracts, or user experience helpers.
Those concerns live in `runtime/`, `validation/`, `security/`, `agents/`, and `experience/`.
