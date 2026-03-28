# Conventional Commits

Format:

type(scope): description

## Types

- feat: new feature
- fix: bug fix
- docs: documentation
- refactor: code change without behavior change
- test: tests
- chore: maintenance
- perf: performance improvement
- ci: CI/CD changes
- build: build system
- revert: revert change

## Examples

feat(core): add validation workflow
fix(state): correct schema validation
docs(decision): add tradeoff matrix

## Breaking change

Use:

feat!: change state schema

or

BREAKING CHANGE: description

## Rule

Every commit must:
- be atomic
- be traceable
- map to a decision or artifact
