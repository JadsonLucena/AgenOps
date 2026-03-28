# Decision Tree

Use this tree before making a decision.

## 1. Is the decision actually needed?
- If no, defer.
- If yes, continue.

## 2. Is the decision a repeat of an existing approved pattern?
- If yes, reuse the existing decision and link it.
- If no, continue.

## 3. Is the decision deterministic?
- If yes, prefer validation or policy.
- If no, continue.

## 4. What is the reversibility?
- Fully reversible
- Partially reversible
- Irreversible

Rule:
- Irreversible decisions require stronger evidence, more review, and explicit approval.

## 5. What is the systemic impact?
- single artifact
- single module
- multiple modules
- multiple teams
- runtime / production impact

Rule:
- higher systemic impact increases review depth.

## 6. What is the cost vs benefit profile?
- low cost / high benefit: proceed
- low cost / low benefit: often defer
- high cost / high benefit: evaluate alternatives carefully
- high cost / low benefit: reject

## 7. Is the decision policy-sensitive?
- security
- compliance
- data handling
- architectural boundary
- release / production

Rule:
- policy-sensitive decisions require explicit evidence and traceability.

## 8. Can it wait?
- If yes, defer until more evidence exists.
- If no, decide with the available evidence and document assumptions.

## 9. Final check
Decision must answer:
- Why this option?
- Why now?
- What breaks if we do nothing?
- What would make us reverse this decision?
