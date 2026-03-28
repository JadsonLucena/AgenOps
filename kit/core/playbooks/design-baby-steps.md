# Design in Baby Steps Playbook

## Purpose

Break the approved scope into the smallest reviewable design chunks using the spec document design as the source of truth.

## Use when

- the problem frame is clear enough to design
- the change is too large for a single implementation pass
- the design needs to remain easy to review, test, and revert

## Steps

1. Read the spec document design.
2. Identify the architectural boundary of the change.
3. Split the scope into independent chunks with one purpose each.
4. Map each chunk to its spec section, file targets, and documentation triggers.
5. Define the outcome, affected interfaces, data impact, and review target for every chunk.
6. Keep only one active chunk at a time.
7. Re-check the chunk size whenever it grows beyond a single review cycle.
8. Confirm the next chunk only after the current one is clarified and verifiable.

## Outputs

- ordered design chunk list
- current chunk
- chunk acceptance criteria
- spec section mapping
- file targets
- impacted docs
- test implications
- rollback notes when relevant

## Guardrails

- Prefer revertible slices.
- Avoid multi-purpose chunks.
- Keep the design small enough to fit one review conversation.
- Escalate to the Software Architect when the chunk boundary is unclear.
