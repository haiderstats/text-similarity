from fastapi import FastAPI

# pylint has a bug where it doesn't fine BaseModel:
# https://github.com/samuelcolvin/pydantic/issues/1961
# pylint: disable=no-name-in-module
from pydantic import BaseModel

app = FastAPI()


class Texts(BaseModel):
    text1: str
    text2: str

    class Config:
        schema_extra = {
            "example": {
                "text1": "The cat in the hat scared a really big bat.",
                "text2": "The dog in the hat scared a really tiny frog.",
            }
        }


@app.post("/")
def text_similarity(texts: Texts) -> float:
    return 4.2
