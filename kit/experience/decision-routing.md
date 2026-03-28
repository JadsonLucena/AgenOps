# Decision Routing

## Route

Use the current state to choose exactly one primary next action.

## Primary router

1. Resolve blockers first.
2. If context budget is tight, compact and snapshot before anything else.
3. Dispatch the Requirements Engineer sub-agent for gaps and ambiguous intent.
4. Dispatch the Engineer Orchestrator for spec document design and handoff setup.
5. Dispatch the Software Architect sub-agent for the first safe design slice.
6. Split the scope into baby-step design chunks.
7. Generate or update triggered documentation.
8. Dispatch the Quality Engineer sub-agent for tests and quality gates.
9. Dispatch the Security Reviewer sub-agent for security review.
10. Dispatch the Code Reviewer sub-agent for maintainability review.
11. Dispatch the DevOps Reviewer sub-agent for release readiness.
12. Close the change.

## Exception

A release blocker may jump ahead of the default route.
After the blocker is resolved, return to the normal state machine.
