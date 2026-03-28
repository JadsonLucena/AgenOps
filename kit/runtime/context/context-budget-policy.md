# Context Budget Policy

## Purpose

Keep the active context within a healthy operational limit.

## Rules

- define an explicit budget per task phase
- treat architecture, requirements, and spec design as higher-budget phases
- treat focused fixes, reviews, and small changes as lower-budget phases
- stop loading historical material once the budget is sufficient for the current decision
- prefer snapshots and summaries over raw history

## Recommended budget signals

Track these signals in the harness state:
- estimated_context_tokens
- context_budget_tokens
- context_budget_ratio
- context_status
- last_compacted_at

## Thresholds

- below 70%: healthy
- 70% to 85%: warning; compact soon
- above 85%: compact before the next non-trivial step
- above 100%: compact immediately and reduce active context

## Rule

The orchestrator owns the budget decision.
Sub-agents may request compaction, but they should not widen the active context on their own.
