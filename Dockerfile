# Dockerfile:moveie-new
# Author:(Alireza Ghaderi)

FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY . /app

COPY pyproject.toml poetry.lock ./app/

RUN poetry install --no-root --no-interaction

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
