# Skeleton of Thought (SoT)

## Purpose
Use a structured outline-first method to produce complex artifacts with less drift and better coherence.

SoT is best for:
- specifications
- ADRs
- policies
- architecture notes
- review reports
- large governance documents

## Core idea
First create the skeleton. Then expand each branch in small, reviewable chunks.

## SoT workflow

### 1. Define the target artifact
State clearly:
- what the artifact is
- why it exists
- who will use it
- what decision or action it supports

### 2. Build the skeleton
Create a top-level outline with only the essential sections.

### 3. Expand one section at a time
For each section:
- add only the information needed there
- avoid cross-section duplication
- keep terminology consistent

### 4. Validate the structure
Check:
- completeness
- ordering
- traceability
- alignment with the expected template

### 5. Refine
Remove redundancy, clarify wording, and tighten links to evidence.

## Operating rules
- Do not write the full artifact in one pass when it is complex.
- Do not expand sections without a defined outline.
- Do not mix decision content with evidence content.
- Do not allow the outline to drift after validation.

## SoT output contract
A SoT-driven artifact should include:
- section list
- section purpose
- section content
- traceability markers
- open questions
- review status

## Anti-patterns
- starting with prose instead of outline
- duplicating the same content across sections
- expanding without validating the skeleton
- producing a monolith that is hard to review

## Integration points
- templates
- step consistency
- system consistency
- decision framework
- human review

## Suggested telemetry
- `sot_outline_created`
- `sot_section_expanded`
- `sot_structure_validated`
- `sot_artifact_refined`
