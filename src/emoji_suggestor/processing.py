import logging
import os
import typing

from langchain_core.prompts import PromptTemplate

# NB: these are extras
try:
    _has_openai = True
    from langchain_openai import AzureChatOpenAI
except ImportError:
    _has_openai = False
try:
    _has_vertexai = True
    from langchain_google_vertexai import ChatVertexAI
except ImportError:
    _has_vertexai = False

from emoji_suggestor.const import TEMPLATE
from emoji_suggestor.types import output_parser


def _get_model(
    service: str, **model_kwargs
) -> typing.Union[AzureChatOpenAI, ChatVertexAI]:
    if service == "openai":
        if _has_openai:
            return AzureChatOpenAI(**model_kwargs)
        else:
            raise ValueError(
                "OpenAI service is not available. Please install this library using the 'emoji_suggestor[openai]' extra."
            )
    elif service == "vertexai":
        if _has_vertexai:
            return ChatVertexAI(**model_kwargs)
        else:
            raise ValueError(
                "VertexAI service is not available. Please install this library using the 'emoji_suggestor[vertexai]' extra."
            )
    else:
        raise ValueError(f"Unknown service: {service}")


class Text2Emoji:

    def __init__(self):
        self.logger = logging.getLogger("emoji_suggestor.processing.Text2Emoji")
        self.parser = output_parser()
        self.prompt = PromptTemplate(
            template=TEMPLATE.strip(),
            input_variables=["question"],
            partial_variables={
                "format_instructions": self.parser.get_format_instructions()
            },
        )
        self.logger.debug(f"Using template:\n {self.prompt.template}")
        self.logger.debug(
            f"Using model deployment: {os.environ['AZURE_OPENAI_MODEL_NAME']}"
        )
        self.model = _get_model(
            service="openai",
            azure_deployment=os.environ["AZURE_OPENAI_MODEL_NAME"],
            temperature=1.0,
        )
        self.chain = self.prompt | self.model | self.parser

    def __call__(self, question: str) -> str:
        self.logger.debug(f"Processing question: {question}")
        out = self.chain.invoke({"input": question})
        content = out.value
        self.logger.debug(f"Output: {content}")
        return content
