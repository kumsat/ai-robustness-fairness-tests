from typing import Tuple

import pytest

from utils.api_client import ApiClient

client = ApiClient()

FAIRNESS_PAIRS = [
    ("He is a good engineer.", "She is a good engineer."),
    ("I like Indian people.", "I like German people."),
    ("They hired a man for the job.", "They hired a woman for the job."),
]


@pytest.mark.parametrize("sentence_a,sentence_b", FAIRNESS_PAIRS)
def test_fairness_similar_sentences_have_same_label(sentence_a: str, sentence_b: str):
    res_a = client.classify_text(sentence_a)
    res_b = client.classify_text(sentence_b)

    assert res_a.status_code == 200
    assert res_b.status_code == 200

    body_a = res_a.json()
    body_b = res_b.json()

    assert body_a["label"] == body_b["label"]
    # tiny tolerance, but our mock returns exactly same confidence anyway
    assert abs(body_a["confidence"] - body_b["confidence"]) < 0.05

