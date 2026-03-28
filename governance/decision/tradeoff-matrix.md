# Trade-off Matrix

Use this matrix to compare options consistently across agents.

## Scoring dimensions

Score each dimension from 1 to 5, where 5 is best.

| Dimension | Meaning |
|---|---|
| Cost | Lower effort, lower spend, lower operational burden |
| Benefit | Higher value delivered |
| Reversibility | Easier rollback or replacement |
| Systemic impact | Lower negative blast radius |
| Risk | Lower technical / operational / security risk |
| Time to implement | Faster delivery |
| Maintainability | Simpler future change |
| Auditability | Easier to explain and trace |

## Example matrix

| Option | Cost | Benefit | Reversibility | Systemic impact | Risk | Time | Maintainability | Auditability | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| A | 4 | 3 | 5 | 4 | 4 | 4 | 4 | 5 | Safe but modest |
| B | 2 | 5 | 2 | 2 | 2 | 3 | 3 | 4 | Strong upside, harder rollback |
| C | 3 | 4 | 4 | 3 | 3 | 2 | 4 | 4 | Faster than B, weaker benefit |

## Decision rule

Use a matrix when:
- options are comparable
- trade-offs are non-trivial
- multiple agents may evaluate the same problem

Do not use a matrix as a substitute for judgment when:
- the decision is binary and deterministic
- the policy already determines the answer
- the risk is so high that the decision must be escalated immediately

## Weighted interpretation

Recommended weighting:
- reversibility: high weight for production-impacting changes
- systemic impact: high weight for shared platform decisions
- auditability: high weight for governance and compliance decisions
- cost: high weight when multiple equivalent options exist

## Notes on consistency

All agents should score using the same rubric, otherwise the framework becomes non-comparable.
