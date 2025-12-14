.PHONY: install-deps
install-deps:
	poetry install

.PHONY: lint
lint: install-deps
	poetry run docformatter -r .
	poetry run black --diff --check .
	poetry run ruff check .
	poetry run mypy src/
	poetry run bandit -r src/ -c pyproject.toml
	poetry run vulture --min-confidence 100 .

.PHONY: format
format: install-deps  ## Run all code formatters
	poetry run docformatter --in-place -r .
	poetry run black .
	poetry run ruff check . --fix

.PHONY: test
test: install-deps
	poetry run pytest -s -v --cov tests/