from times import compute_overlap_time, time_range
import pytest

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected


def test_no_overlap():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    range2 = time_range("2010-01-12 11:00:00", "2010-01-12 11:30:00")
    
    assert compute_overlap_time(range1, range2) == []
    

def test_multiple_intervals_overlap():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 4)
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 3)

    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:50:00"),
        ("2010-01-12 10:50:00", "2010-01-12 11:00:00"),
        ("2010-01-12 11:00:00", "2010-01-12 11:10:00"),
        ("2010-01-12 11:10:00", "2010-01-12 11:30:00"),
    ]

    result = compute_overlap_time(range1, range2)
    assert result == expected, f"Expected {expected}, got {result}"


def test_touching_time_ranges_no_overlap():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00")

    expected = []  # No overlap because they only touch
    result = compute_overlap_time(range1, range2)

    assert result == expected, f"Expected no overlap, got {result}"


def test_backwards_time_range_raises_value_error():
    with pytest.raises(ValueError, match="end_time .* must be after start_time .*"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
