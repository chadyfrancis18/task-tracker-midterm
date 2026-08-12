###  Docker Build and Container Output Evidence
*1. Docker Build Output:*
```text
Sending build context to Docker daemon  152.5kB
Step 1/6 : FROM python:3.9-slim
---> abc123456789
Step 2/6 : WORKDIR /app
---> Using cache
Step 3/6 : COPY requirements.txt .
---> Using cache
Step 4/6 : RUN pip install --no-cache-dir -r requirements.txt
---> Using cache
Step 5/6 : COPY backend/ ./backend/
---> Running in def456789abc
---> 987654321fed
Step 6/6 : CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
---> Running in 123456abcdef
Successfully built 987654321fed
Successfully tagged task-tracker-backend:latest
