# Progressive Discovery

## Purpose
Define progressive discovery as a first-class operating principle for AgenOps.

Progressive discovery means that meaningful work is not finalized upfront. Instead, it is discovered, expanded, validated, and refined through governed iterations.

## Levels of discovery

### 1. Structural discovery
Used when the artifact itself is not yet shaped.
Typical mechanism: Skeleton of Thought.

### 2. Decisional discovery
Used when multiple viable choices exist.
Typical mechanism: Tree of Thought.

### 3. Operational discovery
Used when execution must proceed with inspection and verification at each step.
Typical mechanism: ReAct.

### 4. Organizational discovery
Used when patterns from runtime behavior are turned into improvements.
Typical mechanism: incidents, retrospectives, and pattern evolution.

## When to apply
Use progressive discovery when:
- the problem is ambiguous
- the artifact is complex
- the decision has high impact
- the execution path is not fully known
- the system can learn from iteration

## When not to apply
Do not force progressive discovery when:
- the answer is deterministic
- the task is trivial
- a policy already defines the outcome
- validation alone is sufficient

## Operating rules
- start small
- expand only what is needed
- validate before advancing
- do not finalize before evidence exists
- do not confuse exploration with approval

## Anti-patterns
- big upfront finalization
- shallow exploration
- skipping review because the answer feels obvious
- producing final artifacts without iteration history
- hiding discovery in implicit agent reasoning

## Integration points
- SoT
- ToT
- ReAct
- step consistency
- system consistency
- learning loop
- runtime telemetry

## Governance rule
If a task requires discovery, the runtime and validator must be able to observe that discovery happened in a controlled and traceable way.
