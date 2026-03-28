# Integration Map

## Core integration points

| Layer | Contract path | Purpose |
|---|---|---|
| Core | `kit/core` | roles, workflows, playbooks |
| State | `kit/state` | canonical shared task state |
| Runtime | `kit/runtime` | context, memory, observability hooks |
| Validation | `kit/validation` | deterministic and semantic validation |
| Security | `security/` | threat model, trust boundaries, permissions |
| Judging | `kit/judging` | qualitative review and human gate support |
| Experience | `kit/experience` | routing and phase navigation |
| Templates | `kit/templates` | artifact blueprints |
| Policies | `kit/policies` | global constraints |
| Topology | `governance/topology` | team ownership and interaction modes |
| Decision | `governance/decision` | explicit decision framework |
| Telemetry | `runtime/telemetry` | runtime observability |
| Economics | `governance/economics` | budget and cost controls |
| GitOps | `governance/gitops` | semver, commits, branch flow |
| Learning | `learning/` | incidents, retrospectives, evolution |

## System-level coupling rule
A layer may depend on lower-level artifacts for reading or validation, but it must not silently mutate another layer's canonical source of truth.
