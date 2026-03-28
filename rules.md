# Meta-Model Rules

## Canonical boundaries
- `governance/` is the canonical home for strategic policy and system-level decisions.
- `kit/` is the canonical home for operational execution contracts and daily workflow guidance.
- `scripts/` contains runnable entrypoints and helpers.
- `runtime/telemetry/` contains observability evidence and metrics.
- `security/` contains threat modeling, trust boundaries, and permissions.
- `learning/` contains feedback loops and evolution artifacts.

## Invariants
1. One canonical writer for state.
2. No approval without evidence.
3. No production-impacting change without security and decision traceability.
4. No release without telemetry and budget awareness.
5. No contract update without versioning discipline.
6. No repeated failure without learning capture.
7. No direct dependency from durable docs to ephemeral planning artifacts.

## Validation rule
A governance instance is valid only if:
- all required layers exist
- invariants are explicit
- forbidden relationships are absent or marked as disallowed
- lifecycle transitions are constrained
- decision, security, observability, economics, gitops, and learning are linked
- strategic governance and operational execution are not conflated

## Use
This is the smallest practical version of a unified system meta-model. It is intentionally not exhaustive; it is designed to be extended safely.
