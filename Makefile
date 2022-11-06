.PHONY: lint format test typecheck

lint:
		poetry run pflake8 .

format:
		poetry run black .

test:
		poetry run pytest

typecheck:
		poetry run mypy .
