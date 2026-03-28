# Judge Integration

## Integration points

### ReAct Loop
- judge can run after `verify`
- influences next action (revise vs proceed)

### Human-in-the-loop
- low score triggers human review

### Validation
- judge complements validation, does not replace it

### Decision framework
- can score alternatives in trade-off matrix

## Rule
judge result must never override:
- validation failure
- security violation
- policy violation
