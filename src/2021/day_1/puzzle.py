"""Advent of Code 2021 - Day 1"""


def main():

    # Sample input:
    # 157
    # 158
    # 167
    # 157
    # 148
    # 154

    # Read contents of input (as a file) with a context manager
    with open("input.data", "r") as input_file:
        numbers = [int(number) for number in input_file]

    # Count consecutive numbers which are increasing
    puzzle_1 = sum(1 for i, j in zip(numbers, numbers[1:]) if j > i)

    # Count consecutive sums of 3 numbers which are increasing
    # If sum_1 = a + b + c and sum_2 = b + c + d, then sum_2 > sum_1 if d > a
    puzzle_2 = sum(1 for i, j in zip(numbers, numbers[3:]) if j > i)

    print(f"{puzzle_1=}")
    print(f"{puzzle_2=}")


if __name__ == "__main__":
    main()
