## Feature 1: Due Dates & Overdue Filter
1. As a user, I want to add a due date to a task via the modal form so that I can track deadlines effectively.
   - Acceptance Criteria: Valid ISO date format (YYYY-MM-DD) is accepted, and invalid date formats return a 422 error status.
   - AI Assumption Corrected: Adjusted validation to explicitly reject malformed date strings instead of falling back to default values.
2. As a user, I want to filter tasks by overdue status so that I can see what needs immediate attention.
   - Acceptance Criteria: Enabling the overdue filter returns only tasks with a due date earlier than the current date.
3. As a user, I want to see a visual indicator on overdue tasks so that I can easily spot delayed items.
   - Acceptance Criteria: Overdue cards display an explicit overdue marker and custom styling in the UI.
4. As a user, I want to update an existing task with a new due date so that I can manage changing project timelines.
   - Acceptance Criteria: Updating task details successfully modifies the stored due date and recalculates the overdue status.
5. As a user, I want to omit the due date for tasks that do not have strict deadlines so that the field remains optional.
   - Acceptance Criteria: Creating a task without a due date succeeds and defaults the value safely.

## Feature 2: Tags / Labels
1. As a user, I want to assign tags to a task through the form input so that I can categorize related work.
   - Acceptance Criteria: Tags can be submitted as comma-separated strings and are processed into a clean backend list.
   - AI Assumption Corrected: Ensured tag splitting handles whitespace and strips empty entries cleanly.
2. As a user, I want to filter tasks by tag so that I can view specific project categories.
   - Acceptance Criteria: Filtering by a specific tag returns only tasks containing that tag.
3. As a user, I want empty or duplicate tags to be handled cleanly so that the tag list remains organized.
   - Acceptance Criteria: Blank tag inputs are rejected or stripped out during processing.
4. As a user, I want my tags to be preserved during unrelated updates so that categorization is not lost.
   - Acceptance Criteria: Updating task titles or descriptions does not clear or alter existing assigned tags.
5. As a user, I want to view tag chips directly on task cards so that I can quickly identify categories at a glance.
   - Acceptance Criteria: Each tag is rendered clearly as a visual chip element inside the task card UI.
