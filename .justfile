install-precommit:
    pre-commit install

# Poetry

install-virtualenv:
    poetry install

poetry-lock:
    poetry lock

# Python ci

run-black:
    poetry run black src --check
    poetry run black tests --check

run-flake8:
    poetry run flake8 src
    poetry run flake8 tests

run-isort:
    poetry run isort src --check
    poetry run isort tests --check

run-ci: run-black run-isort run-flake8

run-pytest:
    PYTHONPATH=disney_precommit_sql_file poetry run pytest
