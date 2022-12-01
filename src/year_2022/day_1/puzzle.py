import os

from numpy import sort


def main():
    # Input file path
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))

    # Read contents of input (as a file) with a context manager
    with open(file_path, "r") as input_file:
        # Split lines based on empty new line
        # This returns a list of lists of strings
        groups = [group.splitlines() for group in input_file.read().split("\n\n")]

        answer_1 = puzzle_1(groups)
        print(f"Puzzle 1 -> {answer_1}")

        answer_2 = puzzle_2(groups)
        print(f"Puzzle 2 -> {answer_2}")

        return answer_1, answer_2


def puzzle_1(groups):
    calories = [sum(map(int, group)) for group in groups]

    return max(calories)


def puzzle_2(groups):
    calories = sort([sum(map(int, group)) for group in groups])

    return sum(calories[-3:])


if __name__ == "__main__":
    main()
