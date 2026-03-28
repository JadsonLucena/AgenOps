# Deterministic Step Cache

Only cache steps that produce repeatable results from repeatable inputs.

Examples:
- lint
- test discovery
- schema parsing
- document triggering
- fingerprint-based comparisons

Do not cache steps that depend on hidden state or unstable runtime conditions.
