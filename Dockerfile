FROM python:3.10-slim

# Create a non-root user for security compliance
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code into the container
COPY backend/ ./backend/

# Switch to the non-root user
USER appuser

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
