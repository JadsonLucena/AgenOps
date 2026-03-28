# Pattern Evolution

This document defines how the system evolves based on feedback.

## Sources of learning
- incidents
- retrospectives
- telemetry metrics
- review findings

## Evolution targets

### 1. Contracts
- refine role responsibilities
- tighten handoff schemas
- remove ambiguity

### 2. Validation
- add missing rules
- convert repeated failures into deterministic checks

### 3. Policies
- formalize recurring exceptions
- remove obsolete constraints

### 4. Templates
- improve clarity
- reduce friction
- enforce completeness

### 5. Agent heuristics
- adjust prompting strategies
- refine decision boundaries
- reduce unnecessary branching

## Evolution loop (OODA)

1. Observe
   - telemetry
   - incidents
   - reviews

2. Orient
   - identify patterns
   - classify failures

3. Decide
   - what to change (contract, validation, policy, heuristic)

4. Act
   - update kit
   - version change
   - communicate impact

## Rule

If a problem happens more than once:
→ it must become a rule, validation, or contract update
