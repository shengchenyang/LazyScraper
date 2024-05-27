.PHONY: start dev check

start:
	pip install poetry
	poetry install
	pre-commit install

dev:
	poetry install

git:
	git config --global core.eol lf
	git config --global core.autocrlf input
	git config --global core.safecrlf true

check:
	pre-commit run --all-files
