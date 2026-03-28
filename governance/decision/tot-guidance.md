# Tree of Thought (ToT) Guidance

## Purpose
Use branching exploration when a decision has multiple viable paths and the trade-offs are non-trivial.

ToT is best for:
- architecture choices
- policy exceptions
- release strategy decisions
- security trade-offs
- cost vs value trade-offs
- platform evolution choices

## Core idea
Explore multiple candidate paths, score them, prune weak branches, and commit only the best-supported option.

## ToT workflow

### 1. Define the decision
State the problem and the decision boundary.

### 2. Generate branches
Create a small number of credible options.

### 3. Score branches
Evaluate each option using the decision framework:
- cost
- benefit
- reversibility
- systemic impact
- risk
- maintainability
- auditability

### 4. Prune
Remove options that are clearly inferior or too risky.

### 5. Compare survivors
Summarize the strongest remaining options and the decisive differences.

### 6. Commit
Record the selected option in a decision record with rationale and evidence.

## Operating rules
- Keep the branch count small and meaningful.
- Do not explore infinite alternatives.
- Do not confuse exploration with approval.
- Do not commit a decision without a record.
- Do not let the exploration output replace the decision template.

## ToT output contract
A ToT run should produce:
- decision statement
- candidate branches
- scoring table
- pruning rationale
- chosen branch
- follow-up actions

## Anti-patterns
- too many branches
- scoring without criteria
- pruning without justification
- using ToT for trivial decisions
- outputting raw reasoning instead of decision summaries

## Integration points
- decision framework
- human-in-the-loop policy
- validation
- security review
- economics
- telemetry

## Suggested telemetry
- `tot_branch_created`
- `tot_branch_scored`
- `tot_branch_pruned`
- `tot_branch_selected`
- `tot_decision_recorded`
