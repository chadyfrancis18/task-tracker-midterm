## 1. The Stack
* Language: Python 3.10+
* Framework: FastAPI
* Testing: pytest
* Containerization: Docker (Non-root user)

## 2. Run and Test Commands
* Install: pip install -r requirements.txt (or from backend if structured so)
* Run Server: uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
* Run Tests: pytest tests/ -v
* Docker Build: docker build -t task-tracker-backend .

## 3. Project Rules
* No hardcoded secrets; use .env.
* All code and logic reside strictly inside the backend/ directory.

## 4. Docs-First Guardrail
* No implementation occurs without documentation and verified test runs.
* Guardrail Confirmation: Verified and strictly enforced.

## 5. AI Usage Rules & Decision Card Scenarios
1. Never-Paste Rule: Never paste raw AI-generated code directly into production files without line-by-line manual code review and verification.
2. Code Review: Critically evaluate AI suggestions for security flaws, dead code, or performance bottlenecks.
3. Debugging: Leverage AI to analyze error traces and propose fixes, followed by manual validation.

## 6. Decision Card
| Decision / Scenario | Action Taken / Rule Applied |
| :--- | :--- |
| 1. Framework Selection | Selected FastAPI for modern asynchronous support and clean routing. |
| 2. Testing Framework | Utilized pytest for automated and reliable endpoint testing. |
| 3. Containerization | Implemented non-root security practices in Docker. |
| 4. AI Assistance | Used AI strictly for scaffolding and test optimization under human oversight. |
| 5. Documentation Guardrail | Ensured all code modifications are reflected in evidence docs. |
| 6. Security Compliance | Rejected hardcoded secrets and enforced environment variables. |

## 7. Developer Ownership Statement
I, Chady Elias Francis, take full and absolute ownership of every line of code, configuration file, and documentation artifact within this repository, and have personally verified all execution commands.
