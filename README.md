# Text Similarity


## What is this?

This repository provides a basic way to compare the similarity of two sentences. To measure the similarity I used the [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) between the two word vectors using n-grams. An n-gram is a sequence of n items from a text. For example, given the sentence `The cat in the hat` we have `["the", "cat", "in", "the", "hat"]` as the list of unigrams and `["the cat", "cat in", "in the", "the hat"]` as the set of bigrams. The code in the repository breaks sentences into ngrams (trigrams by default) and gets the cosine similarity between the two word vectors.

This is a pretty simplistic way of comparing two sentences since it only measures the lexical similarity (the same words used in two sentences) as opposed to the semantic similarity (the meaning of the two sentences). That is, the similarity metric given here will suggest that `A big feline` and `A huge cat` will have a similarity of 0.0 since different words are used (and since `A` is removed due to being a stop word). 

The similarity metric is exposed using FastAPI and also Dockerized for your convience. See below for usage instructions.

## Build it yourself:

Clone the repository and move directories:  
```bash
git clone git@github.com:haiderstats/text-similarity.git && cd text-similarity
```

Build the Docker image (make sure you have [Docker installed](https://www.docker.com/)): 

```bash
docker build -t text_similarity:latest .
```

Put the Docker container on your desired port (here we use 26915):

```bash
docker run --name text_similarity -p 26915:8000 text_similarity:latest
```
**_Note_**: Feel free to add a `-d` flag to run the container in detached mode.


Now you should have the text similarity function running locally! Go to http://127.0.0.1:26915/docs to see the swagger docs and checkout the `/similarity` route! Alternatively you can install the `requests` module and run the below python code to send a `POST` request.

```python
import requests

url = "http://127.0.0.1:26915/similarity" #Change this to "http://127.0.0.1:26915/similarity?ngram_limit=1" for the unigram similarity! 
texts = {
    "text1": "The cat in the hat scared a really big bat",
    "text2": "The dog in the hat scared a really tiny frog.",
}

response = requests.post(url, json=texts)
print(response.status_code)
print(response.json())
```
