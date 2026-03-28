# Unified Enforcement

## Purpose
Define a single enforcement model that checks all governance layers consistently.

Unified enforcement means that no layer is validated in isolation when its correctness depends on other layers.

## Enforcement scope
This model covers:
- system consistency
- step consistency
- human-in-the-loop
- ReAct
- LLM as a Judge
- progressive discovery
- decision framework
- security boundaries
- telemetry coverage
- economics and budget
- GitOps discipline
- learning loop

## Core rule
If a change affects more than one governance layer, the validator must check the cross-layer contract, not just the local file.

## Enforcement principles

### 1. No isolated approval
A file may be valid locally and still invalid globally.

### 2. No silent bypass
Any missing evidence, missing trace, or missing gate must fail enforcement.

### 3. No layer drift
State, docs, runtime, and policies must tell the same story.

### 4. No untracked autonomy
Agent actions must remain within declared permissions and stop conditions.

### 5. No unbounded learning
Learning may suggest changes, but only governed updates may modify contracts or rules.

## Enforcement categories

### Structural
- file presence
- schema validity
- required sections
- required cross-links

### Behavioral
- step execution shape
- ReAct loop verification
- human escalation behavior
- judge advisory behavior

### Security
- trust boundaries
- permission envelopes
- prompt injection defense
- sensitive action gating

### Economic
- budget thresholds
- drift-based review triggers
- cost controls

### Release
- commit discipline
- semantic versioning
- artifact promotion rules
- approval evidence bundles

### Learning
- incident capture
- retrospective capture
- pattern evolution updates

## Enforcement workflow
1. Inspect current task state
2. Determine the applicable step and policies
3. Validate local artifact(s)
4. Validate cross-layer dependencies
5. Check telemetry and evidence
6. Block on any unresolved violation
7. Emit an enforcement decision event

## Output states
- `pass`
- `warn`
- `block`

## Block conditions
Block when any of the following are true:
- a required layer is missing
- a policy is contradicted
- a high-impact decision lacks a decision record
- an approved artifact lacks evidence
- a runtime action lacks telemetry
- an agent exceeds permissions
- a budget threshold is breached
- a required discovery protocol is skipped

## Integration points
- validator_v3
- runtime engine
- telemetry schema
- step consistency
- system consistency
- human-in-the-loop policy
- progressive discovery
