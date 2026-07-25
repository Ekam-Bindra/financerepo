SHELL := /bin/sh

PYTHON ?= python3.12
VENV ?= .venv
PNPM ?= pnpm
COMPOSE ?= docker compose

.PHONY: setup install install-web install-api dev dev-web dev-api down format format-check lint typecheck test test-integration build check clean

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(MAKE) install

install: install-web install-api

install-web:
	$(PNPM) install --frozen-lockfile

install-api:
	$(VENV)/bin/python -m pip install -e "services/api[dev]"

dev:
	$(COMPOSE) up --build

dev-web:
	$(PNPM) --filter @equity-research/web dev

dev-api:
	$(VENV)/bin/uvicorn equity_research_api.main:app --app-dir services/api/src --reload --host 0.0.0.0 --port 8000

down:
	$(COMPOSE) down

format:
	$(PNPM) -r format
	$(VENV)/bin/ruff format services/api

format-check:
	$(PNPM) -r format
	$(VENV)/bin/ruff format --check services/api

lint:
	$(PNPM) -r lint
	$(VENV)/bin/ruff check services/api

typecheck:
	$(PNPM) -r typecheck
	$(VENV)/bin/mypy --config-file services/api/pyproject.toml services/api/src services/api/tests

test:
	$(PNPM) -r test
	$(VENV)/bin/pytest services/api/tests

test-integration:
	$(VENV)/bin/pytest tests/integration

build:
	$(PNPM) -r build

check: format-check lint typecheck test build

clean:
	$(COMPOSE) down --volumes --remove-orphans
