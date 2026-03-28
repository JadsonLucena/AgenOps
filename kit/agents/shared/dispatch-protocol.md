# Dispatch Protocol

## Purpose

Define how the orchestrator dispatches formal sub-agents and collects their return envelopes.

## Steps

1. Load the current harness state and shared task state snapshot.
2. Select exactly one target sub-agent.
3. Build the handoff envelope from the current phase and chunk.
4. Persist the envelope path and dispatch status to the shared state store.
5. Execute the target sub-agent within its contract boundary.
6. Collect the return envelope and findings.
7. Update the harness state and shared task state with the returned summary.
8. Route to the next phase or next sub-agent.

## Rule

Only one active sub-agent should own the current handoff at a time.
The orchestrator remains the only component allowed to merge multiple sub-agent outputs.
