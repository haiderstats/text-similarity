from fastapi.testclient import TestClient

from text_similarity.main import app

client = TestClient(app)


def test_perfect_response():
    response = client.post(
        "/", json={"text1": "A big brown cow.", "text2": "A big brown cow."}
    )
    assert response.status_code == 200
    assert response.json() == {"similarity": 1.0}


def test_perfect_0_response():
    response = client.post(
        "/", json={"text1": "A big brown cow.", "text2": "A huge purple jellyfish?"}
    )
    assert response.status_code == 200
    assert response.json() == {"similarity": 0.0}
