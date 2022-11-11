.PHONY: lint format test typecheck format-check

lint:
		poetry run pflake8 .

format:
		poetry run black .

format-check:
		poetry run black . --check

test:
		poetry run pytest

typecheck:
		poetry run mypy .
