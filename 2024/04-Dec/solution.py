"""
https://adventofcode.com/2024/day/4
"""

# Future imports (must occur at the beginning of the file):
from __future__ import annotations  # https://www.python.org/dev/peps/pep-0585/

# Standard library imports:
import os
import re

# https://adventofcode.com/2024/day/4/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
TEST_OUTPUT_P1 = 18
TEST_OUTPUT_P2 = 9
ACTUAL_OUTPUT_P1 = 2397
ACTUAL_OUTPUT_P2 = 1824


def get_horizontal(grid: list[list[str]], r: int, c: int):
    return grid[r][c] + grid[r][c + 1] + grid[r][c + 2] + grid[r][c + 3]


def get_vertical(grid: list[list[str]], r: int, c: int):
    return grid[r][c] + grid[r + 1][c] + grid[r + 2][c] + grid[r + 3][c]


def get_diagonal(grid: list[list[str]], r: int, c: int):
    return grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] + grid[r + 3][c + 3]


def get_diagonal_2(grid: list[list[str]], r: int, c: int):
    return grid[r][c] + grid[r - 1][c + 1] + grid[r - 2][c + 2] + grid[r - 3][c + 3]


def get_diagonal_3(grid: list[list[str]], r: int, c: int):
    return grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]


def get_diagonal_4(grid: list[list[str]], r: int, c: int):
    return grid[r][c] + grid[r - 1][c + 1] + grid[r - 2][c + 2]


def part_1(input_string: str):
    """https://adventofcode.com/2024/day/4#part1"""
    grid = [list(x) for x in input_string.strip().split("\n")]
    num_rows = len(grid)
    num_cols = len(grid[0])
    print(num_rows, num_cols)
    total = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if c + 3 < num_cols:
                word = get_horizontal(grid, r, c)
                if word == "XMAS" or word == "SAMX":
                    total += 1
            if r + 3 < num_rows:
                word = get_vertical(grid, r, c)
                if word == "XMAS" or word == "SAMX":
                    total += 1
            if r + 3 < num_rows and c + 3 < num_cols:
                word = get_diagonal(grid, r, c)
                if word == "XMAS" or word == "SAMX":
                    total += 1
            if r - 3 >= 0 and c + 3 < num_cols:
                word = get_diagonal_2(grid, r, c)
                if word == "XMAS" or word == "SAMX":
                    total += 1
    return total


def part_2(input_string: str):
    """https://adventofcode.com/2024/day/4#part2"""
    grid = [list(x) for x in input_string.strip().split("\n")]
    num_rows = len(grid)
    num_cols = len(grid[0])
    print(num_rows, num_cols)
    total = 0
    # i,j is the center of the X - i.e. the "A"
    for i in range(1, num_rows - 1):
        for j in range(1, num_cols - 1):
            is_down_diagonal = False
            is_up_diagonal = False
            # top left corner of the X
            r = i - 1
            c = j - 1
            word = get_diagonal_3(grid, r, c)
            if word == "MAS" or word == "SAM":
                is_down_diagonal = True
            # bottom left corner of the X
            r = i + 1
            c = j - 1
            word = get_diagonal_4(grid, r, c)
            if word == "MAS" or word == "SAM":
                is_up_diagonal = True
            if is_down_diagonal and is_up_diagonal:
                total += 1
    return total


def main():
    """https://adventofcode.com/2024/day/4"""
    with open(DATA_PATH, "r") as f:
        ACTUAL_INPUT = f.read()

    output = part_1(TEST_INPUT)
    assert output == TEST_OUTPUT_P1, f"expected {TEST_OUTPUT_P1} but got {output}"
    print("test part 1:", output)

    output = part_1(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P1, f"expected {ACTUAL_OUTPUT_P1} but got {output}"
    print("actual part 1:", output)

    output = part_2(TEST_INPUT)
    assert output == TEST_OUTPUT_P2, f"expected {TEST_OUTPUT_P2} but got {output}"
    print("test part 2:", output)

    output = part_2(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P2, f"expected {ACTUAL_OUTPUT_P2} but got {output}"
    print("actual part 2:", output)


if __name__ == "__main__":
    main()
