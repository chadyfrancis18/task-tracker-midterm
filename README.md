# Task Tracker Midterm Project

A full-stack task management application built with FastAPI, HTML/JS frontend, and tested using Pytest, featuring custom due date tracking and tag categorization.

## Project Structure
- backend/: Contains the FastAPI application (main.py) with CRUD endpoints and advanced filter logic.
- frontend/: Contains the user interface (index.html) to interact with tasks and filters.
- tests/: Contains automated test cases (test_main.py).
- docs/: Contains project documentation deliverables (User Stories, Mini-ADR, Prompt Log, Verification, and Reflection).

## How to Run
Install dependencies:
   ```bash
   pip install -r requirements.txt
uvicorn backend.main:app --reload
pytest
