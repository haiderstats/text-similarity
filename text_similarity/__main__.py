import uvicorn  # type: ignore


def main():
    uvicorn.run("text_similarity.main:app", port=8000, log_level="info")


if __name__ == "__main__":
    main()
