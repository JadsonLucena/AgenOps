Canonical strategic versioning lives in `governance/gitops/semantic-versioning.md` and `governance/gitops/versioning-policy.md`.

# Versioning and Compatibility Policy

## Scope

Preserve consumer stability through semantic versioning and compatibility discipline.

## Requirements

- Use semantic versioning for the kit itself.
- Preserve backward compatibility when possible.
- Deprecate before removing when consumers depend on the previous behavior.
- Pin submodule versions in consumer repositories.
- Record the compatibility impact of every major decision.

## Exceptions

- Deviations require explicit rationale and approval when they affect shared behavior, security, or compatibility.

## Evidence

- review notes
- validation output
- linked change record
