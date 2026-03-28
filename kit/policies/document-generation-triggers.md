Canonical artifact lifecycle and promotion rules live in `governance/` and the meta-model.

# Document Generation Triggers

## Scope

Generate documentation only when a change affects the artifact that owns the truth.

## Requirements

Generate documentation only when a change affects the artifact's source of truth.
- API contract changes -> OpenAPI
- domain or requirement changes -> Requirements Specification, BDD, ADR, Activity Diagrams
- persistence changes -> MER
- architectural boundary changes -> UML and ADR
- release decisions -> release notes and final summary

## Exceptions

- Deviations require explicit rationale and approval when they affect shared behavior, security, or compatibility.

## Evidence

- review notes
- validation output
- linked change record
