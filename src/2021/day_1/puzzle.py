"""Advent of Code 2021 - Day 1"""


import os


def main():

    # Sample input:
    # 157
    # 158
    # 167
    # 157
    # 148
    # 154

    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'input.data')
    )
    with open(file_path, "r") as input_file:
        numbers = [int(number) for number in input_file]

    # Count consecutive numbers which are increasing
    puzzle_1 = sum(1 for i, j in zip(numbers, numbers[1:]) if j > i)
    print(f"Puzzle 1 -> {puzzle_1}")

    # Count consecutive sums of 3 numbers which are increasing
    # If sum_1 = a + b + c and sum_2 = b + c + d, then sum_2 > sum_1 if d > a
    puzzle_2 = sum(1 for i, j in zip(numbers, numbers[3:]) if j > i)
    print(f"Puzzle 2 -> {puzzle_2}")

    return puzzle_1, puzzle_2


if __name__ == "__main__":
    main()
