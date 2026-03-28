# Experience Manifest

## Scope

This module improves how the kit is consumed.

## Entries

- phase-map.md
- quick-flow.md
- next-step-guidance.md
- command-map.md
- menu-patterns.md
- onboarding.md
- state-model.md
- state-store.md
- state-machine.md
- decision-routing.md
- state-router.py

## Harness rule

The experience module keeps a small persistent state so guidance can be deterministic across commands and sessions.
The harness must be able to route brainstorming, spec document design, design chunks, and formal sub-agent handoffs without losing the current state.
It must also know when to compact, snapshot, and prune the active context.
