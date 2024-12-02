"""
https://adventofcode.com/2024/day/1
"""

# Future imports (must occur at the beginning of the file):
from __future__ import annotations  # https://www.python.org/dev/peps/pep-0585/

# Standard library imports:
import os
from collections import Counter

# https://adventofcode.com/2024/day/1/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""
TEST_OUTPUT_P1 = 11
TEST_OUTPUT_P2 = 31


def get_total_distance(input_string: str) -> int:
    """https://adventofcode.com/2024/day/1#part1"""
    lines = input_string.strip().split("\n")
    left_locs: list[int] = []
    right_locs: list[int] = []
    for line in lines:
        left, right = map(int, line.split())
        left_locs.append(left)
        right_locs.append(right)
    left_locs.sort()
    right_locs.sort()
    distances = [abs(left - right) for left, right in zip(left_locs, right_locs)]
    return sum(distances)


def get_similarity_score(input_string: str) -> int:
    """https://adventofcode.com/2024/day/1#part2"""
    lines = input_string.strip().split("\n")
    left_locs: Counter[int] = Counter()
    right_locs: Counter[int] = Counter()
    for line in lines:
        left, right = map(int, line.split())
        left_locs.setdefault(left, 0)
        left_locs[left] += 1
        right_locs.setdefault(right, 0)
        right_locs[right] += 1
    similarity_scores = [k * v * right_locs.get(k, 0) for k, v in left_locs.items()]
    return sum(similarity_scores)


def main():
    with open(DATA_PATH, "r") as f:
        ACTUAL_INPUT = f.read()

    output = get_total_distance(TEST_INPUT)
    assert output == TEST_OUTPUT_P1, f"expected {TEST_OUTPUT_P1} but got {output}"
    print("test part 1:", output)

    output = get_total_distance(ACTUAL_INPUT)
    assert output == 2031679, f"expected 2031679 but got {output}"
    print("actual part 1:", output)

    output = get_similarity_score(TEST_INPUT)
    assert output == TEST_OUTPUT_P2, f"expected {TEST_OUTPUT_P2} but got {output}"
    print("test part 2:", output)

    output = get_similarity_score(ACTUAL_INPUT)
    assert output == 19678534, f"expected 19678534 but got {output}"
    print("actual part 2:", output)


if __name__ == "__main__":
    main()
