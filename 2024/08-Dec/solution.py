"""
https://adventofcode.com/2024/day/8
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

# Third party imports:
import pyperclip

# https://adventofcode.com/2024/day/8/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT_P1 = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
TEST_INPUT_P2 = TEST_INPUT_P1
TEST_OUTPUT_P1 = 14
TEST_OUTPUT_P2 = 34
ACTUAL_OUTPUT_P1 = 371
ACTUAL_OUTPUT_P2 = 1229


def print_grid(grid: list[list[str]]):
    """Prints the grid with a border."""
    grid_width = len(grid[0])
    print("-" * grid_width)
    for row in grid:
        print("|" + "".join(row) + "|")
    print("-" * grid_width)


def get_grid(input_string: str):
    """Converts the input string into a grid."""
    return [list(x) for x in input_string.strip().split("\n")]


def part_1(input_string: str):
    """https://adventofcode.com/2024/day/8#part1"""
    grid = get_grid(input_string)
    # print_grid(grid)
    num_rows = len(grid)
    num_cols = len(grid[0])
    map_of_antenas: dict[str, list[tuple[int, int]]] = {}
    for r in range(num_rows):
        for c in range(num_cols):
            cell = grid[r][c]
            if cell != ".":
                map_of_antenas.setdefault(cell, []).append((r, c))

    antinodes: set[tuple[int, int]] = set()
    for k, v in map_of_antenas.items():
        if len(v) > 1:
            combos = itertools.combinations(v, 2)
            # print(k, list(combos))
            for a, b in combos:
                # print(k, a, b)
                dy = b[0] - a[0]
                dx = b[1] - a[1]
                antinode = (a[0] + (2 * dy), a[1] + (2 * dx))
                x, y = antinode
                if x >= 0 and y >= 0 and x < num_rows and y < num_cols:
                    grid[antinode[0]][antinode[1]] = "#"
                    # print("antinode:", antinode)
                    antinodes.add(antinode)

                antinode = (a[0] - dy, a[1] - dx)
                x, y = antinode
                if x >= 0 and y >= 0 and x < num_rows and y < num_cols:
                    grid[antinode[0]][antinode[1]] = "#"
                    # print("antinode:", antinode)
                    antinodes.add(antinode)

    print_grid(grid)
    return len(antinodes)


def part_2(input_string: str):
    """https://adventofcode.com/2024/day/8#part2"""
    grid = get_grid(input_string)
    # print_grid(grid)
    num_rows = len(grid)
    num_cols = len(grid[0])
    map_of_antenas: dict[str, list[tuple[int, int]]] = {}
    for r in range(num_rows):
        for c in range(num_cols):
            cell = grid[r][c]
            if cell != ".":
                map_of_antenas.setdefault(cell, []).append((r, c))

    antinodes: set[tuple[int, int]] = set()
    for k, v in map_of_antenas.items():
        if len(v) > 1:
            combos = itertools.combinations(v, 2)
            # print(k, list(combos))
            for a, b in combos:
                antinodes.add(a)
                antinodes.add(b)
                # print(k, a, b)
                dy = b[0] - a[0]
                dx = b[1] - a[1]
                direction_magnitude = 1
                while True:
                    m = direction_magnitude
                    antinode = (a[0] + (m * dy), a[1] + (m * dx))
                    x, y = antinode
                    if x >= 0 and y >= 0 and x < num_rows and y < num_cols:
                        grid[antinode[0]][antinode[1]] = "#"
                        # print("antinode:", antinode)
                        antinodes.add(antinode)
                    else:
                        break
                    direction_magnitude += 1

                direction_magnitude = -1
                while True:
                    m = direction_magnitude
                    antinode = (a[0] + (m * dy), a[1] + (m * dx))
                    x, y = antinode
                    if x >= 0 and y >= 0 and x < num_rows and y < num_cols:
                        grid[antinode[0]][antinode[1]] = "#"
                        # print("antinode:", antinode)
                        antinodes.add(antinode)
                    else:
                        break
                    direction_magnitude -= 1

    print_grid(grid)
    return len(antinodes)


def main():
    """https://adventofcode.com/2024/day/8"""
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
