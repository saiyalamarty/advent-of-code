import os

import numpy as np


def main():

    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))
    with open(file_path, "r") as input_file:
        for line in input_file:
            positions = np.array(list(map(int, line.strip().split(","))))

    min_fuel_1 = min_fuel_2 = np.inf
    for i in range(min(positions), max(positions)):
        min_fuel_1 = min(sum(np.absolute(positions - i)), min_fuel_1)
        min_fuel_2 = min(
            sum(int(each * (each + 1) / 2) for each in np.absolute(positions - i)),
            min_fuel_2,
        )

    print(f"Puzzle 1 -> {min_fuel_1}")
    print(f"Puzzle 2 -> {min_fuel_2}")

    return min_fuel_1, min_fuel_2


if __name__ == "__main__":
    main()
