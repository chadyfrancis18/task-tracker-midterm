## 1. AI Review Comments
* *Comment 1:* Suggested refactoring for database dependency injection in backend/database.py. 
  * *Classification:* Useful
  * *Reason:* It simplified session management and made unit testing much cleaner.
* *Comment 2:* Proposed a complex caching layer using Redis for simple get tasks.
  * *Classification:* Noise
  * *Reason:* Over-engineering for a small midterm/final project scope where local memory is sufficient.
* *Comment 3:* Suggested removing authentication middleware from protected routes to speed up requests.
  * *Classification:* Wrong
  * *Reason:* It would completely break the security model and bypass token verification.

## 2. Security Findings
* *Finding 1:* Hardcoded secret key warning in backend/config.py.
  * *Classification:* Valid
  * *Reason:* Environment variables must be used instead of plaintext strings to prevent credential leaks.
* *Finding 2:* Potential SQL injection vulnerability flagged in raw query construction inside backend/models.py.
  * *Classification:* False Positive
  * *Reason:* SQLAlchemy ORM parameterization is already being used safely, neutralizing the risk.
* *Finding 3:* Missing rate limiting on the login endpoint.
  * *Classification:* Noise
  * *Reason:* Out of scope for this specific academic project requirements.

## 3. Manual Check Performed
* *Self-Check:* Verified manually that unauthenticated users trying to access protected task endpoints receive a 401 Unauthorized status code by testing via Postman/curl.

## 4. Rejected or Corrected AI Suggestion
* *Suggestion:* The AI suggested using global mutable state to cache user sessions for faster retrieval.
* *Action Taken:* *Rejected / Corrected* because it introduces concurrency bugs and thread-safety issues in FastAPI; replaced with proper dependency injection.

## 5. AI Usage Rules
1. Never let AI generate authentication or cryptographic logic without a strict line-by-line manual security review.
2. Always verify that AI-suggested package imports exist and match the project's requirements.txt.
3. Use AI primarily for scaffolding, boilerplate generation, and debugging assistance, retaining full ownership of architectural decisions.

## 6. Ownership Statement
I, Chady Francis, designed, implemented, and thoroughly tested the Task Tracker application code structure within this repository. I personally validated all automated tests, container configurations, and execution workflows. Every line of code and documentation included in this final submission has been meticulously reviewed and understood by me

## 7. AGENTS.md Guardrail Confirmation
* *Status:* Confirmed & Complied
* *Details:* All tasks, code generation, and documentation updates have strictly adhered to the guardrails, safety protocols, and formatting instructions outlined in AGENTS.md.
