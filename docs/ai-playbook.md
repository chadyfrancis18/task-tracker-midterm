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
* *Decision:* Reject the complex caching layer.
* *Rationale:* It introduces unnecessary architectural overhead and violates project simplicity scopes
## Frontend Verification Check
* *Status:* Verified
* *Details:* Checked frontend static assets and components to ensure proper structure and smooth integration with the backend API.
