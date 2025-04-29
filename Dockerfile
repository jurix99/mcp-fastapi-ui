# Install uv
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN pip install mcpo

WORKDIR /app

COPY pyproject.toml ./
COPY ./app ./app


RUN uv pip install . --system

CMD ["uvx", "mcpo", "--host", "0.0.0.0", "--port", "8000", "--" ,"uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
    