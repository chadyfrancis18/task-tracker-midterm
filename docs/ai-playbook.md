# AI Playbook & Architecture Guidelines

## When you reach for AI first
- Generating boilerplate code, structural scaffolding, and initial Pydantic models in FastAPI (backend/main.py).
- Writing unit test templates using pytest and TestClient for standard CRUD and PATCH operations.
- Debugging syntax errors, status codes, or package dependency conflicts in requirements.txt.

## When you do not
- Writing core authentication logic, password hashing, or token verification (since this project intentionally has no auth system).
- Final architectural decisions regarding complex external database connections or ORMs (since this project uses an in-memory tasks_db list).

## Your non-negotiables
- No hardcoded API keys, database URLs, or plaintext secrets are ever allowed in code or prompts.
- Every single AI-generated snippet must be manually reviewed line-by-line and tested locally using pytest.

## Your review rules
- Check for unintended global state modifications or data leakage between tests.
- Verify that all package imports actually exist and match the project dependencies.

## What you are still figuring out
- Optimizing data structures for handling larger in-memory collections under high concurrency.
- Fine-tuning automated CI pipeline triggers and multi-stage Docker builds.

## Decision Card

1. *New Feature:* Choosing to implement a partial update route (PATCH /tasks/{task_id}) using Pydantic's exclude_unset=True rather than a full PUT replacement, to align with standard REST practices for updating task status or titles safely.
2. *Code Review:* Manually inspecting all route handlers in backend/main.py to ensure proper HTTPException handling (e.g., returning 404 when a task ID is not found).
3. *Debugging:* Resolving test execution mismatches by ensuring that test case function names in tests/test_main.py precisely match the documented release evidence.
4. *Infrastructure:* Deciding to use a lightweight Dockerfile and in-memory list storage (tasks_db) instead of an external database to maintain simplicity and fast execution for this project scope.
5. *Never-Paste:* Refusing to paste unverified or generic code snippets directly into production files without checking type hints and schema models first.
6. *One Rule:* Maintaining strict synchronization between code implementation, automated test suites, and documentation files (release-evidence.md and ai-playbook.md) at all times.
