"""Advent of Code 2021 - Day 2"""


def main():
    puzzle_1()
    puzzle_2()


def puzzle_1():

    # Read contents of input (as a file) with a context manager
    with open("input.data", "r") as input_file:

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

        print(f"Puzzle 1 -> {hor*dep}")


def puzzle_2():
    with open("input.data", "r") as input_file:

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
                    dep += aim*int(x)

        print(f"Puzzle 2 -> {hor*dep}")


if __name__ == '__main__':
    puzzle_1()
    puzzle_2()
