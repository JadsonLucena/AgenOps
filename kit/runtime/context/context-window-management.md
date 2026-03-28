# Context Window Management

## Rules

- load on demand
- keep an explicit budget per phase
- summarize aggressively when the budget becomes tight
- prefer recent and authoritative artifacts
- use the minimum relevant source set
- prune irrelevant history early
- snapshot before compaction
- keep structured summaries rather than large verbatim copies
- rehydrate only the fields needed for the next decision

## Load order

1. shared task state
2. approved artifacts
3. latest summary
4. current sub-agent handoff
5. minimal supporting evidence
6. full historical details only on demand
