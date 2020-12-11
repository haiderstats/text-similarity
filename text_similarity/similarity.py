# pylint has a bug where it doesn't fine BaseModel:
# https://github.com/samuelcolvin/pydantic/issues/1961
# pylint: disable=no-name-in-module
from typing import Dict, List, Tuple

from pydantic import BaseModel

from text_similarity.common import STOP_WORDS


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

    def word_counter(self) -> Tuple[Dict[str, int], Dict[str, int]]:
        text1_words = word_counter(self.text1)
        text2_words = word_counter(self.text2)
        return text1_words, text2_words


def cosine_similarity(vector_1: List[int], vector_2: List[int]) -> float:
    numerator = 0.0
    normalized_a = 0.0
    normalized_b = 0.0

    for a, b in zip(vector_1, vector_2):
        numerator += a * b
        normalized_a += a ** 2
        normalized_b += b ** 2

    normalized_a = normalized_a ** 0.5
    normalized_b = normalized_b ** 0.5

    denominator = normalized_a * normalized_b
    if denominator == 0:
        return 0.0

    return numerator / denominator


def word_counter(text: str, ngrams: int = 3) -> Dict[str, int]:
    word_list = text.lower().translate({ord("."): " .", ord("?"): " ?"}).split(" ")
    word_list = [word for word in word_list if word not in STOP_WORDS]

    word_counts: Dict[str, int] = {}
    for index, word in enumerate(word_list):
        word_counts[word] = word_counts.get(word, 0) + 1
        for n in range(1, ngrams):
            try:
                word = word + " " + word_list[index + n]
                word_counts[word] = word_counts.get(word, 0) + 1
            except IndexError:
                break

    return word_counts
