import pytest
from times import compute_overlap_time, time_range

# Parametrize for the valid test cases
@pytest.mark.parametrize("range1, range2, expected",
    [
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
            time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
            [("2010-01-12 10:30:00", "2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
        ),
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00"),
            time_range("2010-01-12 11:00:00", "2010-01-12 11:30:00"),
            []
        ),
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 4),
            time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 3),
            [
                ("2010-01-12 10:30:00", "2010-01-12 10:50:00"),
                ("2010-01-12 10:50:00", "2010-01-12 11:00:00"),
                ("2010-01-12 11:00:00", "2010-01-12 11:10:00"),
                ("2010-01-12 11:10:00", "2010-01-12 11:30:00"),
            ]
        ),
        (
            time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00"),
            time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00"),
            []
        ),
    ]
)
def test_generic_case(range1, range2, expected):
    result = compute_overlap_time(range1, range2)
    assert result == expected, f"Expected {expected}, got {result}"

# Test case for invalid time range (start_time > end_time) raising a ValueError
def test_backwards_time_range_raises_value_error():
    with pytest.raises(ValueError, match="end_time .* must be after start_time .*"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
