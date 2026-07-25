FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY services/api/pyproject.toml services/api/README.md /app/services/api/
COPY services/api/src /app/services/api/src

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir /app/services/api

EXPOSE 8000

CMD ["uvicorn", "equity_research_api.main:app", "--app-dir", "/app/services/api/src", "--host", "0.0.0.0", "--port", "8000"]

