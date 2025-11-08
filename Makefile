.PHONY: install-deps
install-deps:
	poetry install

.PHONY: lint
lint: install-deps  ## Run all code linters
	poetry run docformatter -r .
	poetry run black --diff --check .
	poetry run isort --skip docker --profile black --diff --check .
	poetry run bandit -r src -c pyproject.toml
	poetry run pylint src
	poetry run flake8 .
	poetry run mypy src
	poetry run vulture --min-confidence 100 .

.PHONY: format
format: install-deps  ## Run all code formatters
	poetry run docformatter --in-place -r .
	poetry run isort --skip docker --profile black .
	poetry run black .

.PHONY: test
test: install-deps
	poetry run pytest -s -v --cov tests/