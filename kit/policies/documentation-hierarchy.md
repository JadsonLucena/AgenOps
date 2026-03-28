Canonical artifact lifecycle and promotion rules live in `governance/` and the meta-model.

# Documentation Hierarchy

## Scope

Define the order of authority when documents disagree.

## Requirements

When documents disagree, use this order of authority:
1. Requirements Specification
2. ADR
3. Public API contract
4. Domain model / MER
5. Activity Diagrams and UML
6. Implementation details
7. Informal notes
Only the highest-authority document should define a durable decision.

## Exceptions

- Deviations require explicit rationale and approval when they affect shared behavior, security, or compatibility.

## Evidence

- review notes
- validation output
- linked change record
