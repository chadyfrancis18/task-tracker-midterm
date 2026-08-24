# Release Evidence

## Part A: Baseline

* Branch Name: final-project
* API Start Command: uvicorn backend.main:app --host 0.0.0.0 --port 8000
* Health Check (/health) Result:
  ```json
  {
    "status": "healthy",
    "service": "task-tracker-backend"
  }


  *CI Workflow Status: Success - Run #58

## Part B1: C1 Verification & Test Check
$ pytest backend/tests/ -v
============================= test session starts ==============================
platform linux -- Python 3.10.12, pytest-7.4.0, pluggy-1.0.0
rootdir: /app
collected 5 items

backend/tests/test_main.py::test_read_health PASSED                      [ 20%]
backend/tests/test_main.py::test_create_task PASSED                      [ 40%]
backend/tests/test_main.py::test_get_tasks PASSED                        [ 60%]
backend/tests/test_main.py::test_update_task PASSED                      [ 80%]
backend/tests/test_main.py::test_delete_task PASSED                      [100%]

============================== 5 passed in 0.45s ===============================

## Part B2: Container Health & Runtime Response

* Docker Image Build Status: Successfully built using the multi-layer Dockerfile.
* Container Startup & Runtime Response:
  * Command: docker run -p 8000:8000 task-tracker-backend
  * Health Check Endpoint Response (/health): 
    json
    {
      "status": "healthy",
      "service": "task-tracker-backend"
    }
    
* Security Check: Verified that the application runs under a non-root user (appuser) as configured in the Dockerfile

## Part B3: Claims vs Reality Check


1. Claim 1 (API Health Endpoint): The application exposes a health check endpoint at /health returning a status and service.
   * Reality: Verified via container runtime response: {"status": "healthy", "service": "task-tracker-backend"}.
2. Claim 2 (Docker Container User): The Dockerfile configures and runs the application using a non-root user for security.
   * Reality: Verified via Dockerfile instruction creating and switching to a non-root user.
3. Claim 3 (CI Pipeline Automation): Continuous integration automatically runs tests on every push to the repository using GitHub Actions.
   * Reality: Verified via successful GitHub Actions workflow execution (CI Run #58)

## Basics:

### Frontend Verification Check

* Status: Verified
* Workflow & Execution: Opened the frontend interface locally via browser, confirming that the task board loads successfully and verifying the interactive create/edit task workflows with the backend.
