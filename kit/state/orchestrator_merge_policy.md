# Orchestrator Merge Policy

## Purpose

Define how the orchestrator merges sub-agent output into the shared task state.

## Merge rules

1. Keep the latest canonical objective and scope.
2. Merge only the fields that the sub-agent owns.
3. Preserve conflicting views as open questions or risks.
4. Increase the state version on every meaningful merge.
5. Write a changelog entry for every merge.
6. If context grows unhealthy, compact and snapshot before accepting the next broad update.

## Conflict handling

- requirements conflict -> elicit again
- architecture conflict -> create or update ADR
- QA/security conflict -> preserve both findings and decide in the orchestrator
- documentation conflict -> prefer durable artifacts over drafts
