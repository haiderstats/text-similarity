from typing import Dict

from fastapi import FastAPI, Query

from text_similarity.similarity import Texts

app = FastAPI()


@app.post("/")
def text_similarity(
    texts: Texts,
    ngram_limit: int = Query(
        3, description="The highest ngram used for comparision.", gt=0, le=5
    ),
) -> Dict[str, float]:
    return {"similarity": texts.similarity(ngram_limit)}
