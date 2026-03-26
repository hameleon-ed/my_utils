# Global Agent Policy

This repository is a research-grade system focused on reproducible, modular, and extensible AI-driven experimentation.

The agent must operate under the following invariant principles.

---

## 1. Architectural Integrity

- Preserve modular boundaries.
- Core logic must remain inside `src/`.
- Entry points must remain inside `apps/`.
- Avoid circular dependencies.
- Avoid implicit cross-module coupling.
- Do not mix training, evaluation, and visualization logic.

If restructuring is required:
- Propose a migration plan before modifying files.

---

## 2. Reproducibility First

All changes must preserve:

- Deterministic experiment reproducibility
- Explicit hyperparameter logging
- Configuration traceability
- Environment specification integrity

Do not introduce hidden randomness or implicit state.

---

## 3. Planning Protocol

For multi-file changes:

1. Provide structured plan
2. Identify affected modules
3. Explain architectural impact
4. Wait for approval before execution

Never execute large refactors without a plan.

---

## 4. Minimal Intrusion Principle

- Do not rewrite unrelated files.
- Avoid cosmetic changes unless requested.
- Preserve existing naming conventions.
- Maintain backward compatibility unless explicitly allowed.

---

## 5. Research Governance

When modifying RL components:

- Analyze reward structure stability
- Consider normalization effects
- Evaluate non-stationarity risks
- Avoid hidden reward scaling
- Preserve evaluation comparability

---

## 6. Documentation Standard

All new modules must include:

- Purpose description
- Input/output expectations
- Architectural role
- Reproducibility notes (if applicable)

---

## 7. Safety Constraints

The agent must NOT:

- Remove experiment history
- Modify version control metadata
- Alter CI/CD without explanation
- Introduce silent dependency upgrades
- Modify evaluation metrics without justification

---

## 8. Optimization Awareness

Prefer:

- Explicit over implicit
- Modular over monolithic
- Transparent over clever
- Reproducible over convenient

---

## 9. Meta Rule

If instructions conflict:
- Prioritize reproducibility
- Then architectural clarity
- Then minimal change scope