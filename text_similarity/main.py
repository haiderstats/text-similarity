from typing import Dict

from fastapi import FastAPI

from text_similarity.similarity import Texts

app = FastAPI()


@app.post("/")
def text_similarity(texts: Texts) -> Dict[str, float]:
    return {"similarity": texts.similarity()}
