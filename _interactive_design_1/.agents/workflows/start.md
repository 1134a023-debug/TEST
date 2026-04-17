---
description: Initialize project memory and high-fidelity context retrieval
---
1. **Environment & Role Audit**: Verify your project roles as **System_Architect, Specialist**. Determine if greenfield or existing.
2. **System Health Verification**: Run `docker ps` and syntax checks. If the container is not running, execute `docker compose up -d`.
3. **Rigid Internalization**: Read `AGENTS.md`. Align with the User's roles: **Researcher, Developer**. Internalize Core Rules.
4. **Semantic Memory Reconstruction**: Extract Historical Habits to form context.
   🚨 **MANDATORY**: AI MUST explicitly execute LanceDB to read memory (run INSIDE container):
   - `docker exec -i -interactive-design-1-workspace bash -c "source .venv/bin/activate && python scripts/query.py 'important architecture status'"`
   - `docker exec -i -interactive-design-1-workspace bash -c "source .venv/bin/activate && python scripts/query.py 'recent decisions'"`
   - **Domain Queries** (General Purpose):
   - `docker exec -i -interactive-design-1-workspace bash -c "source .venv/bin/activate && python scripts/query.py 'recent project changes and commit history'"`
   - `docker exec -i -interactive-design-1-workspace bash -c "source .venv/bin/activate && python scripts/query.py 'unresolved issues and blockers'"`
5. **Autonomous Mission Adaptation**: Determine task complexity. Jump to EXECUTION or draft a plan.
6. **Ready Message**: Confirm system readiness and role synchronization to the User.
