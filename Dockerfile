FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src
COPY mlflow-artifacts /app/mlflow-artifacts
COPY data /app/data


CMD ["python", "src/app.py"]
