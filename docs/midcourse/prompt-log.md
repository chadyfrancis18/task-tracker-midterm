## Feature 1: Due Dates & Overdue Filter

### Prompt 1.1 (Due Date Backend Validation)
- *Weak Prompt:* "Add due date to Task Tracker tasks."
- *Refined Prompt:* "Write a Flask backend validation function for due_date using the YYYY-MM-DD ISO format within our existing Task Tracker, returning a 422 status code on validation error, and compute an overdue boolean value dynamically."
- *AI Returned:* Provided a Python datetime parsing function with basic exception handling and a helper to compare dates against the current day.
- *Action Taken:* Accepted the core parsing logic; edited the comparison rules to ensure proper timezone-naive local date handling so overdue filtering functions reliably across the Task Tracker backend.

### Prompt 1.2 (Overdue Query Parameter)
- *Weak Prompt:* "Filter overdue tasks."
- *Refined Prompt:* "Extend the Flask GET /tasks route in the Task Tracker to support an optional query parameter overdue=true that filters the task list returning only items where overdue is true."
- *AI Returned:* Suggested a query parameter check filtering the in-memory task array.
- *Action Taken:* Accepted with minor edits to combine search queries and overdue filters cleanly without conflicting loop conditions.

### Prompt 1.3 (Frontend Task Tracker Integration)
- *Weak Prompt:* "Show due date on HTML."
- *Refined Prompt:* "Write JavaScript fetch and DOM manipulation logic for frontend/index.html to include a due date input field in the Task Tracker creation form and display an overdue warning pill on task cards."
- *AI Returned:* Provided form input elements and dynamic template literals to render task metadata.
- *Action Taken:* Accepted after correcting backticks and template string syntax to ensure smooth rendering of tasks without breaking frontend execution.

---

## Feature 2: Tags / Labels

### Prompt 2.1 (Backend Tag Normalization)
- *Weak Prompt:* "Add tags to tasks."
- *Refined Prompt:* "Implement robust backend handling in the Flask Task Tracker for comma-separated tag inputs, ensuring tags are stripped of whitespace, empty strings are rejected, and unique lists are stored."
- *AI Returned:* Provided string .split(',') logic with a list comprehension.
- *Action Taken:* Accepted the list comprehension approach with additional safety checks to handle both array inputs and string inputs smoothly.

### Prompt 2.2 (Tag Filtering Route)
- *Weak Prompt:* "Search by tags."
- *Refined Prompt:* "Update the Flask GET /tasks route in the Task Tracker to support an optional tag query parameter that filters tasks containing the specified tag string."
- *AI Returned:* Provided conditional checking against the task's tag array.
- *Action Taken:* Accepted as written, ensuring case-consistent matching with stored tag lists.

### Prompt 2.3 (Frontend Tag Chips UI)
- *Weak Prompt:* "Render tags as pills."
- *Refined Prompt:* "Write JavaScript to map task tags into styled HTML tag chips and append them inside each Task Tracker card dynamically."
- *AI Returned:* Provided a .map() function generating span elements with CSS classes.
- *Action Taken:* Accepted fully, ensuring proper CSS styling and clean layout integration within the task container.
