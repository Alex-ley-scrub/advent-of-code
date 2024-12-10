"""
https://adventofcode.com/2024/day/5
"""

# Future imports (must occur at the beginning of the file):
from __future__ import annotations  # https://www.python.org/dev/peps/pep-0585/

# Standard library imports:
import os
import re
import time

# Third party imports:
import pyperclip

# https://adventofcode.com/2024/day/5/input
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.abspath(os.path.join(DIR_PATH, "input.txt"))

TEST_INPUT_P1 = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
TEST_INPUT_P2 = TEST_INPUT_P1
TEST_OUTPUT_P1 = 143
TEST_OUTPUT_P2 = 123
ACTUAL_OUTPUT_P1 = 5108
ACTUAL_OUTPUT_P2 = 7380


def get_rules_and_page_groups(input_string: str):
    """https://adventofcode.com/2024/day/5"""
    batch_1, batch_2 = input_string.strip().split("\n\n")
    rules: dict[str, list[str]] = {}
    for x in batch_1.strip().split("\n"):
        k, v = x.split("|")
        rules.setdefault(k, []).append(v)
    print(rules)
    pages_groups = [x.split(",") for x in batch_2.strip().split("\n")]
    print("len(pages_groups):", len(pages_groups))
    return rules, pages_groups


def get_valid_invalid_page_groups(
    rules: dict[str, list[str]], pages_groups: list[list[str]]
):
    """https://adventofcode.com/2024/day/5"""
    valid_page_groups: list[list[str]] = []
    invalid_page_groups: list[list[str]] = []
    for pages in pages_groups:
        is_valid = True
        for idx, page_no in enumerate(pages):
            if page_no in rules:
                later_pages = rules[page_no]
                for later_page in later_pages:
                    if later_page in pages[:idx]:
                        is_valid = False
                        invalid_page_groups.append(pages)
                        break
                if is_valid is False:
                    break
        if is_valid:
            valid_page_groups.append(pages)
    assert len(pages_groups) == len(valid_page_groups) + len(invalid_page_groups)
    return invalid_page_groups, valid_page_groups


def part_1(input_string: str):
    """https://adventofcode.com/2024/day/5#part1"""
    rules, pages_groups = get_rules_and_page_groups(input_string)
    _, valid_page_groups = get_valid_invalid_page_groups(rules, pages_groups)
    total = 0
    for pages in valid_page_groups:
        # add middle page_no
        middle_idx = len(pages) // 2
        total += int(pages[middle_idx])
    return total


def part_2(input_string: str):
    """https://adventofcode.com/2024/day/5#part2"""
    rules, pages_groups = get_rules_and_page_groups(input_string)
    invalid_page_groups, _ = get_valid_invalid_page_groups(rules, pages_groups)
    total = 0
    for pages in invalid_page_groups:
        # print("before:", pages)
        # make the pages valid using the rules:
        # brute force, but there should be a better way:
        is_valid = False
        num_loops = 0
        while is_valid is False and num_loops < 200:
            num_loops += 1
            nested_is_valid = True
            for idx, page_no in enumerate(pages):
                if page_no in rules:
                    later_pages = rules[page_no]
                    for later_page in later_pages:
                        if later_page in pages[:idx]:
                            earlier_index = pages.index(later_page)
                            # print("swap", page_no, later_page)
                            pages[idx] = later_page
                            pages[earlier_index] = page_no
                            nested_is_valid = False
                            break
                    if nested_is_valid is False:
                        break
            is_valid = nested_is_valid
        assert is_valid, f"pages still invalid: {pages}"
        # print("after:", pages, is_valid)
        print("took num_loops:", num_loops)
        # add middle page_no
        middle_idx = len(pages) // 2
        total += int(pages[middle_idx])
    return total


def main():
    """https://adventofcode.com/2024/day/5"""
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
