"""
https://adventofcode.com/2023/day/2
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

# https://adventofcode.com/2023/day/2/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
TEST_OUTPUT_P1 = 8
TEST_OUTPUT_P2 = 2286
ACTUAL_OUTPUT_P1 = 2810
ACTUAL_OUTPUT_P2 = 69110
NUM_BALLS_P1 = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def part_1(input_string: str):
    """https://adventofcode.com/2023/day/2#part1"""
    games = input_string.strip().split("\n")
    total = 0
    for game in games:
        valid_game = True
        game_name, hands_str = game.split(":")
        game_id = game_name.strip("Game ")
        hands = hands_str.split(";")
        for hand in hands:
            for ball in hand.split(","):
                num, color = ball.strip().split()
                if NUM_BALLS_P1[color] < int(num):
                    valid_game = False
                    break
        if valid_game:
            total += int(game_id)
    return total


def part_2(input_string: str):
    """https://adventofcode.com/2023/day/2#part2"""
    games = input_string.strip().split("\n")
    total = 0
    for game in games:
        min_balls = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        _, hands_str = game.split(":")
        hands = hands_str.split(";")
        for hand in hands:
            for ball in hand.split(","):
                num, color = ball.strip().split()
                min_balls[color] = max(int(num), min_balls[color])
        power = functools.reduce(operator.mul, min_balls.values(), 1)
        total += power
    return total


def main():
    """https://adventofcode.com/2023/day/2"""
    with open(DATA_PATH, "r") as f:
        ACTUAL_INPUT = f.read()

    output = part_1(TEST_INPUT)
    assert output == TEST_OUTPUT_P1, f"expected {TEST_OUTPUT_P1} but got {output}"
    print("test part 1:", output)

    output = part_1(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P1, f"expected {ACTUAL_OUTPUT_P1} but got {output}"
    print("actual part 1:", output)
    pyperclip.copy(output)

    output = part_2(TEST_INPUT)
    assert output == TEST_OUTPUT_P2, f"expected {TEST_OUTPUT_P2} but got {output}"
    print("test part 2:", output)

    output = part_2(ACTUAL_INPUT)
    assert output == ACTUAL_OUTPUT_P2, f"expected {ACTUAL_OUTPUT_P2} but got {output}"
    print("actual part 2:", output)
    pyperclip.copy(output)


if __name__ == "__main__":
    main()
