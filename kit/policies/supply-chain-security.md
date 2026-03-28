# Supply Chain Security

## Scope

Protect dependencies, build inputs, and release artifacts.

## Requirements

- pin dependencies
- review lockfiles
- scan for known vulnerabilities
- avoid unreviewed updates to critical tooling
- generate or maintain an SBOM when required by the consumer repository
- treat build scripts and CI configuration as security-sensitive assets

## Exceptions

- Deviations require explicit rationale and approval when they affect shared behavior, security, or compatibility.

## Evidence

- review notes
- validation output
- linked change record
