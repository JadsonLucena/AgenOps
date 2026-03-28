# AgenOps

**AgenOps** is a governance-driven system of AI agents and reusable skills designed to support, execute, and control the software engineering lifecycle.

It provides a portable, language-agnostic framework that can be embedded into any project as a Git module, enabling consistent engineering practices powered by intelligent agents and reusable skills.

## What AgenOps is

AgenOps is a governed agent system that combines:

- AI agent execution (ReAct)
- reusable skills
- structured decision-making (ADR + ToT)
- artifact lifecycle management
- validation and consistency enforcement
- human-in-the-loop control
- observability and telemetry
- security and trust boundaries
- cost awareness (FinOps)
- continuous learning loops

## Core flow

Plan → Explore → Decide → Execute → Validate → Learn → Improve

## Canonical layout

```text
/kit
  /core            → roles, workflows, playbooks, protocols
  /skills          → reusable capabilities for agents
  /runtime         → execution model, memory, observability hooks
  /validation      → enforcement (system and step consistency)
  /security        → permissions and trust boundaries
  /policies        → governance rules
  /playbooks       → structured execution patterns (SoT)
  /judging         → qualitative evaluation (LLM as a Judge)
  /templates       → durable artifact templates
  /state           → canonical shared state

/governance
  /decision        → ADR + ToT
  /topology        → team ownership and interaction modes
  /economics      → cost control (FinOps)
  /gitops         → versioning and change management

/runtime
  /telemetry       → logs, traces, metrics

/learning
  /incidents       → failures and analysis
  /retrospectives  → continuous improvement

/meta-model
  system-consistency.md
  README.md
```

## Key capabilities

### ReAct
Agents follow a controlled loop:
- Observe
- Reason
- Act
- Verify

### SoT
Skeleton of Thought keeps complex artifacts structured before expansion.

### ToT
Tree of Thought explores and prunes alternatives for hard decisions.

### LLM as a Judge
A rubric-based advisory judge scores artifacts without replacing validation.

### Human-in-the-loop
Critical actions require human approval when risk, impact, or ambiguity crosses a threshold.

### Observability
Structured events, traces, and metrics make runtime behavior visible.

### Economics
Budgets and cost models keep agent execution financially controlled.

### Learning
Incidents and retrospectives feed improvements back into the system.

## Artifact lifecycle

```text
draft → reviewed → approved → archived
```

Promotion requires:
- validation
- review
- evidence bundle

## GitOps integration

- Semantic Versioning
- Conventional Commits
- GitFlow

## Design principles

- Explicit over implicit
- Governed execution over free-form autonomy
- Validation over assumption
- Traceability over convenience
- Safety over speed
- Evolution over rigidity

## Compatibility note

Some legacy compatibility mirrors may exist under older `kit/*` paths. The canonical governance model is the current layer structure documented above and enforced by the meta-model.

## Installation

Add AgenOps as a Git submodule:

```bash
git submodule add <your-repo-url> AgenOps
```

## Contributing

Contributions should follow:
- the decision framework
- validation rules
- semantic commits
- evidence requirements

## License

Define your license here.
