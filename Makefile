install:
	poetry install

lint:
	poetry run flake8 src tests

test-cov:
	poetry run pytest --cov-report xml --cov=src tests/  