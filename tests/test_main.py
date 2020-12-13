from fastapi.testclient import TestClient

from text_similarity.main import app

client = TestClient(app)


def test_perfect_response():
    response = client.post(
        "/similarity", json={"text1": "A big brown cow.", "text2": "A big brown cow."}
    )
    assert response.status_code == 200
    assert response.json() == {"similarity": 1.0}


def test_perfect_0_response():
    response = client.post(
        "/similarity",
        json={"text1": "A big brown cow.", "text2": "A huge purple jellyfish?"},
    )
    assert response.status_code == 200
    assert response.json() == {"similarity": 0.0}


def test_sample_questions():
    response_1_2 = client.post(
        "/similarity",
        json={
            "text1": (
                "The easiest way to earn points with Fetch Rewards is to"
                "just shop for the products you already love. If you have"
                "any participating brands on your receipt, you'll get points"
                "based on the cost of the products. You don't need to clip"
                "any coupons or scan individual barcodes. Just scan each grocery"
                "receipt after you shop and we'll find the savings for you."
            ),
            "text2": (
                "The easiest way to earn points with Fetch Rewards is to just"
                "shop for the items you already buy. If you have any eligible"
                "brands on your receipt, you will get points based on the total"
                "cost of the products. You do not need to cut out any coupons"
                "or scan individual UPCs. Just scan your receipt after you"
                "check out and we will find the savings for you."
            ),
        },
    )
    assert response_1_2.status_code == 200

    response_1_3 = client.post(
        "/similarity",
        json={
            "text1": (
                "The easiest way to earn points with Fetch Rewards is to"
                "just shop for the products you already love. If you have"
                "any participating brands on your receipt, you'll get points"
                "based on the cost of the products. You don't need to clip"
                "any coupons or scan individual barcodes. Just scan each grocery"
                "receipt after you shop and we'll find the savings for you."
            ),
            "text2": (
                "We are always looking for opportunities for you to earn"
                "more points, which is why we also give you a selection of Special"
                "Offers. These Special Offers are opportunities to earn bonus points"
                "on top of the regular points you earn every time you purchase a participating"
                "brand. No need to pre-select these offers, we'll give you the points whether"
                "or not you knew about the offer. We just think it is easier that way."
            ),
        },
    )

    assert response_1_3.status_code == 200

    similarity_1_2 = response_1_2.json()
    similarity_1_3 = response_1_3.json()
    assert similarity_1_2["similarity"] > similarity_1_3["similarity"]


def test_ngram_fail_response():
    response = client.post(
        "/similarity?ngram_limit=0",
        json={
            "text1": "A big brown cow.",
            "text2": "A big brown cow.",
        },
    )
    assert response.status_code == 422
