# Team Types

This kit assumes a topology aligned with Team Topologies and flow efficiency.

## 1. Stream-aligned team

Owns a value stream or product slice end to end.

### Responsibilities
- deliver user-facing or domain-facing outcomes
- consume kit contracts and templates
- produce implementation, tests, and delivery artifacts
- maintain local product context

### What it should not own
- global governance rules
- core kit evolution
- shared platform mechanics
- cross-team approval policy

### Interaction with the kit
- uses the kit as a platform
- receives guidance from enabling teams
- requests support from platform owners
- follows the evidence bundle and lifecycle rules

## 2. Platform team

Owns the governance kit itself.

In this system, the kit is the platform.

### Responsibilities
- maintain core modules, schemas, policies, and templates
- evolve workflow contracts and validation rules
- preserve backwards compatibility where practical
- provide paved roads for downstream teams
- reduce cognitive and operational load for consumers

### What it should not own
- business domain decisions for consumer teams
- stream-specific implementation choices
- local product priorities
- ad hoc exceptions without policy

### Interaction with the kit
- publishes stable contracts
- receives feedback from stream-aligned teams
- exposes versioned artifacts
- owns platform-level quality and documentation

## 3. Enabling team

Accelerates adoption and maturity.

### Responsibilities
- improve onboarding and adoption of AI/governance practices
- teach teams how to use the kit correctly
- help close capability gaps
- model advanced workflows before they are standardized

### What it should not own
- permanent decision rights over product delivery
- long-term ownership of the platform
- local team execution ownership

### Interaction with the kit
- introduces patterns into stream-aligned teams
- feeds improvements back into the platform team
- validates usability, clarity, and ergonomics

## Topology rule

No team type should collapse into a generic "all-purpose delivery team".

Each team type must have a dominant responsibility and a bounded interface.
