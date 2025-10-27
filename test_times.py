from times import compute_overlap_time, time_range

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
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 4)  # Range 1: 10:00 - 12:00, 4 intervals
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 3)  # Range 2: 10:30 - 11:30, 3 intervals
    
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),  # 1st overlap
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),  # 2nd overlap
        ("2010-01-12 10:45:00", "2010-01-12 10:52:00"),  # 3rd overlap
        ("2010-01-12 10:53:00", "2010-01-12 11:00:00")   # 4th overlap
    ]
    
    assert compute_overlap_time(range1, range2) == expected
