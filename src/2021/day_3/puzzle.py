"""Advent of Code 2021 - Day 3"""


import statistics
from copy import deepcopy


def main():

    # Read contents of input (as a file) with a context manager
    with open("input.data", "r") as input_file:
        numbers = [number.strip("\n") for number in input_file]

    print(puzzle_1(numbers))
    print(puzzle_2(numbers))


def puzzle_1(numbers: list[str]) -> int:

    gamma = ""
    epsilon = ""
    digit_count = len(numbers[0])
    for i in range(digit_count):
        m = find_mode(numbers, i)
        gamma += m
        epsilon += flip_bit(m)

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon


def puzzle_2(numbers_main: list[str]) -> int:
    numbers = deepcopy(numbers_main)
    digit_count = len(numbers[0])
    for i in range(digit_count):
        m = find_mode(numbers, i)
        numbers = filter_numbers(numbers, i, m)

        if len(numbers) == 1:
            break

    o2 = int(numbers[0], 2)

    numbers = deepcopy(numbers_main)
    for i in range(digit_count):
        m = find_mode(numbers, i)
        m = flip_bit(m)
        numbers = filter_numbers(numbers, i, m)

        if len(numbers) == 1:
            break

    co2 = int(numbers[0], 2)

    return o2 * co2


def filter_numbers(numbers: list[str], position: int, value: str) -> list[str]:
    return [number for number in numbers if number[position] == value]


def find_mode(numbers: list[str], position: int) -> str:
    numbers = [int(number[position]) for number in numbers]
    numbers.sort(reverse=True)

    mode = statistics.mode(numbers)

    return str(mode)


def flip_bit(b: str) -> str:
    return "0" if b == "1" else "1"


if __name__ == '__main__':
    main()
