# Dependency Integrity Policy

## Scope

Protect the build from tampered or unexpected dependencies.

## Requirements

Pin dependencies where feasible and verify integrity information.

- pin versions where feasible
- verify checksums or signatures where supported
- fail on integrity mismatches
- review new dependency introductions

## Exceptions

- prototype branches may relax pinning only when the risk is accepted

## Evidence

- lockfile diff
- integrity scan
- approval record
