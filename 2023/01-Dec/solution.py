"""
https://adventofcode.com/2023/day/1
"""

# Future imports (must occur at the beginning of the file):
from __future__ import annotations  # https://www.python.org/dev/peps/pep-0585/

# Standard library imports:
import os
import re

# https://adventofcode.com/2023/day/1/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT_P1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
TEST_OUTPUT_P1 = 142
TEST_INPUT_P2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
TEST_OUTPUT_P2 = 281
ACTUAL_OUTPUT_P1 = 54940
ACTUAL_OUTPUT_P2 = 54208


def get_calibration_int(calibration_string: str):
    """https://adventofcode.com/2023/day/1#part1"""
    regex = re.compile(r"\d")
    matches = regex.findall(calibration_string)
    return int(matches[0] + matches[-1])


def get_sum_of_calibration_ints(input_str: str):
    """https://adventofcode.com/2023/day/1#part1"""
    calibration_strings = input_str.strip().split("\n")
    calibration_values = [get_calibration_int(s) for s in calibration_strings if s]
    return sum(calibration_values)


def replace_words_with_numbers(input_string: str):
    """https://adventofcode.com/2023/day/1#part2"""
    return (
        input_string.replace("one", "1")
        .replace("two", "2")
        .replace("three", "3")
        .replace("four", "4")
        .replace("five", "5")
        .replace("six", "6")
        .replace("seven", "7")
        .replace("eight", "8")
        .replace("nine", "9")
    )


def get_calibration_value(calibration_string: str):
    """https://adventofcode.com/2023/day/1#part2"""
    # get overlapping matches by using a capturing group inside a lookahead
    # https://stackoverflow.com/a/70979561/9792594
    regex = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")
    matches = regex.findall(calibration_string)
    values = [replace_words_with_numbers(s) for s in matches]
    return int(values[0] + values[-1])


def get_sum_of_calibration_values(input_str: str):
    """https://adventofcode.com/2023/day/1#part2"""
    calibration_strings = input_str.strip().split("\n")
    calibration_values = [get_calibration_value(s) for s in calibration_strings if s]
    return sum(calibration_values)


def main():
    """https://adventofcode.com/2023/day/1"""
    with open(DATA_PATH, "r") as f:
        ACTUAL_INPUT = f.read()

    output = get_sum_of_calibration_ints(TEST_INPUT_P1)
    assert output == TEST_OUTPUT_P1, f"expected {TEST_OUTPUT_P1} but got {output}"
    print("test part 1:", output)

    output = get_sum_of_calibration_ints(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P1, f"expected {ACTUAL_OUTPUT_P1} but got {output}"
    print("actual part 1:", output)

    output = get_sum_of_calibration_values(TEST_INPUT_P2)
    assert output == TEST_OUTPUT_P2, f"expected {TEST_OUTPUT_P2} but got {output}"
    print("test part 2:", output)

    output = get_sum_of_calibration_values(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P2, f"expected {ACTUAL_OUTPUT_P2} but got {output}"
    print("actual part 2:", output)


if __name__ == "__main__":
    main()
