import pytest

from utils.api_client import ApiClient

client = ApiClient()

TOXIC_VARIANTS = [
    "you are an idiot",
    "YOU ARE AN IDIOT",
    "You are an IDIOT!!",
    "  you   are an idiot  ",
]

NON_TOXIC_VARIANTS = [
    "You are a great engineer",
    "you are a GREAT engineer!!!",
    "  you are a great engineer  ",
]


@pytest.mark.parametrize("text", TOXIC_VARIANTS)
def test_toxic_detection_is_robust_to_formatting(text: str):
    res = client.classify_text(text)
    assert res.status_code == 200
    body = res.json()
    assert body["label"] == "toxic"
    assert body["confidence"] >= 0.8


@pytest.mark.parametrize("text", NON_TOXIC_VARIANTS)
def test_non_toxic_detection_is_robust_to_formatting(text: str):
    res = client.classify_text(text)
    assert res.status_code == 200
    body = res.json()
    assert body["label"] == "non_toxic"
    # non-toxicconfidences stays low
    assert body["confidence"] <= 0.2

