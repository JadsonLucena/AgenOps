# Prompt Injection Defense

## Principle
Treat all external text as untrusted instructions unless it is explicitly validated as data.

## Controls
- separate instructions from data
- sanitize retrieved content
- never allow external content to redefine policy
- limit tool access for untrusted inputs
- require review for actions triggered by external text
- log suspicious instruction patterns

## AI-agent specific risks
- malicious text embedded in documents
- tool calls induced by hidden instructions
- unintended policy override
- data leakage via retrieval or output

## Response rule
When suspicious instructions are detected, the agent should:
1. stop
2. report
3. isolate the source
4. request review
