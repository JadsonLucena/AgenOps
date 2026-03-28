# Cache Strategy

Cache stable, deterministic artifacts.

## Good candidates

- parsed configs
- generated summaries
- validated file fingerprints
- deterministic check outputs
- unchanged diagrams or contracts

## Bad candidates

- transient state
- secrets
- noisy execution traces
- content that depends on rapidly changing runtime conditions
