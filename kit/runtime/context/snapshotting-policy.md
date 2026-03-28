# Snapshotting Policy

## Purpose

Turn a large or noisy context into a compact state snapshot.

## Snapshot content

A snapshot should retain:
- task identity
- current phase
- approved requirements
- current design chunk
- open questions
- blockers
- risks
- current sub-agent
- next action
- latest changelog entry

## Snapshot path

Prefer a stable path under planning artifacts or a user-scoped state directory.

## Rules

- snapshot before compaction when the context is still valuable
- snapshot after any major phase transition
- snapshot before handing off to a new sub-agent if the current context is broad
- keep snapshots versioned and timestamped

## Rule

A snapshot is a compact truth record, not a full transcript.
