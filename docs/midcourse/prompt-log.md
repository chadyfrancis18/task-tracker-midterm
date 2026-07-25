## Feature 1: Due Dates & Overdue Filter
- *Weak Prompt:* "Add due date to tasks."
- *Refined Prompt:* "Write a Flask backend validation function for due_date using YYYY-MM-DD format, returning 422 on error, and compute an overdue boolean."
- *Result & Action:* Accepted date parsing logic; edited comparison rules to handle timezone-naive local dates safely.

## Feature 2: Tags / Labels
- *Weak Prompt:* "Add tags."
- *Refined Prompt:* "Implement robust handling for comma-separated tag inputs in Flask Task Tracker to ensure clean list storage without empty values."
- *Result & Action:* Accepted list comprehension with .strip() and conditional filtering; rejected complex nested tag tables.
