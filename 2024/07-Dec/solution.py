"""
https://adventofcode.com/2024/day/7
"""

# Future imports (must occur at the beginning of the file):
from __future__ import annotations  # https://www.python.org/dev/peps/pep-0585/

# Standard library imports:
import os
import re
import time
import operator
import itertools
import functools
from typing import Callable

# Third party imports:
import pyperclip

# https://adventofcode.com/2024/day/7/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT_P1 = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
TEST_INPUT_P2 = TEST_INPUT_P1
TEST_OUTPUT_P1 = 3749
TEST_OUTPUT_P2 = 11387
ACTUAL_OUTPUT_P1 = 1620690235709
ACTUAL_OUTPUT_P2 = 145397611075341


def get_total_bags(input_string: str, allowed_operators: list[Callable]):
    """https://adventofcode.com/2024/day/7"""
    calibrations = [row.split(": ") for row in input_string.strip().split("\n")]
    total = 0
    for target_str, calibration_str in calibrations:
        target = int(target_str)
        numbers = list(map(int, calibration_str.split()))
        num_operators = len(numbers) - 1
        all_operators = list(itertools.product(allowed_operators, repeat=num_operators))
        # print(numbers, num_operators, all_operators)
        for operators in all_operators:
            result = numbers[0]
            for i, op in enumerate(operators):
                result = op(result, numbers[i + 1])
                if result > target:
                    break
            if result == target:
                total += target
                break
    return total


def part_1(input_string: str):
    """https://adventofcode.com/2024/day/7#part1"""
    return get_total_bags(input_string, [operator.add, operator.mul])


def part_2(input_string: str):
    """https://adventofcode.com/2024/day/7#part2"""
    concat = lambda x, y: int(str(x) + str(y))
    return get_total_bags(input_string, [operator.add, operator.mul, concat])


def main():
    """https://adventofcode.com/2024/day/7"""
    with open(DATA_PATH, "r") as f:
        ACTUAL_INPUT = f.read()

    t_start = time.time()
    output = part_1(TEST_INPUT_P1)
    t_end = time.time()
    assert output == TEST_OUTPUT_P1, f"expected {TEST_OUTPUT_P1} but got {output}"
    print("test part 1:", output)
    print(f"time: {t_end - t_start:.3f} sec")

    t_start = time.time()
    output = part_1(ACTUAL_INPUT)
    t_end = time.time()
    assert output == ACTUAL_OUTPUT_P1, f"expected {ACTUAL_OUTPUT_P1} but got {output}"
    print("actual part 1:", output)
    print(f"time: {t_end - t_start:.3f} sec")
    pyperclip.copy(output)

    t_start = time.time()
    output = part_2(TEST_INPUT_P2)
    t_end = time.time()
    assert output == TEST_OUTPUT_P2, f"expected {TEST_OUTPUT_P2} but got {output}"
    print("test part 2:", output)
    print(f"time: {t_end - t_start:.3f} sec")

    t_start = time.time()
    output = part_2(ACTUAL_INPUT)
    t_end = time.time()
    assert output == ACTUAL_OUTPUT_P2, f"expected {ACTUAL_OUTPUT_P2} but got {output}"
    print("actual part 2:", output)
    print(f"time: {t_end - t_start:.3f} sec")
    pyperclip.copy(output)


if __name__ == "__main__":
    main()
