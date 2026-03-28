# Gitflow Workflow

## Branches

### main
- production-ready code
- always stable

### develop
- integration branch
- latest changes

### feature/*
- new features
- branch from develop
- merge back to develop

### release/*
- preparation for release
- stabilize, test, fix bugs

### hotfix/*
- urgent fixes in production
- branch from main
- merge into main and develop

## Flow

1. feature → develop
2. develop → release
3. release → main
4. main → tag (version)
5. hotfix → main → develop

## Rule

- no direct commits to main
- all changes go through PR + validation
- release must pass all gates
