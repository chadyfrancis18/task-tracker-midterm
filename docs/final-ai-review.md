## 1. AI Review Comments
* Comment 1: Suggested adding automated unit tests for the main task routes.
* Classification: Useful
* Reason: It improved code coverage and caught regressions early.
* Comment 2: Proposed a complex caching layer using Redis for simple get tasks.
* Classification: Noise
* Reason: Over-engineering for a small project scope where local memory is sufficient.
* Comment 3: Suggested refactoring main application logic for better separation.
* Classification: Useful
* Reason: It streamlined the FastAPI endpoint structure.

## 2. Security Findings
* Finding 1: Potential hardcoded string checks in backend logic.
* Classification: False Positive
* Reason: No sensitive credentials or secrets are hardcoded in the codebase.
* Finding 2: Missing rate limiting on public endpoints.
* Classification: Noise
* Reason: Out of scope for this specific academic project requirements.

## 3. Manual Check Performed
* Self-Check: Verified manually that running pytest and the /health endpoint returns the expected responses successfully.

## 4. Rejected or Corrected AI Suggestion
* Suggestion: The AI suggested using global mutable state to cache user tasks for faster retrieval.
* Action Taken: Rejected / Corrected because it introduces concurrency bugs; replaced with clean local state handling.

## 5. AI Usage Rules & Decision Card Scenarios
1. New Feature: Use AI for scaffolding and generating boilerplate logic under strict design oversight.
2. Code Review: Critically evaluate AI suggestions for security flaws, dead code, or performance bottlenecks.
3. Debugging: Leverage AI to analyze error traces and propose fixes, followed by manual validation.
4. Infrastructure: Use AI-assisted guidance for containerization and environment configuration files.
5. Never-Paste: Never paste raw AI-generated code or configuration blocks directly into production without line-by-line manual review.
6. One Rule: Always verify package compatibility and ensure imports match the project requirements.

## 6. Ownership Statement
I, Chady Francis, designed, implemented, and thoroughly tested the Task Tracker application code structure within this repository. I have personally validated all automated tests, container configurations, and execution workflows. Every line of code and documentation included in this final submission has been meticulously reviewed and understood by me
