"""
https://adventofcode.com/2024/day/9
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

# https://adventofcode.com/2024/day/9/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT_P1 = """
2333133121414131402
"""
TEST_INPUT_P2 = TEST_INPUT_P1
TEST_OUTPUT_P1 = 1928
TEST_OUTPUT_P2 = 2858
ACTUAL_OUTPUT_P1 = 6340197768906
ACTUAL_OUTPUT_P2 = 6363913128533


def part_1(input_string: str):
    """https://adventofcode.com/2024/day/9#part1"""
    disk_map = list(input_string.strip())
    opts = ["file_len", "space_len"]
    file_id = 0
    memory_block = []
    # print(disk_map)
    for i, x in enumerate(disk_map):
        opt = opts[i % 2]
        if opt == "file_len":
            memory_block += [str(file_id)] * int(x)
            file_id += 1
        elif opt == "space_len":
            memory_block += ["."] * int(x)
    # print(memory_block)
    # "clean up" the memory block:
    for i in range(len(memory_block), 0, -1):
        if memory_block[i - 1] != ".":
            first_dot_idx = memory_block.index(".")
            if first_dot_idx < i - 1:
                memory_block[first_dot_idx] = memory_block[i - 1]
                memory_block[i - 1] = "."
            else:
                break
    # print(memory_block)
    checksum = 0
    for i, x in enumerate(memory_block):
        if x != ".":
            checksum += i * int(x)
    return checksum


def part_2(input_string: str):
    """https://adventofcode.com/2024/day/9#part2"""
    disk_map = list(input_string.strip())
    opts = ["file_len", "space_len"]
    file_id = 0
    memory_block = []
    # print(disk_map)
    for i, x in enumerate(disk_map):
        opt = opts[i % 2]
        if opt == "file_len":
            memory_block += [file_id] * int(x)
            file_id += 1
        elif opt == "space_len":
            memory_block += ["."] * int(x)
    # print("".join(str(x) for x in memory_block))
    # "clean up" the memory block:
    file_spans: dict[int, tuple[int, int]] = {}
    space_locations: list[int] = []
    for i, x in enumerate(memory_block):
        if x == ".":
            space_locations.append(i)
            continue

        if x not in file_spans:
            file_spans[x] = (i, i)
        else:
            start, end = file_spans[x]
            file_spans[x] = (start, i)

    # print(space_locations)
    space_spans: dict[int, tuple[int, int]] = {}
    current_space_idx = space_locations[0]
    for i, x in enumerate(space_locations):
        space_spans[current_space_idx] = (current_space_idx, x)
        if i + 1 < len(space_locations):
            if space_locations[i + 1] != x + 1:
                current_space_idx = space_locations[i + 1]

    # print(file_spans)
    # print(space_spans)
    for i in sorted(file_spans.keys(), reverse=True):
        # print(i, file_spans[i])
        start, end = file_spans[i]
        size = 1 + end - start
        for j in sorted(space_spans.keys(), reverse=False):
            space_start, space_end = space_spans[j]
            space_size = 1 + space_end - space_start
            if space_size >= size and space_start < start:
                space_spans.pop(j)
                for k in range(space_start, space_start + size):
                    memory_block[k] = i
                if space_size > size:
                    space_spans[space_start + size] = (space_start + size, space_end)
                for k in range(start, start + size):
                    memory_block[k] = "."
                break
    # print("".join(str(x) for x in memory_block))
    checksum = 0
    for i, x in enumerate(memory_block):
        if x != ".":
            checksum += i * int(x)
    return checksum


def main():
    """https://adventofcode.com/2024/day/9"""
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
