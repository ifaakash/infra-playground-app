# Lock python image by using SHA
FROM python:3.12-slim@sha256:4600f71648e110b005bf7bca92dbb335e549e6b27f2e83fceee5e11b3e1a4d01

# Initialise working directory
WORKDIR /app/infra_playground_app

# Install all packages from requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY app.py .

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
