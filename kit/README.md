# Kit

Operational execution layer for the governance system.

## Canonical role
This layer contains the concrete workflows, role contracts, state artifacts, templates, and runnable helpers that implement governance decisions.

## Boundaries
- It consumes strategic policy from `governance/`
- It does not redefine system-wide policy
- It is the source of truth for day-to-day execution contracts
