# Unified Enforcement Validation

## Purpose
Describe the checks required before any approval, promotion, or release.

## Required checks

### 1. Presence
- required files exist
- required directories exist
- required schemas exist

### 2. Consistency
- state matches artifacts
- decisions match trade-offs
- policies match runtime behavior
- telemetry matches execution
- learning updates match observed incidents

### 3. Permission
- agent actions respect declared permissions
- trust boundaries are not crossed without approval

### 4. Evidence
- high-impact changes have decision records
- approvals include evidence bundles
- judge output is advisory only

### 5. Discovery
- complex artifacts use SoT
- hard decisions use ToT
- operational steps under ReAct show observe/reason/act/verify

### 6. Economics
- budget thresholds are known
- overruns trigger escalation
- cost drift is visible

### 7. GitOps
- commits are conventional
- versions reflect impact
- releases are tagged and traceable

## Failure policy
Any unmet required check results in a block, not a warning, when the change affects:
- production
- security
- shared platform behavior
- canonical state
- release readiness

## Integration
This file should be used by:
- `validator_v3.py`
- CI checks
- release gates
