# Release Evidence

## 1. CI/CD Pipeline Status
The GitHub Actions workflow CI (build-and-test) is successfully passing on the final-project branch.
- *Status:* Success
- *Build Duration:* 26s
- *Link:* [GitHub Actions Run #49](https://github.com/chadyfrancis18/task-tracker-midterm/actions/runs/31613556031)

## 2. Docker Build Evidence
The application builds successfully using the Dockerfile.
- *Command:* docker build -t task-tracker .
- *Result:* Image built successfully.

## 3. Pytest Execution
All tests are passing within the CI pipeline.
- *Total Tests:* 4
- *Result:* 4 passed in 0.34s
- *Test cases covered:* Root read, Task creation, Overdue filtering, and Task deletion.
