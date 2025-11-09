import times
from unittest.mock import patch


@patch("times.requests.get")
def test_iss_passes(mock_get):
    # ---- Fake API response ----
    fake_json = {
        "passes": [
            {"startUTC": 1706827200, "endUTC": 1706827500},  # Example timestamps
        ]
    }

    mock_get.return_value.json.return_value = fake_json

    # ---- Call the function ----
    result = times.iss_passes(56, 0, api_key="FAKE_KEY")

    # ---- Assertions ----
    assert len(result) == 1
    assert "→" in result[0]            # formatted output
    mock_get.assert_called_once()      # ensure request was made
