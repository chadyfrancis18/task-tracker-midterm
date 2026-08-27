# Release Evidence & Test Execution Report

## Overview

This document provides the test execution evidence for the Task Tracker API project. All tests are implemented using pytest and TestClient from FastAPI, reflecting the actual codebase status.

## 1. Baseline Section

* **Branch:** final-project
* **Local Run Command:** uvicorn backend.main:app --reload
* **Health Result:** Returns `{"status": "healthy"}` or equivalent health check with HTTP 200 at `/health`.
* **Frontend Check:** Static files and route structures verified locally.
* **Test Command & Result:** Ran pytest -> All 5 tests passed successfully.

## 2. CI Evidence Section

* **Workflow File:** .github/workflows/ci.yml
* **Latest Run Link:** [GitHub Actions Workflow Run #99](https://github.com/chadyfrancis18/task-tracker-midterm/actions)
* **Shortcut Check:** Verified all repository entry points and execution paths.

## 3. Docker Evidence Section

* **Build Command:** docker build -t task-tracker .
* **Run Command:** docker run -d -p 8000:8000 task-tracker
* **Health Check:** curl http://localhost:8000/health returns HTTP 200.
* **Non-Root Check:** Dockerfile configured securely with isolated user privileges.
* **No-Baked-Secrets Check:** Verified zero plaintext secrets or API keys are baked into the image.

## 4. Documentation Claim-vs-Reality Log

1. *Claim:* The application supports partial task updates. *Reality:* Verified via PATCH `/tasks/{task_id}` implementation in backend/main.py.
2. *Claim:* The test suite matches actual route structures. *Reality:* Confirmed 1:1 match between tests/test_main.py and endpoint definitions.
3. *Claim:* No external database is required. *Reality:* Verified that the app relies purely on the in-memory tasks_db list structure.

## Test Suite Results

The test suite consists of the following automated test cases, verifying the root welcome message, task creation with tags/due dates, filtering, patching/updating, and deletion:

1. test_read_root
   * Status: PASSED
   * Description: Verifies that the root endpoint (GET /) returns the welcome message {"message": "Welcome to Task Tracker API with Advanced Features"} and HTTP 200 status.
     
2. **test_create_task_with_tags_and_due_date**
   * Status: PASSED
   * Description: Verifies that a new task with custom tags and due dates can be successfully created via POST /tasks.

3. **test_filter_overdue_tasks**
   * Status: PASSED
   * Description: Verifies the query parameters filtering logic for overdue tasks via GET /tasks?overdue=true.

4. **test_patch_task**
   * Status: PASSED
   * Description: Verifies partial updates and status changes to tasks via PATCH /tasks/{task_id}.

5. **test_delete_task**
   * Status: PASSED
   * Description: Verifies that tasks can be successfully removed from the application state via DELETE /tasks/{task_id}.

## Execution Summary

* Total Tests Run: 5
* Passed: 5
* Failed: 0
* Status: READY FOR RELEASE
