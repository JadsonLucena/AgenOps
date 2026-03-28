# State Store

## Purpose

Persist a small JSON state so the harness can produce deterministic next-step guidance across commands and sessions.

## Default location

Use `KIT_STATE_FILE` when set.
If it is not set, use a user-scoped state path such as `$XDG_STATE_HOME/engineering-governance-kit/state.json` or `~/.local/state/engineering-governance-kit/state.json`.

## Schema

Keep the state small, explicit, and serializable.

Recommended fields:
- session_id
- phase
- change_type
- last_completed_step
- next_action
- brainstorm_status
- requirements_status
- spec_status
- architecture_status
- design_status
- current_spec_section_index
- spec_sections
- spec_file_plan
- current_chunk_index
- design_chunks
- documentation_triggers
- test_status
- validation_status
- security_status
- blockers
- open_questions
- pending_reviews
- current_subagent
- subagent_queue
- current_contract_path
- upstream_contract
- downstream_contract
- handoff_envelope_path
- handoff_status
- last_handoff_at
- context_budget_tokens
- estimated_context_tokens
- context_budget_ratio
- context_status
- context_snapshot_version
- context_snapshot_path
- context_summary_path
- context_load_order
- last_compacted_at
- updated_at

## Rules

- do not store secrets
- do not store raw internal reasoning
- update the state after every meaningful transition
- keep one authoritative state file per session or task
- the state should track the current spec section, the current design chunk, the current sub-agent, the active handoff envelope, and the current context budget
