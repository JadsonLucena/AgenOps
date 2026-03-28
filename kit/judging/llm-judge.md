# LLM as a Judge

## Purpose
Provide a standardized, rubric-based evaluation layer for artifacts, decisions, and outputs.

This layer is **advisory**, not authoritative.

## Principles
- deterministic validation always has priority
- judge outputs must be explainable
- scoring must be consistent
- no auto-approval from judge

## When to use
- evaluating quality of artifacts
- comparing alternative solutions
- triaging outputs before human review

## Output format
- score (0–100)
- dimension scores
- strengths
- weaknesses
- recommendation (approve / revise / reject)
