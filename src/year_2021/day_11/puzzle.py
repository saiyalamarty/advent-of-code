import os
from copy import deepcopy


def main():

    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))

    numbers = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            line = list(map(int, line.strip()))
            numbers.append(line)

    answer_1 = puzzle_1(deepcopy(numbers))
    answer_2 = puzzle_2(deepcopy(numbers))

    print(f"Puzzle 1 -> {answer_1}")
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1, answer_2


def puzzle_1(numbers):
    total_flashed = 0
    for i in range(100):
        numbers, to_flash = increase_energy(numbers)
        flashed = flash(numbers, to_flash)
        total_flashed += flashed

    return total_flashed


def puzzle_2(numbers):
    x, y = len(numbers[0]), len(numbers)
    all_flashed = 0
    day = 0
    while not all_flashed:
        day += 1
        numbers, to_flash = increase_energy(numbers)
        flashed = flash(numbers, to_flash)

        if flashed == (x * y):
            all_flashed = day
    return all_flashed


def increase_energy(numbers):
    to_flash = set()
    for j in range(len(numbers)):
        for i in range(len(numbers[j])):
            if numbers[j][i] > 9:
                numbers[j][i] = 0

            numbers[j][i] += 1
            if numbers[j][i] == 10:
                to_flash.add((i, j))

    return numbers, to_flash


def flash(numbers, to_flash):
    x, y = len(numbers[0]), len(numbers)

    flashed = set()
    while to_flash:
        additional_to_flash = set()
        for each in to_flash:
            for n in range(each[1] - 1, each[1] + 2):
                for m in range(each[0] - 1, each[0] + 2):
                    if n in range(y) and m in range(x) and (m, n) not in flashed:
                        numbers[n][m] += 1
                        if numbers[n][m] == 10:
                            additional_to_flash.add((m, n))
            flashed.add(each)
        to_flash -= flashed
        to_flash = to_flash.union(additional_to_flash)

    return len(flashed)


if __name__ == "__main__":
    main()
