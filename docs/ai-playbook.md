# AI Development Playbook

## 1. Overview
This playbook defines the standard practices, guardrails, and iterative workflows for integrating AI assistance into the Task Tracker project development lifecycle.

## 2. Prompt Engineering Standards
* *Contextual Prompting:* Always provide clear file paths, framework versions (FastAPI, Python), and specific error logs when asking the AI for assistance.
* *Scope Limitation:* Ask the AI to generate small, modular functions or fixes rather than entire application monoliths to maintain tight control over the codebase.

## 3. Review & Verification Workflow
1. *Generation:* AI generates a code snippet, refactoring suggestion, or test case.
2. *Manual Inspection:* Developer reviews the code line-by-line for security flaws, hardcoded credentials, or logic bugs.
3. *Automated Testing:* Run pytest -v locally and through CI pipelines to verify functionality.
4. *Integration:* Only merge changes into the repository branch after tests pass successfully.

## 4. Security & Safety Guardrails
* Never paste production API keys, database credentials, or sensitive secrets into AI prompt interfaces.
* Treat all AI-generated authentication or authorization logic as untrusted until thoroughly vetted manually
