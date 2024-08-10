FROM python:3.9-slim

WORKDIR /C:/Users/manis/Documents/GitHub/MLOPSAssignment1/mlopsassignement1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /C:/Users/manis/Documents/GitHub/MLOPSAssignment1/mlopsassignement1/

EXPOSE 5002

CMD ["python", "app.py"]
