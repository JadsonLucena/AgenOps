# Runtime Orchestration Hardening

## Purpose
Define how AgenOps runtime behavior must be hardened so that agent execution remains controlled, traceable, and safe under load.

## Core objective
Runtime orchestration must never behave like a free-form prompt loop. It must behave like a controlled state machine with checkpoints and escalation.

## Hardening principles

### 1. Single source of orchestration truth
The orchestrator determines:
- current step
- next allowed action
- stop conditions
- escalation target

### 2. Bounded execution
Each loop iteration must be limited to:
- one bounded action
- one checkpoint
- one verification result

### 3. Deterministic routing
Routing decisions must be based on:
- current state
- step contract
- policy constraints
- permissions
- evidence status

### 4. Explicit checkpointing
The runtime must checkpoint:
- before action
- after action
- after verification
- before escalation
- before state merge

### 5. Fail closed
If runtime cannot determine the next safe action, it must stop and escalate.

## What this hardening protects against
- silent state drift
- skipped validation
- hidden retries
- accidental multi-step jumps
- unlogged escalation
- unauthorized canonical writes

## Required runtime behaviors

### Orchestration start
- load state
- load step contract
- load policy context
- load telemetry context

### Routing
- choose a permitted role or sub-agent
- choose one bounded action
- reject ambiguous action plans

### Checkpointing
- persist execution checkpoints
- emit telemetry events
- retain stop reasons

### Verification
- confirm action outcome
- detect divergence early
- stop on mismatch

### Escalation
- route to human-in-the-loop when risk, ambiguity, or policy demands it
- preserve traceability of why escalation occurred

## Integration points
- ReAct loop
- step consistency
- system consistency
- human-in-the-loop
- unified enforcement
- progressive discovery
- judge output

## Operational rule
If the runtime cannot prove that the next step is safe, it must not continue.
