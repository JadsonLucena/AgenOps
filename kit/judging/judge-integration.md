# Judge Integration

## Integration points

### ReAct Loop
- judge can run after `verify`
- judge influences the next action (`revise` vs `proceed`)

### Human-in-the-loop
- low score can trigger human review

### Validation
- judge complements validation, it does not replace it

### Decision framework
- judge can score alternatives in the trade-off matrix

## Rule
Judge results must never override:
- validation failure
- security violation
- policy violation
