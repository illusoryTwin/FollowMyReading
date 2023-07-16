from enum import Enum
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse


class file_with_body(BaseModel):
    file: FileResponse
    original_strings: list
    audio_transcription: list

    class Config:
        arbitrary_types_allowed = True


class orig_strings_and_transcription(str, Enum):
    true = "yes"
    false = "no"


class Language(str, Enum):
    ru = "russian"
    ara = "arabic"
    eng = "english"
