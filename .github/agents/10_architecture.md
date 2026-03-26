# Architecture Policy

This repository follows a strict modular research architecture.

Rules:
- All core logic must live inside src/<package_name>/
- apps/ contains only entrypoint scripts
- No business logic in notebooks
- No training logic inside evaluation modules
- Separate environment, model, training, and evaluation layers

When proposing refactoring:
- Preserve modular boundaries
- Avoid circular dependencies
- Maintain reproducibility