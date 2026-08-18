# Release Evidence

## Part A: Baseline

- *Branch Name:* final-project
- *API Start Command:* uvicorn app.main:app --host 0.0.0.0 --port 8000
- *Health Check (/health) Result:*
  ```json
  {
    "status": "healthy"
  }
* *CI Workflow Status:* [Success - Run #58](https://github.com/chadyfrancis18/task-tracker-midterm/actions/runs/32127522792)
## Part B3: Claims vs Reality Check

1. *Claim 1 (API Health Endpoint):* The application exposes a health check endpoint at /health returning a status of healthy.
   * *Reality:* Verified via container runtime response: {"status": "healthy"}.

2. *Claim 2 (Docker Container User):* The Dockerfile configures and runs the application using a non-root user for security.
   * *Reality:* Verified via Dockerfile instruction creating and switching to a non-root user.

3. *Claim 3 (CI Pipeline Automation):* Continuous integration automatically runs tests on every push to the repository using GitHub Actions.
   * *Reality:* Verified via successful GitHub Actions workflow execution (CI Run #58).
