from emoji_suggestor.processing import Text2Emoji


def text_2_emoji(question: str) -> str:
    model = Text2Emoji()
    return model(question)
