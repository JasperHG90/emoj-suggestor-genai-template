alias s := setup
alias e := example

install:
    poetry install

pre_commit:
    poetry run pre-commit install

setup: install pre_commit

example:
    poetry run emoji_suggestor suggest "How do I make apple pie?"
