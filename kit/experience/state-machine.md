# State Machine

## Purpose

Define the allowed transitions for the harness state.

## Normal transitions

1. intake -> brainstorm
2. brainstorm -> spec
3. spec -> design
4. design -> document
5. document -> test
6. test -> prepare
7. prepare -> implement
8. implement -> refactor
9. refactor -> verify
10. verify -> close
11. close -> done

## Exception transitions

- any phase with a blocker -> blocker resolution
- any phase with context budget warning -> compact and snapshot
- any phase with context budget exceeded -> compact immediately before the next non-trivial step
- brainstorm with missing requirements -> dispatch Requirements Engineer sub-agent
- spec with unclear file boundaries -> dispatch Engineer Orchestrator sub-agent
- design with architectural uncertainty -> dispatch Software Architect sub-agent
- verify with quality issues -> dispatch Quality Engineer sub-agent
- verify with security issues -> dispatch Security Reviewer sub-agent
- verify with code review issues -> dispatch Code Reviewer sub-agent
- verify with release issues -> dispatch DevOps Reviewer sub-agent

## Guardrail

Exception routing may interrupt the normal path, but it should always create a handoff envelope, persist the current sub-agent, snapshot the current state when needed, and return to the normal state machine after the blocker is resolved.
