import uvicorn  # type: ignore


def main():
    uvicorn.run("text_similarity.main:app", host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    main()
