# Interaction Modes

The organizational design must make coupling explicit and limited.

## 1. Collaboration

Use when a stream-aligned team and the platform team are shaping a contract, workflow, or template together.

### Allowed for
- contract design
- interface negotiation
- platform usability improvements
- adoption debugging

### Rules
- time-box the collaboration
- produce a durable contract at the end
- do not keep the dependency informal

## 2. X-as-a-Service

Use when a stream-aligned team consumes a stable platform capability.

### Allowed for
- validation
- templates
- shared state schemas
- review policies
- onboarding flows

### Rules
- the platform publishes a stable interface
- consumers do not modify internals
- compatibility is versioned and documented

## 3. Facilitating

Use when the enabling team is helping a stream-aligned team improve capability.

### Allowed for
- training
- pair design
- workflow coaching
- pattern transfer
- AI adoption

### Rules
- temporary by design
- capability transfer is the goal
- the enabling team should exit when the gap closes

## 4. Explicitly prohibited modes

### Hidden ownership
No team may depend on an implicit owner for critical governance artifacts.

### Unlimited collaboration
No team may remain in permanent co-design with the platform.

### Direct state mutation
No consumer team may mutate canonical governance state.

### Ad hoc exception loops
No team may bypass policy by negotiating outside the documented approval path.

## Flow rule

Prefer pull-based flow from stream-aligned teams to the platform.

Avoid pushing platform changes into stream teams unless the change is a breaking governance update, a security correction, or a compatibility migration.
