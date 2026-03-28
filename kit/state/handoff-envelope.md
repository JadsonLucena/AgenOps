# Handoff Envelope

## Purpose

Pass work between sub-agents without leaking unnecessary context.

## Include

- task_id
- source_agent
- target_agent
- phase
- current_chunk
- objective_summary
- shared_state_version
- context_snapshot_path
- summary_path
- expected_output
- constraints
- blockers
- open_questions
- due_at

## Rule

The handoff envelope must be concise and should reference snapshots or summaries instead of embedding long transcripts.
