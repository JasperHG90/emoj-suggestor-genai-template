import logging
import os

from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI

from emoji_suggestor.const import TEMPLATE


class Text2Emoji:

    def __init__(self):
        self.logger = logging.getLogger("emoji_suggestor.processing.Text2Emoji")
        self.prompt = PromptTemplate(
            template=TEMPLATE.strip(), input_variables=["question"]
        )
        self.logger.debug(f"Using template:\n {self.prompt.template}")
        self.logger.debug(
            f"Using model deployment: {os.environ['AZURE_OPENAI_MODEL_NAME']}"
        )
        self.model = AzureChatOpenAI(
            azure_deployment=os.environ["AZURE_OPENAI_MODEL_NAME"], temperature=1.0
        )
        self.chain = self.prompt | self.model

    def __call__(self, question: str) -> str:
        self.logger.debug(f"Processing question: {question}")
        out = self.chain.invoke({"input": question})
        content = out.content.strip()
        self.logger.debug(f"Output: {content}")
        return content
