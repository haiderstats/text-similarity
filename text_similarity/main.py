from fastapi import FastAPI

from text_similarity.similarity import Texts

app = FastAPI()


@app.post("/")
def text_similarity(texts: Texts) -> float:
    return 4.2
