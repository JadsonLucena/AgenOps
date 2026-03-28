# Cost Model

## Purpose
Make the cost of agent-driven work visible enough to govern.

## Cost drivers

### 1. Compute
- model inference
- tool execution
- validation runs
- generation loops
- retries

### 2. Context size
- prompt length
- retrieval overhead
- repeated summarization
- artifact fan-out

### 3. Workflow depth
- number of phases
- number of approvals
- number of review loops
- number of handoffs

### 4. Human time
- review time
- clarification cycles
- incident response
- exception handling

### 5. Storage and retention
- planning artifacts
- telemetry
- logs
- snapshots
- archived evidence bundles

## Economic unit definitions

Use a unit that reflects the business object being optimized.

Examples:
- cost per task
- cost per approval
- cost per artifact promoted
- cost per successful release
- cost per validated change
- cost per customer-facing workflow

## Cost-to-serve categories

### Fixed cost
Always-on platform costs, baseline infrastructure, shared governance overhead.

### Variable cost
Costs that scale with activity, such as agent tokens, retries, or review loops.

### Hidden cost
Costs that are not obvious in a single execution but accumulate across workflows, for example:
- excessive context growth
- repeated approval churn
- unnecessary rework
- duplicated reviews

### Exception cost
Costs introduced by policy exceptions, escalations, and manual intervention.

## Allocation rule
Costs should be assigned to the flow, team, or artifact that caused them where possible.

Shared costs should be allocated transparently using a documented rule, not buried in a generic overhead bucket.

## Guardrail rule
If a workflow or agent repeatedly exceeds expected cost for the same unit of value, the pattern should be reviewed and either optimized or restricted.

## FinOps alignment
This model supports allocation, budgeting, reporting, and unit economics as core operating capabilities. It also follows the principle that business value should drive technology decisions and that teams should make conscious trade-offs among cost, quality, and speed. citeturn743117search8turn743117search10turn743117search16turn743117search2
