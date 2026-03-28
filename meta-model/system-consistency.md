# System Consistency

## Purpose
Ensure the entire governance system remains coherent across all layers.

## Scope
Applies to:
- state
- artifacts
- decisions
- telemetry
- policies
- workflows
- skills
- versioning

## Core Rules

### 1. State ↔ Artifacts
- Every approved artifact must be represented in state.
- State must not reference non-existent artifacts.

### 2. Decision ↔ Artifacts
- Every high-impact change must have a decision record.
- Decision records must reference affected artifacts.

### 3. Telemetry ↔ Execution
- Every critical action must emit telemetry.
- Missing telemetry means the execution is not fully governed.

### 4. Policies ↔ Runtime
- Runtime behavior must comply with declared policies.
- Policy violations must block progression.

### 5. Version ↔ Change
- Version bumps must reflect actual change type.
- Breaking changes without a MAJOR bump are invalid.

### 6. Skills ↔ Execution
- Skills used by agents must be registered and discoverable.
- Skill usage must be compatible with the current step and trust boundary.

### 7. Workflow ↔ Step Consistency
- Each step must have explicit inputs, outputs, and exit criteria.
- Skipping a required step invalidates the flow.

## Validation Checklist
- [ ] All canonical layers exist
- [ ] All approved artifacts are linked in state
- [ ] Decisions exist for impactful changes
- [ ] Telemetry is emitted for critical actions
- [ ] Policies are enforced
- [ ] Versioning matches the change type
- [ ] Skills are registered and accessible
- [ ] Step transitions are explicit

## Enforcement
The system is invalid if:
- orphan artifacts exist
- decision records are missing for impactful changes
- telemetry is missing for critical actions
- policy violations are detected
- step transitions are undefined
- registered skills are missing or untraceable
