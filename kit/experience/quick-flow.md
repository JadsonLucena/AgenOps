# Quick Flow

## Use when

Use this flow for small, low-risk, well-understood changes.

## Steps

1. Classify the change.
2. Run a short brainstorm only if the problem is not already clear.
3. Create a compact spec document design if the change touches files, contracts, or multiple artifacts.
4. Check whether a documentation trigger exists.
5. Write or update the minimal failing test.
6. Implement the smallest safe change.
7. Refactor only if design quality improves.
8. Run the required validations.
9. Compact the context if the budget is tight.
10. Close with a concise summary.

## Guardrail

Quick flow never bypasses security, integrity, or quality gates.
It only shortens deliberation when the scope is small.

## State rule

Quick flow still updates the persistent harness state and snapshots the context when needed.
