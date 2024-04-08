from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


class Emoji(BaseModel):
    value: str = Field(description="The emoji value")


def output_parser() -> PydanticOutputParser:
    return PydanticOutputParser(pydantic_object=Emoji)
