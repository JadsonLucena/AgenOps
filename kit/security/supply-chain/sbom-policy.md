# SBOM Policy

## Scope

Protect the release from undocumented dependencies.

## Requirements

Every releasable package should have a dependency inventory.

- identify top-level dependencies
- record versions
- record license metadata when available
- keep the inventory synchronized with releases

## Exceptions

- temporary local experiments do not need release-grade SBOM output

## Evidence

- SBOM file
- release tag
- dependency scan report
