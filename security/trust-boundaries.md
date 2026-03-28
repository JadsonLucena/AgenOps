# Trust Boundaries

## Boundary 1: External input -> system
Everything that comes from the user, files, web content, or downstream systems is untrusted until validated.

## Boundary 2: Planning artifacts -> canonical state
Drafts in `planning_artifacts/` are not authoritative. They must be reviewed and promoted before they can influence `docs/` or canonical state.

## Boundary 3: Agent local context -> shared state
A local agent may reason privately, but it may not mutate shared state directly.

## Boundary 4: Shared state -> approved artifacts
Only approved, validated, and traceable state may produce durable documents.

## Boundary 5: Platform governance -> consumer teams
Consumer teams may use the kit, but they do not change the platform's canonical rules without versioned governance.

## Boundary 6: Runtime telemetry -> learning layer
Telemetry informs learning, but telemetry alone does not change contracts. It must first be reviewed and interpreted.

## Trust rules
- no boundary is implicit
- every crossing must be named
- every crossing must be logged
- every sensitive crossing must be authorized
- every high-risk crossing must be reversible or explicitly accepted

## Practical trust zones

### Untrusted
- user input
- retrieved external content
- third-party documents
- arbitrary code or configs

### Controlled
- planning drafts
- agent-local summaries
- intermediate validation output

### Trusted
- approved contracts
- validated schemas
- canonical state
- signed or approved release artifacts

## Boundary principle
Zero trust means no component is trusted simply because it is "inside" the system; trust must be earned per request and per operation.
