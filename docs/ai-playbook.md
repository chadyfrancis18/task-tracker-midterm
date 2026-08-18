## When you reach for AI first
* Generating boilerplate code, structural scaffolding, and initial schemas (e.g., Pydantic models in FastAPI).
* Writing unit test templates using pytest for standard CRUD operations.
* Debugging cryptic tracebacks, syntax errors, or dependency conflicts in requirements.txt.

## When you do not
* Writing core authentication logic, password hashing, or token verification (must be written and reviewed 100% manually).
* Final architectural and security decisions regarding data flow or database connections.

## Your non-negotiables
* No hardcoded API keys, database URLs, or plaintext secrets are ever allowed in code or prompts.
* Every single AI-generated snippet must be manually reviewed line-by-line and tested locally using pytest.

## Your review rules
* Check for unintended global state modifications or concurrency issues.
* Verify that all package imports actually exist and match the project dependencies.

## What you are still figuring out
* Optimizing complex database queries for heavy asynchronous loads under production constraints.
* Fine-tuning automated CI pipeline triggers for multi-stage Docker builds.

## A Decision Card
* *Scenario:* Deciding whether to use an AI-suggested caching layer.
* *Context:* The application is a compact midterm/final Task Tracker.
## AI Usage Rules & Decision Card Scenarios

1. *New Feature:* Use AI for scaffolding and generating boilerplate logic under strict design oversight.
2. *Code Review:* Critically evaluate AI suggestions for security flaws, dead code, or performance bottlenecks.
3. *Debugging:* Leverage AI to analyze error traces and propose fixes, followed by manual validation.
4. *Infrastructure:* Use AI-assisted guidance for containerization and environment configuration files.
5. *Never-Paste:* Never paste raw AI-generated code or configuration blocks directly into production without line-by-line manual review.
6. *One Rule:* Always verify package compatibility and ensure imports match the project requirements.

## Basics: Frontend Verification Check
- *Status:* Verified
- *Workflow & Execution:* To test and review the frontend and backend workflow, open the user interface locally or via container runtime, ensure proper structure, verify smooth integration with the FastAPI backend, and check static assets.
* *Decision:* Reject the complex caching layer.
* *Rationale:* It introduces unnecessary architectural overhead and violates project simplicity scopes
## Frontend Verification Check
* *Status:* Verified
* *Details:* Checked frontend static assets and components to ensure proper structure and smooth integration with the backend API.
