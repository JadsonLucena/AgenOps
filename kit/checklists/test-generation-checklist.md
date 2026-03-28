# Test Generation Checklist

## Purpose

Confirm that a proposed test is necessary, well-designed, and aligned with the test strategy.

## Items

- [ ] Is this test necessary?
- [ ] Is the test at the correct pyramid level?
- [ ] Does it use the correct structure: BDD for acceptance/integration, AAA for unit?
- [ ] Are names and messages in English?
- [ ] Is the test atomic and deterministic?
- [ ] Are doubles appropriate, especially for integration tests?
- [ ] Is the setup repeated three or more times before extracting helpers?
- [ ] Does it cover the relevant happy path, edge cases, and failure cases?
- [ ] Does it avoid over-mocking and unrelated assertions?
- [ ] Does it follow project lint and style rules?

## Pass condition

All items are checked or have documented exceptions.
