# Comprehensive AI Prompt Log and Development History

This document details the structured AI prompts and iterations used throughout the development of the Task Tracker backend, categorized by specific features and system components.

---

## Feature 1: Core Data Models & Pydantic Validation
* *Objective:* Establish robust data validation structures for task items.
* *Prompt (User):* 
  > "Help me design the Pydantic BaseModels for a Task Tracker in FastAPI. The task needs a unique ID, a required title string, an optional description, a completion status boolean, an optional due date, and a list of string tags."
* *AI Output:* 
  * Generated the base schema using BaseModel, Optional, and Field with default factories for tags.
  * Human Review & Adjustment: Verified that the types align with Python typing conventions and database requirements.

---

## Feature 2: In-Memory Database & State Management
* *Objective:* Create a temporary storage mechanism to hold tasks during execution.
* *Prompt (User):* 
  > "How can I set up a simple in-memory list structure (tasks_db) in FastAPI to store, append, and retrieve task objects without a physical SQL database for this mid-term phase?"
* *AI Output:* 
  * Provided an in-memory Python list (tasks_db: List[Task] = []) and basic logic for appending new instances generated with unique identifiers.
  * Human Review & Adjustment: Ensured state persistence works smoothly across consecutive requests during local testing.

---

## Feature 3: Task Retrieval & Creation Endpoints (CRUD)
* *Objective:* Implement RESTful endpoints to fetch all tasks and create new ones.
* *Prompt (User):* 
  > "Write FastAPI route handlers for GET /tasks to return all tasks using a response model, and POST /tasks to validate and add a new task to our storage."
* *AI Output:* 
  * Generated routing code using @app.get("/tasks", response_model=...) and @app.post("/tasks", status_code=201).
  * Bug Fix / Iteration Note: The AI initially suggested Java/C#-style generics (List<Task>), which caused a Python SyntaxError. This was identified through terminal error logs and manually corrected to Python's standard List[Task].

---

## Feature 4: Advanced Filtering (Tags and Overdue Status)
* *Objective:* Add filtering capabilities to query tasks based on specific tags or whether they are overdue.
* *Prompt (User):* 
  > "Show me how to incorporate optional query parameters in FastAPI (get_tasks) to filter items by a specific tag string or an overdue boolean flag using Python's date library."
* *AI Output:* 
  * Suggested implementing query parameters using Optional[str] and Optional[bool], alongside conditional filtering loops checking against date.today().
  * Human Review & Adjustment: Integrated the date-handling logic safely to prevent comparison errors when due dates are null.

---

## Feature 5: Error Handling & Debugging Assistance
* *Objective:* Troubleshoot and fix module import blockages and internal server exceptions.
* *Prompt (User):* 
  > "The backend fails to start and gives a SyntaxError when trying to import main.py because of bracket syntax in type hints. How do I fix this type-hinting issue in Python?"
* *AI Output:* 
  * Explained the difference between runtime generic syntax and typing module annotations, instructing to replace angle brackets < > with square brackets [ ].
  * Human Review & Adjustment: Applied the fix globally across all route definitions, ensuring clean application startup and successful automated test execution.
