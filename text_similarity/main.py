from typing import Dict

from fastapi import FastAPI, Query

from text_similarity.similarity import Texts

app = FastAPI()


@app.post("/similarity")
def text_similarity(
    texts: Texts,
    ngram_limit: int = Query(
        3, description="The highest ngram used for comparision.", ge=1, le=5
    ),
) -> Dict[str, float]:
    return {"similarity": texts.similarity(ngram_limit)}
