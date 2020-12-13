FROM python:3.6-buster as builder

RUN pip install poetry

WORKDIR "/usr/src/app"

COPY pyproject.toml poetry.lock ./
COPY text_similarity text_similarity

RUN poetry build --format wheel

FROM python:3.6-buster

WORKDIR "/usr/src/app"

COPY --from=builder /usr/src/app/dist/ /tmp/dist/

RUN pip install --no-cache-dir /tmp/dist/* && rm -rf dist

CMD ["text_similarity"]
