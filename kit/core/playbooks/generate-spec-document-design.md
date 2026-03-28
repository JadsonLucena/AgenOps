# Generate Spec Document Design Playbook

## Purpose

Turn elicited requirements into a spec document design: a small, reviewable blueprint that defines the sections, file paths, and downstream artifacts needed before detailed design or implementation begins.

## Use when

- requirements are elicited but not yet structured enough for design
- the change needs a clear artifact roadmap
- multiple documents will be triggered by the same change
- the next step must stay small, explicit, and reviewable

## Steps

1. Restate the goal in one sentence.
2. Split the spec into small sections such as problem, scope, business rules, acceptance criteria, risks, and file plan.
3. Assign each section to a target file path or document owner.
4. Mark downstream artifacts and documentation triggers for each section.
5. Identify the next design chunk and the review target for that chunk.
6. Keep only one active spec section at a time.
7. Record open questions and assumptions that still block safe design.

## Outputs

- spec outline
- section order
- file path plan
- downstream artifact map
- design chunk candidates
- review targets
- test implications
- open questions

## Guardrails

- Do not add implementation detail to the spec design.
- Do not mix multiple concerns into one section.
- Do not let the plan grow beyond one review cycle.
- Escalate to the Software Architect when a file boundary or design boundary is unclear.
