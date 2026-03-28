# Integration Map

## Canonical layer map

| Layer | Path | Purpose |
|---|---|---|
| Core | `kit/core` | roles, workflows, playbooks, protocols |
| Skills | `kit/skills` | reusable capabilities for agents |
| State | `kit/state` | canonical shared task state |
| Runtime | `kit/runtime` | execution, memory, observability hooks |
| Validation | `kit/validation` | system and step consistency enforcement |
| Security | `security` | permissions and trust boundaries |
| Judging | `kit/judging` | advisory qualitative evaluation |
| Experience | `kit/experience` | routing, onboarding, phase map |
| Templates | `kit/templates` | artifact blueprints |
| Policies | `kit/policies` | global governance rules |
| Topology | `governance/topology` | team ownership and interaction modes |
| Decision | `governance/decision` | ADR + ToT |
| Telemetry | `runtime/telemetry` | logs, traces, metrics |
| Economics | `governance/economics` | cost and budget control |
| GitOps | `governance/gitops` | versioning and change management |
| Learning | `learning` | incidents, retrospectives, evolution |
| Meta-model | `meta-model` | global consistency contract |

## Compatibility note
Some legacy mirror paths are retained for downstream consumers. The canonical contract is defined by the layer map above and the meta-model.
