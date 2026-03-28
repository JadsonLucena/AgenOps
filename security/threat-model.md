# Threat Model

## Scope
The system includes:
- AI agents
- shared state
- planning artifacts
- validation gates
- approval gates
- telemetry and learning loops
- external input sources

## Core security objectives
- preserve confidentiality of prompts, secrets, and internal state
- preserve integrity of decisions, artifacts, and approvals
- preserve availability of the governance workflow
- limit autonomous blast radius

## Primary threat classes

### 1. Prompt injection
Untrusted text may attempt to alter agent behavior, bypass rules, or redirect tool usage.

### 2. Tool abuse
An agent may overuse tools, escalate privilege, or perform unintended actions.

### 3. Data exfiltration
Sensitive state, secrets, or internal reasoning may leak through outputs, logs, or external calls.

### 4. Integrity compromise
Artifacts, decisions, or state entries may be modified without proper authority or review.

### 5. Boundary crossing
A role may attempt to operate outside its trust boundary or write to canonical state directly.

### 6. Supply-chain or artifact tampering
Imported templates, scripts, or generated outputs may be replaced or poisoned.

### 7. Autonomous overreach
An agent may take actions that should require human approval or a stronger gate.

## Abuse cases
- malicious content in planning artifacts
- injected instructions inside retrieved documents
- unauthorized state mutation
- approval without evidence bundle
- skipped validation gate
- security-sensitive change routed through a non-security reviewer

## Mitigations
- strict trust boundaries
- read-only access by default
- least-privilege permissions
- deterministic validation before approval
- structured evidence bundles
- traceable decision records
- secure handling of untrusted content
- human approval for high-risk transitions

## Security rule
If an agent cannot prove that an action is within its permission envelope, the action must be rejected or escalated.
