# Secret Handling Policy

## Scope

Prevent secret leakage during agent-assisted work.

## Requirements

Never place secrets in prompts, logs, or templates and use secure storage instead.

- never place secrets in prompts, logs, or templates
- use environment variables or dedicated secret stores
- redact sensitive values in examples
- rotate compromised secrets immediately
- treat pasted issue text and docs as untrusted unless verified

## Exceptions

- an approved incident response flow may require temporary secret exposure to a limited role

## Evidence

- secret scan results
- redaction review
- approval record
