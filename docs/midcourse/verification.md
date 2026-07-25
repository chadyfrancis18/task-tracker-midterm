## 1. Baseline Check
- Objective: Run the existing Task Tracker pytest suite and application functionality before making any changes to establish a baseline state.
- Execution: Executed pytest in the terminal and verified that all baseline tests passed successfully.
- Result: Baseline check confirmed clean starting code with zero failures in the base Task Tracker repository.

## 2. Backend Test Results
- Objective: Validate the implementation of Feature 1 (Due Dates & Overdue Filter) and Feature 2 (Tags / Labels) using pytest.
- Test Cases Added:
  1. test_create_task_with_valid_due_date_and_tags: Confirms that tasks accept valid ISO dates (YYYY-MM-DD) and comma-separated tags successfully.
  2. test_create_task_invalid_date_format: Verifies that malformed date strings return a 422 unprocessable entity error status code.
  3. test_overdue_task_detection: Checks that past dates are automatically computed and flagged as overdue (overdue: true).
  4. test_filter_overdue_tasks: Ensures that requesting /tasks?overdue=true correctly filters and returns only overdue tasks.
- Execution & Outcome: All new and existing pytest cases passed successfully against the FastAPI backend implementation.

## 3. Manual Browser Checks
- Objective: Verify user interface integration and responsiveness in frontend/index.html.
- Steps Performed:
  1. Opened the Task Tracker application in the browser.
  2. Created a new task with a due date and comma-separated tags via the input form.
  3. Verified that the task card renders correctly with the due date and visual tag chips.
  4. Tested the search input and the "Overdue only" checkbox filter to ensure dynamic list updates work smoothly without breaking layout or template rendering.

## 4. Behavior Contract & Break Test
- Objective: Verify API behavior contracts before and after refactoring, and perform explicit break tests to confirm error handling.
- Execution & Outcome: Confirmed contract stability across endpoints and verified robust error responses on malformed inputs.
