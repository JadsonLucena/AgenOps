# State Versioning Policy

## Purpose

Ensure every shared state update is traceable.

## Rules

- increment the task version on every meaningful merge
- increment the context snapshot version whenever compaction occurs
- keep changelog entries short and specific
- never replace a prior snapshot in place; write a new snapshot version or timestamped file
- prefer deterministic file names for the latest snapshot pointer
