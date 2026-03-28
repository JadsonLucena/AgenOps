# State Model

## Purpose

Define the state shape used by the harness.

## Fields

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

## Rule

The state model should be small, explicit, serializable, and safe to persist.
Do not store secrets or raw internal reasoning.
