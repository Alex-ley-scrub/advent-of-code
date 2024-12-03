"""
https://adventofcode.com/2024/day/3
"""

# Future imports (must occur at the beginning of the file):
from __future__ import annotations  # https://www.python.org/dev/peps/pep-0585/

# Standard library imports:
import os
import re

# https://adventofcode.com/2024/day/3/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT_P1 = (
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
)
TEST_INPUT_P2 = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)
TEST_OUTPUT_P1 = 161
TEST_OUTPUT_P2 = 48
ACTUAL_OUTPUT_P1 = 179571322
ACTUAL_OUTPUT_P2 = 103811193

MUL_REGEX = re.compile(r"mul\((\d+),(\d+)\)")
DO_REGEX = re.compile(r"do\(\)")
DO_NOT_REGEX = re.compile(r"don\'t\(\)")


def part_1(input_string: str):
    """https://adventofcode.com/2024/day/3#part1"""
    matches = MUL_REGEX.findall(input_string)
    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])
    return total


def part_2(input_string: str):
    """https://adventofcode.com/2024/day/3#part2"""
    # findall matches with indexes:
    mul_matches = [m for m in MUL_REGEX.finditer(input_string)]
    do_matches = [m for m in DO_REGEX.finditer(input_string)]
    do_not_matches = [m for m in DO_NOT_REGEX.finditer(input_string)]
    total = 0
    enabled = True
    all_matches = mul_matches + do_matches + do_not_matches
    all_matches.sort(key=lambda x: x.span())
    for match in all_matches:
        if match.group(0) == "do()":
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        if enabled and match.group(0).startswith("mul"):
            total += int(match.group(1)) * int(match.group(2))
    return total


def main():
    """https://adventofcode.com/2024/day/3"""
    with open(DATA_PATH, "r") as f:
        ACTUAL_INPUT = f.read()

    output = part_1(TEST_INPUT_P1)
    assert output == TEST_OUTPUT_P1, f"expected {TEST_OUTPUT_P1} but got {output}"
    print("test part 1:", output)

    output = part_1(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P1, f"expected {ACTUAL_OUTPUT_P1} but got {output}"
    print("actual part 1:", output)

    output = part_2(TEST_INPUT_P2)
    assert output == TEST_OUTPUT_P2, f"expected {TEST_OUTPUT_P2} but got {output}"
    print("test part 2:", output)

    output = part_2(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P2, f"expected {ACTUAL_OUTPUT_P2} but got {output}"
    print("actual part 2:", output)


if __name__ == "__main__":
    main()
