"""
https://adventofcode.com/2023/day/1
"""

# Future imports (must occur at the beginning of the file):
from __future__ import annotations  # https://www.python.org/dev/peps/pep-0585/

# Standard library imports:
import os
import re


def replace_words_with_numbers(input_string: str):
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
    # get overlapping matches by using a capturing group inside a lookahead
    # https://stackoverflow.com/a/70979561/9792594
    regex = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")
    matches = regex.findall(calibration_string)
    values = [replace_words_with_numbers(s) for s in matches]
    return int(values[0] + values[-1])


# https://adventofcode.com/2023/day/1/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))
with open(DATA_PATH, "r") as f:
    calibration_strings = f.readlines()
    calibration_values = [get_calibration_value(s) for s in calibration_strings if s]
    total = sum(calibration_values)
    print("final answer:", total)
