# Cache Invalidation Policy

Invalidate cache entries when any of the following changes:
- source file hash
- config version
- playbook version
- workflow version
- role version
- relevant environment state

If the input is materially different, do not trust the old cache entry.
