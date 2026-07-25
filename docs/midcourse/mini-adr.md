- *Context:* Extending the existing Flask Task Tracker application with due dates and tags while keeping the architecture lightweight.
- *Decision:* 
  1. Store due_date as standard strings in ISO format and compute the overdue state dynamically in the backend logic using Python datetime.
  2. Normalize tag inputs by splitting comma-separated strings and trimming whitespace to prevent formatting inconsistencies.
- *Alternatives Considered & Rejected:* Rejected heavy external calendar libraries and complex database relations for tags as they overbuild beyond the requirements of Flask modules.

