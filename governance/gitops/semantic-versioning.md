# Semantic Versioning (SemVer)

Format:
MAJOR.MINOR.PATCH

## Rules

### MAJOR
- breaking changes
- incompatible contract changes
- schema changes in state or validation

### MINOR
- backward-compatible features
- new workflows
- new templates

### PATCH
- bug fixes
- documentation improvements
- non-breaking optimizations

## Governance rule

Version must reflect impact:

- affects multiple teams → MAJOR or MINOR
- internal improvement → PATCH

## Examples

1.0.0 → initial release
1.1.0 → new validation rule (non-breaking)
2.0.0 → change in state schema
