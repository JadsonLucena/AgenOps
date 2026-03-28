# Release Process

## Steps

1. Ensure all PRs are merged into develop
2. Create release branch
3. Run full validation:
   - contracts
   - security
   - evidence bundle
   - telemetry checks
4. Generate changelog
5. Bump version (SemVer)
6. Merge into main
7. Tag release
8. Merge back to develop

## Gate requirements

Release cannot proceed without:
- passing validation
- passing security review
- evidence bundle complete
- decision records updated
