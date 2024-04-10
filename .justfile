alias s := setup
alias e := example

install:
    poetry install -E openai -E vertexai --with dev

pre_commit:
    poetry run pre-commit install

setup: install pre_commit

example:
    poetry run emojifi text "How do I make apple pie?"
