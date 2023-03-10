.PHONY: run-server
run-server:
	poetry run python seven_wonders_guide/manage.py runserver 8000

.PHONY: install
install:
	poetry install --without dev

.PHONY: install-dev
install-dev:
	poetry install

.PHONY: tests
tests:
	poetry run python -m unittest discover
