# Decision Policy

## Purpose
Ensure decisions are consistent, auditable, and aligned with the governance system.

## Rules

### 1. One decision, one record
Every meaningful decision gets a record.

### 2. No implicit decisions
If a choice changes architecture, flow, policy, or production behavior, it must be documented.

### 3. Deterministic where possible
If validation or policy can decide the matter, do not escalate to subjective debate.

### 4. Evidence first
Decisions must cite:
- requirements
- architecture context
- telemetry
- incidents
- reviews
- validation results

### 5. Reversibility matters
Irreversible or expensive-to-reverse decisions require stronger review.

### 6. Systemic impact matters
A decision affecting multiple modules or teams requires broader review.

### 7. Use the same language
All decision records should use the same fields and rating scale.

### 8. Supersession rule
A new decision does not rewrite history. It supersedes an old decision and links to it.

### 9. Human approval rule
High-risk, cross-team, security-sensitive, or production-impacting decisions require human approval.

### 10. Learning rule
Repeated decision mistakes become pattern updates, not just lessons learned.
