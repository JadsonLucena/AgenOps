# Skill Contract

## Purpose
Define the minimum contract a reusable skill must satisfy.

## Required fields
- skill id
- objective
- inputs
- outputs
- constraints
- evidence
- boundaries
- version

## Contract template
```yaml
skill_id: requirements-elicitation
version: 1.0.0
objective: Convert vague intent into testable requirements
inputs:
  - problem_statement
  - context
  - constraints
outputs:
  - requirements_outline
  - open_questions
  - assumptions
constraints:
  - no hidden chain-of-thought
  - no direct state mutation
evidence:
  - traceable references
  - explicit decision summary
boundaries:
  - trust boundaries respected
  - only approved tools used
```

## Rule
If a skill cannot state its inputs, outputs, constraints, and evidence, it is not yet safe to use as a reusable capability.
