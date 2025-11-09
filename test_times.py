import pytest
import yaml
from pathlib import Path
from times import time_range, compute_overlap_time


def load_yaml_cases():
    # Resolve path relative to this test file
    yaml_file = Path(__file__).parent / "fixture.yaml"

    with open(yaml_file, "r") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def yaml_cases():
    return load_yaml_cases()


@pytest.mark.parametrize("case_index", range(len(load_yaml_cases())))
def test_generic_cases(case_index, yaml_cases):
    case = yaml_cases[case_index]

    tr1_args = case["time_range_1"]
    tr2_args = case["time_range_2"]

    range1 = time_range(
        tr1_args["start"],
        tr1_args["end"],
        tr1_args.get("number_of_intervals", 1),
        tr1_args.get("gap_between_intervals_s", 0)
    )

    range2 = time_range(
        tr2_args["start"],
        tr2_args["end"],
        tr2_args.get("number_of_intervals", 1),
        tr2_args.get("gap_between_intervals_s", 0)
    )

    expected = [tuple(e) for e in case["expected"]]
    result = compute_overlap_time(range1, range2)

    assert result == expected, f"Case '{case['name']}' failed."


def test_backwards_time_range_raises_value_error():
    with pytest.raises(ValueError, match="end_time .* must be after start_time .*"):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
