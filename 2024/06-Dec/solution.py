"""
https://adventofcode.com/2024/day/6
"""

# Future imports (must occur at the beginning of the file):
from __future__ import annotations  # https://www.python.org/dev/peps/pep-0585/

# Standard library imports:
import os
import re
import operator
import itertools
import functools

# Third party imports:
import pyperclip

# https://adventofcode.com/2024/day/6/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT_P1 = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
TEST_INPUT_P2 = TEST_INPUT_P1
TEST_OUTPUT_P1 = 41
TEST_OUTPUT_P2 = 6
ACTUAL_OUTPUT_P1 = 4433
ACTUAL_OUTPUT_P2 = 1516


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


def play_game(grid: list[list[str]], debug: bool = False):
    """https://adventofcode.com/2024/day/6"""
    r, c = -1, -1
    symbol = ""
    for i, row in enumerate(grid):
        if "^" in row or ">" in row or "v" in row or "<" in row:
            r, c = i, row.index("^")
            symbol = row[c]
            break
    all_symbols = ["^", ">", "v", "<"]
    all_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    assert symbol in all_symbols
    direction = all_directions[all_symbols.index(symbol)]

    visited: set[tuple[int, int]] = set()
    direction = (-1, 0)
    steps = 0
    is_loop = False

    while True:
        steps += 1
        visited.add((r, c))
        grid[r][c] = symbol
        if debug:
            print_grid(grid)
        grid[r][c] = "X"
        r1 = r + direction[0]
        c1 = c + direction[1]
        if r1 < 0 or r1 >= len(grid) or c1 < 0 or c1 >= len(grid[0]):
            # we left the grid
            break
        if grid[r1][c1] == "#" or grid[r1][c1] == "O":
            # turn right
            for i, d in enumerate(all_directions):
                if d == direction:
                    direction = all_directions[(i + 1) % 4]
                    symbol = all_symbols[(i + 1) % 4]
                    break
            continue
        r, c = r1, c1
        if steps > len(visited) * 3:
            is_loop = True
            break
    return is_loop, visited, steps


def part_1(input_string: str):
    """https://adventofcode.com/2024/day/6#part1"""
    grid = get_grid(input_string)
    _is_loop, visited, _steps = play_game(grid, debug=False)
    return len(visited)


def part_2(input_string: str):
    """https://adventofcode.com/2024/day/6#part2"""
    original_grid = get_grid(input_string)
    grid_length = len(original_grid)
    grid_width = len(original_grid[0])
    total = 0
    for r in range(grid_length):
        for c in range(grid_width):
            if original_grid[r][c] != ".":
                continue
            grid = [row.copy() for row in original_grid]
            grid[r][c] = "O"
            is_loop, _, _ = play_game(grid, debug=False)
            if is_loop:
                total += 1
    return total


def main():
    """https://adventofcode.com/2024/day/6"""
    with open(DATA_PATH, "r") as f:
        ACTUAL_INPUT = f.read()

    output = part_1(TEST_INPUT_P1)
    assert output == TEST_OUTPUT_P1, f"expected {TEST_OUTPUT_P1} but got {output}"
    print("test part 1:", output)

    output = part_1(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P1, f"expected {ACTUAL_OUTPUT_P1} but got {output}"
    print("actual part 1:", output)
    pyperclip.copy(output)

    output = part_2(TEST_INPUT_P2)
    assert output == TEST_OUTPUT_P2, f"expected {TEST_OUTPUT_P2} but got {output}"
    print("test part 2:", output)

    output = part_2(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P2, f"expected {ACTUAL_OUTPUT_P2} but got {output}"
    print("actual part 2:", output)
    pyperclip.copy(output)


if __name__ == "__main__":
    main()
