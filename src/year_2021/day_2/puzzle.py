"""Advent of Code 2021 - Day 2"""


import os


def main():
    return puzzle_1(), puzzle_2()


def puzzle_1():

    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))
    with open(file_path, "r") as input_file:

        # Initializing horizontal distance and depth to 0
        hor = 0
        dep = 0

        # Iterating over each line of the file
        for line in input_file:

            # Split the line based on the whitespace
            # This returns a list of 2 words
            match line.split():

                # Matching the first element of the list
                # Extracting the second element of the list (binding?)
                case ["down", x]:
                    dep += int(x)

                case ["up", x]:
                    dep -= int(x)

                case ["forward", x]:
                    hor += int(x)

        answer = hor * dep
        print(f"Puzzle 1 -> {answer}")

    return answer


def puzzle_2():

    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))
    with open(file_path, "r") as input_file:

        aim = 0
        hor = 0
        dep = 0

        for line in input_file:
            match line.split():
                case ["down", x]:
                    aim += int(x)

                case ["up", x]:
                    aim -= int(x)

                case ["forward", x]:
                    hor += int(x)
                    dep += aim * int(x)

        answer = hor * dep
        print(f"Puzzle 2 -> {answer}")

    return answer


if __name__ == "__main__":
    main()
