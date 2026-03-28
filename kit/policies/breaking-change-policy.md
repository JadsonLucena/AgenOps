Canonical strategic breaking-change governance lives in `governance/gitops/versioning-policy.md`.

# Breaking Change Policy

## Scope

Classify changes that invalidate existing contracts, expectations, or integrations.

## Requirements

A change is breaking when it invalidates an existing contract, expectation, or integration path.
- classify the change as breaking
- document the impact
- update tests
- update contracts
- communicate migration steps
- provide rollback or fallback guidance when possible

## Exceptions

- Deviations require explicit rationale and approval when they affect shared behavior, security, or compatibility.

## Evidence

- review notes
- validation output
- linked change record
