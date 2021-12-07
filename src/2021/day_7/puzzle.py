import os

import numpy as np


def main():
    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'input.data')
    )

    with open(file_path, "r") as input_file:
        for line in input_file:
            positions = np.array(list(map(int, line.strip().split(","))))

    return puzzle_1(positions), puzzle_2(positions)


def puzzle_1(positions: np.array):

    min_fuel = None
    for i in range(min(positions), max(positions)):
        fuel = sum(np.absolute(positions - i))
        min_fuel = min_fuel or fuel
        min_fuel = min(fuel, min_fuel)

    print(f"Puzzle 1 -> {min_fuel}")
    return min_fuel


def puzzle_2(positions: np.array):

    min_fuel = None
    for i in range(min(positions), max(positions)):
        fuel = sum(int(each * (each + 1) / 2) for each in np.absolute(positions - i))
        min_fuel = min_fuel or fuel
        min_fuel = min(fuel, min_fuel)

    print(f"Puzzle 2 -> {min_fuel}")
    return min_fuel


if __name__ == '__main__':
    main()
