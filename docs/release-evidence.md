## Part A: Baseline

- Branch Name: final-project
- API Start Command: uvicorn app.main:app --host 0.0.0.0 --port 8000
- Health Check (/health) Result:
{
"status": "healthy"
}

- CI Workflow Status: [Success - Run #58](https://github.com/chadyfrancis18/task-tracker-midterm/actions)

## Part B1: C1 Verification & Test Check

- Verification Status: Passed successfully.
- Test Command Evidence:

pytest tests/

## Part B2: Container Health & Runtime Response

- Docker Image Build Status: Successfully built using the multi-layer Dockerfile.
- Container Startup & Runtime Response:
  - Command: docker run -p 8000:8000 task-tracker-backend
  - Health Check Endpoint Response (/health): json { "status": "healthy" }
- Security Check: Verified that the application runs under a non-root user (appuser) as configured in the Dockerfile

## Part B3: Claims vs Reality Check

1. Claim 1 (API Health Endpoint): The application exposes a health check endpoint at /health returning a status of healthy.
   - Reality: Verified via container runtime response: {"status": "healthy"}.
2. Claim 2 (Docker Container User): The Dockerfile configures and runs the application using a non-root user for security.
   - Reality: Verified via Dockerfile instruction creating and switching to a non-root user.
3. Claim 3 (CI Pipeline Automation): Continuous integration automatically runs tests on every push to the repository using GitHub Actions.
   - Reality: Verified via successful GitHub Actions workflow execution ([CI Run #58](https://github.com/chadyfrancis18/task-tracker-midterm/actions)).

## Basics:

Frontend Verification Check
- Status: Verified
- Workflow & Execution: To test and review the frontend and backend workflow, open the user interface locally or via container runtime, ensure proper structure, verify smooth integration with the FastAPI backend, and check static assets.
