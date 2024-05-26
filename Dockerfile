FROM python:3.12-slim
LABEL authors="wladbelsky"

COPY . /app

ENTRYPOINT ["python3", "/app/main.py"]