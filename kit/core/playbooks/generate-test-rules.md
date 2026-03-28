# Test Generation Rules

## Core principle

Create tests that validate expected behavior rather than implementation details.

## Standards

- Tests must be atomic, fast, and reliable.
- Follow the testing pyramid.
- Use BDD for acceptance and integration tests.
- Use AAA for unit tests.
- Keep titles, descriptions, and error messages in English.
- Use the appropriate double only when it helps isolate a unit or reduce test fragility.
- Avoid over-mocking.
- Avoid God Tests.
- Avoid unrelated assertions in the same test.
- Avoid complex logic inside tests.
- Keep tests deterministic and CI-friendly.

## Preferences

- Suggest fuzz tests only when relevant.
- Integration tests should not use doubles by default.
- If a stub seems acceptable in an integration test, ask the developer before proceeding.
- Prefer DRY when the same setup repeats three times or more.
- Accept DTOs and builders as legitimate exceptions to the “more than two arguments” guideline.

## Anti-patterns

- flaky tests
- tests that only exist for coverage metrics
- tests coupled to time, order, or environment
- tests that mirror implementation details
- tests that require tests of their own

## Output format

Prefer a concise test plan:
- target level
- scenario
- setup
- assertions
- risk covered
