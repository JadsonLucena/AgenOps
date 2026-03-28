# Summarization Rules

## Goal

Compress context while preserving the decision value.

## Keep

- goal
- current phase
- changed artifacts
- decisions
- risks
- blockers
- open questions
- next step

## Drop

- full dialogue history
- duplicate paraphrases
- raw internal reasoning
- obsolete options already rejected

## Style

- prefer bullet summaries
- use stable names for artifacts
- reference paths rather than copying content
- keep summaries short enough to rehydrate quickly

## Rule

A summary should support the next action without forcing the harness to reload the entire conversation.
