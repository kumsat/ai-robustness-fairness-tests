from utils.api_client import ApiClient

client = ApiClient()


def test_missing_text_field_returns_400():
    # Send empty JSON
    res = client.classify_text(text=None)  # our client always sends {"text": value}
    assert res.status_code == 400 or res.status_code == 422


def test_empty_string_returns_400():
    res = client.classify_text("")
    assert res.status_code == 400

