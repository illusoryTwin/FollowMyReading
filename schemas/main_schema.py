from pydantic import BaseModel, Field


class sentences_list(BaseModel):
    sentences: list = Field(examples=[["Hello!", "My name is John."]])
