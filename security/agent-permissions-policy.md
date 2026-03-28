# Agent Permissions Policy

## Rules

### 1. Least privilege
Every agent receives only the permissions required to perform its role.

### 2. Read is cheaper than write
Default access should be read-only unless a role explicitly requires write access.

### 3. Orchestrator is the only canonical writer
Only the orchestrator may mutate canonical governance state.

### 4. Reviewers advise, they do not self-authorize
Review roles can emit findings and block gates, but they cannot silently grant themselves broader access.

### 5. Sensitive actions require explicit approval
Any action that crosses a trust boundary or affects production must require a documented approval path.

### 6. Permissions are versioned
Permission envelopes evolve through versioned policy updates, not ad hoc exceptions.

### 7. Deny by default
If a capability is not declared in the schema, it is forbidden.

### 8. AI agents are high-risk actors
Agent autonomy increases the need for blast-radius control, logging, and human override paths.
