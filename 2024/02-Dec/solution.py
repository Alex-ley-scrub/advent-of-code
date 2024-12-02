"""
https://adventofcode.com/2024/day/2
"""

# Future imports (must occur at the beginning of the file):
from __future__ import annotations  # https://www.python.org/dev/peps/pep-0585/

# Standard library imports:
import os


# https://adventofcode.com/2024/day/2/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
TEST_OUTPUT_P1 = 2
TEST_OUTPUT_P2 = 4
ACTUAL_OUTPUT_P1 = 236
ACTUAL_OUTPUT_P2 = 308


def is_report_safe(report: str) -> bool:
    """https://adventofcode.com/2024/day/2#part1"""
    values = [int(x) for x in report.split()]
    all_deltas = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    if all(delta >= 1 and delta <= 3 for delta in all_deltas):
        return True
    if all(delta >= -3 and delta <= -1 for delta in all_deltas):
        return True
    return False


def get_total_safe_reports(input_string: str) -> int:
    """https://adventofcode.com/2024/day/2#part1"""
    reports = input_string.strip().split("\n")
    return sum(is_report_safe(report) for report in reports)


def is_report_safe_with_dampener(report: str) -> bool:
    """https://adventofcode.com/2024/day/2#part2"""
    values = [int(x) for x in report.split()]
    is_safe = is_report_safe(report)
    if is_safe:
        return True
    # if we remove 1 element, and it is safe, then the report is safe
    for i in range(len(values)):
        new_values = values[:i] + values[i + 1 :]
        is_safe = is_report_safe(" ".join(map(str, new_values)))
        if is_safe:
            return True
    return False


def get_total_safe_reports_with_dampener(input_string: str) -> int:
    """https://adventofcode.com/2024/day/2#part2"""
    reports = input_string.strip().split("\n")
    return sum(is_report_safe_with_dampener(report) for report in reports)


def main():
    """https://adventofcode.com/2024/day/2"""
    with open(DATA_PATH, "r") as f:
        ACTUAL_INPUT = f.read()

    output = get_total_safe_reports(TEST_INPUT)
    assert output == TEST_OUTPUT_P1, f"expected {TEST_OUTPUT_P1} but got {output}"
    print("test part 1:", output)

    output = get_total_safe_reports(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P1, f"expected {ACTUAL_OUTPUT_P1} but got {output}"
    print("actual part 1:", output)

    output = get_total_safe_reports_with_dampener(TEST_INPUT)
    assert output == TEST_OUTPUT_P2, f"expected {TEST_OUTPUT_P2} but got {output}"
    print("test part 2:", output)

    output = get_total_safe_reports_with_dampener(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P2, f"expected {ACTUAL_OUTPUT_P2} but got {output}"
    print("actual part 2:", output)


if __name__ == "__main__":
    main()
