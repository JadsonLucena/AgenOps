# Artifact Provenance Policy

## Scope

Protect the traceability of build outputs.

## Requirements

Release artefacts must be traceable to source and build steps.

- link outputs to source revision
- preserve build metadata
- retain release notes for published artefacts
- prefer signed releases when the ecosystem supports signing

## Exceptions

- local scratch builds are not release artefacts

## Evidence

- provenance record
- build metadata
- release manifest
