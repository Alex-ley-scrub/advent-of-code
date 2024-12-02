import os
import requests

COOKIE = os.getenv("AOC_COOKIE")
TEMPLATE_PY = """\"\"\"
https://adventofcode.com/{year}/day/{day}
\"\"\"

# Future imports (must occur at the beginning of the file):
from __future__ import annotations  # https://www.python.org/dev/peps/pep-0585/

# Standard library imports:
import os
import re

# https://adventofcode.com/{year}/day/{day}/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT = \"\"\"
\"\"\"
TEST_OUTPUT_P1 = ...
TEST_OUTPUT_P2 = ...
ACTUAL_OUTPUT_P1 = ...
ACTUAL_OUTPUT_P2 = ...

def part_1(input_string: str):
    \"\"\"https://adventofcode.com/{year}/day/{day}#part1\"\"\"
    ...

def part_2(input_string: str):
    \"\"\"https://adventofcode.com/{year}/day/{day}#part2\"\"\"
    ...

def main():
    \"\"\"https://adventofcode.com/{year}/day/{day}\"\"\"
    with open(DATA_PATH, "r") as f:
        ACTUAL_INPUT = f.read()

    output = part_1(TEST_INPUT)
    assert output == TEST_OUTPUT_P1, f"expected {{TEST_OUTPUT_P1}} but got {{output}}"
    print("test part 1:", output)

    output = part_1(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P1, f"expected {{ACTUAL_OUTPUT_P1}} but got {{output}}"
    print("actual part 1:", output)

    output = part_2(TEST_INPUT)
    assert output == TEST_OUTPUT_P2, f"expected {{TEST_OUTPUT_P2}} but got {{output}}"
    print("test part 2:", output)

    output = part_2(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P2, f"expected {{ACTUAL_OUTPUT_P2}} but got {{output}}"
    print("actual part 2:", output)

if __name__ == "__main__":
    main()
"""


def get_input(year: int, day: int) -> str:
    """Get input for a given year and day and save it to a file."""
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(url, cookies={"cookie": COOKIE}, timeout=60)
    text = response.text
    print(text[:250])
    dev_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    # pad day with 0 if less than 10 using f-string formatting:
    path = os.path.join(dev_path, str(year), f"{day:02}-Dec", "input.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text)
    print(f"Input saved to {path}")
    py_path = os.path.join(dev_path, str(year), f"{day:02}-Dec", "solution.py")
    if not os.path.exists(py_path):
        with open(py_path, "w") as f:
            f.write(TEMPLATE_PY.format(year=year, day=day))
        print(f"Solution template saved to {py_path}")
    return path


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--year", type=int)
    parser.add_argument("--day", type=int)
    args = parser.parse_args()
    get_input(args.year, args.day)
