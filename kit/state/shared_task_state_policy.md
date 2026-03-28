# Shared Task State Policy

## Purpose

Provide a shared state that multiple sub-agents can read safely while the orchestrator preserves the canonical truth.

## Context control

The shared task state may include a compact context section with:
- context budget
- estimated tokens
- status
- snapshot version
- snapshot path
- summary path
- last compaction time

## Rules

- the orchestrator owns merges and version increments
- sub-agents may append findings and propose updates in their own scope
- no sub-agent may silently overwrite the canonical state
- the active context should be compacted before it grows unhealthy
- snapshots should be taken before pruning when the current context still has decision value
- summaries must preserve the decision value, not the whole transcript
