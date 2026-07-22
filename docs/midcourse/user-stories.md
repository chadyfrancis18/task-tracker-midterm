# User Stories

## Feature 1: Due Dates + Overdue Filter
- *Story 1:* As a user, I want to assign a due date to a task so that I can manage my deadlines.
  - Acceptance Criteria: The task model accepts a valid due_date field.
- *Story 2:* As a user, I want to filter tasks to show only overdue items so that I can prioritize urgent work.
  - Acceptance Criteria: Query parameter /tasks?overdue=true returns uncompleted tasks past their due date.
- *AI Assumption Correction:* Corrected date format handling from string-only to Python native date objects for accurate comparison.

## Feature 2: Tags / Labels
- *Story 1:* As a user, I want to add tags to my tasks to categorize them.
  - Acceptance Criteria: Tasks can store a list of string tags.
- *Story 2:* As a user, I want to filter tasks by specific tags.
  - Acceptance Criteria: Query parameter /tasks?tag=name returns tasks containing that tag.
