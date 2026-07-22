# Mini Architecture Decision Record (ADR)

## Context
We needed to implement two core features (Due Dates and Tags) into the FastAPI Task Tracker while maintaining clean separation and test coverage.

## Decision
- Implemented due_date using Python's datetime.date type for robust comparisons.
- Implemented tags as a List[str] in Pydantic models to allow multiple categories per task.
- Added query parameters in the /tasks GET route to handle filtering logic on the server side.

## Alternatives Considered
- Storing tags and dates as raw unformatted strings: Rejected because it lacks proper validation and makes overdue calculations prone to errors.

