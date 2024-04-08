import logging

import typer

from emoji_suggestor import __version__, commands

logger = logging.getLogger("emoji_suggestor")
handler = logging.StreamHandler()
format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(format)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


app = typer.Typer(
    help="🧰 Input text, get emoji suggestions",
    no_args_is_help=True,
)


@app.callback()
def main(trace: bool = typer.Option(False, help="Enable debug logging.")):
    if trace:
        logger.setLevel(logging.DEBUG)


@app.command(
    short_help="📌 Displays the current version number of the emoji_suggestor library"
)
def version():
    print(__version__)


@app.command(
    name="suggest",
    help="Suggestions for emojis based on input text",
    no_args_is_help=True,
)
def _suggest(
    question: str = typer.Argument(
        ..., help="The input text for which to suggest an emoji."
    )
):
    logger.debug(f"emoji_suggestor version={__version__}")
    print(commands.text_2_emoji(question))


def entrypoint():
    # NB: need to do this because Databricks has its own method for shutting down.
    #  click, typer etc. raise sys.exit(0) which causes the DB job to fail.
    #  see e.g. https://tinyurl.com/5h4avuvc
    try:
        app()
    except SystemExit as e:
        if e.code != 0:
            raise
