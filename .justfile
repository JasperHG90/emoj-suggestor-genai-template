alias s := setup

install:
    poetry install

pre_commit:
    poetry run pre-commit install

setup: install pre_commit
