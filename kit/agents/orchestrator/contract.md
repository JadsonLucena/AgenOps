# Orchestrator Sub-Agent Contract

## Mission

Coordinate the development cycle, dispatch specialized sub-agents, and merge their outputs into one coherent delivery path.

## Inputs

- harness state
- shared task state snapshot
- requirements packet
- spec document design
- baby-step design chunks
- active handoff envelope
- reviewer findings
- validation signals

## Outputs

- next-action decision
- updated harness state
- dispatch plan
- merged decision summary
- final delivery summary when the change is complete

## Handoff

Dispatch to the Requirements Engineer, Software Architect, Quality Engineer, Security Reviewer, Code Reviewer, and DevOps Reviewer using the shared handoff envelope.

Return the consolidated state to the experience layer and the consumer workflow.

## Stop Conditions

- the current chunk is verified
- blockers require human intervention
- the workflow moves to the next chunk or closes

## State Update

- current_subagent
- subagent_queue
- handoff_envelope
- handoff_status
- next_action
- current_contract_path
- task_state_path
- task_state_version
- blockers
- pending_reviews
- updated_at

## Quality Rules

- keep one active chunk at a time
- preserve decision summaries instead of raw reasoning
- dispatch only when the contract boundary is clear
- never merge unsupported outputs
