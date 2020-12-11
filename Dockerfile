FROM python:3.6-buster

RUN pip install poetry

WORKDIR "/usr/src/app"

COPY pyproject.toml poetry.lock ./
COPY text_similarity text_similarity

RUN poetry build --format wheel
RUN pip install --no-cache-dir dist/* && rm -rf dist

CMD ["text_similarity"]
