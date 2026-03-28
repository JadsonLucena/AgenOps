# QA Quality Gate Playbook

## Goal

Validate correctness, determinism, and code health before merge.

## Steps

1. Run the test suite.
2. Run lint.
3. Run static analysis or Sonar-like checks.
4. Confirm the tests are at the right level of the pyramid.
5. Review failure patterns and reliability risks.
6. Confirm the test names, structure, and assertions are readable and isolated.
7. Confirm the repository satisfies the concise test-generation checklist.

## Decision rules

- Prefer risk-based coverage over vanity coverage.
- Keep integration tests production-like.
- Do not use doubles in integration tests by default.
- Request developer preference before using a stub in integration tests.
- Suggest fuzz tests only when the data domain or risk profile justifies them.

## Outputs

- quality gate status
- list of failing checks
- prioritized recommendations
