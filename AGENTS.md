## 1. The Stack
- *Language:* Python 3.10+
- *Framework:* FastAPI
- *Testing:* pytest
- *Containerization:* Docker (Non-root user)

## 2. Run and Test Commands
- *Install:* pip install -r backend/requirements.txt
- *Run Server:* uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
- *Run Tests:* pytest backend/tests/ -v
- *Docker Build:* docker build -t task-tracker-backend ./backend

## 3. Project Rules
- No hardcoded secrets; use .env.
- All code and logic reside strictly inside the backend/ directory.

## 4. Docs-First Guardrail
- No implementation occurs without documentation and verified test runs.

## 5. AI Usage Rules
1. Never commit blind code without manual verification.
2. Check all configurations for security risks.
3. Keep prompts scoped to specific project requirements.

## 6. Rejected or Corrected AI Suggestion
- *Correction:* The AI suggested running the Docker container as root by default. This was rejected and updated to use a dedicated non-root system user for security compliance.

## 7. Developer Ownership Statement
I, Chady Elias Francis, take full and absolute ownership of every line of code, configuration file, and documentation artifact within this repository, and I have personally verified all execution commands.
