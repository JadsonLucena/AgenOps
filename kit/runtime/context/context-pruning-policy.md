# Context Pruning Policy

## Purpose

Remove stale or low-value material from the active context without losing the task truth.

## Prune

- repeated background text
- superseded drafts
- obsolete design alternatives
- resolved questions
- completed review notes older than the latest summary
- duplicate excerpts from durable documentation

## Preserve

- task objective
- approved requirements
- architecture decisions
- open questions
- blockers
- risks
- current sub-agent
- current chunk
- current snapshot pointer

## Rule

Pruning must preserve the truth-bearing fields and update the snapshot version.
Do not prune away decisions, only the redundant path taken to reach them.
