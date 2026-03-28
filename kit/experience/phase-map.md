# Phase Map

## Phases

### 1. Intake and Brainstorm
Confirm the objective, surface gaps, persist the initial harness state, and dispatch the Requirements Engineer sub-agent when needed.

### 2. Spec Document Design
Turn the elicited request into a small spec blueprint with section order, file paths, downstream artifacts, and a handoff envelope.

### 3. Design in Baby Steps
Break the approved scope into the smallest reviewable design chunks and dispatch the Software Architect sub-agent if a slice is unsafe.

### 4. Generate Documentation
Create only the artifacts triggered by the current chunk:
- Requirements Specification
- BDD
- ADR
- Activity Diagrams
- MER
- UML
- OpenAPI

### 5. Write Failing Tests
Apply the test-generation rules and keep tests atomic.

### 6. Prepare the Codebase
Refactor structure first when it improves the current chunk.

### 7. Implement
Write the smallest correct change using Hexagonal Architecture, DDD, and Clean Architecture.

### 8. Refactor
Improve design without changing behavior.

### 9. Verify
Run Quality Engineer, Security Reviewer, Code Reviewer, and DevOps Reviewer sub-agents.

During verification, dispatch the required sub-agents through the shared handoff envelope.

### 10. Close
Publish the final delivery summary, update durable documentation, compact the context if needed, and persist the final harness state.

## State rule

Each phase transition should update the state store, refresh the context snapshot when the budget is tight, and update any active handoff envelope before the next action is executed.
