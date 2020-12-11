from text_similarity.similarity import cosine_similarity, word_counter


def test_cosine_perfect():
    vector_1 = [1, 0, 0, 1, 5]
    vector_2 = [1, 0, 0, 1, 5]
    assert cosine_similarity(vector_1, vector_2) == 1.0


def test_cosine_perfect_0():
    vector_1 = [1, 0, 0, 1, 5]
    vector_2 = [0, 100, 10, 0, 0]
    assert cosine_similarity(vector_1, vector_2) == 0.0


def test_cosine_real_values():
    vector_1 = [3, 8, 7, 5, 2, 9]
    vector_2 = [10, 8, 6, 6, 4, 5]
    assert cosine_similarity(vector_1, vector_2) == 0.864


# pylint: disable=expression-not-assigned
def test_word_counter():
    text = "A big big cow."
    words = word_counter(text)
    assert "a" not in words
    words.get("big") == 2
    words.get("cow") == 1


# An empty string should still be similar to an empty string
def test_word_counter_empty():
    text = ""
    words = word_counter(text)
    assert words == {"": 1}
