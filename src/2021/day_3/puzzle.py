"""Advent of Code 2021 - Day 3"""


import os
import statistics
from copy import deepcopy


def main():

    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'input.data')
    )
    with open(file_path, "r") as input_file:
        numbers = [number.strip("\n") for number in input_file]

    return puzzle_1(numbers), puzzle_2(numbers)


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

    answer = gamma * epsilon
    print(f"Puzzle 1 -> {answer}")

    return answer


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

    answer = o2 * co2
    print(f"Puzzle 2 -> {answer}")

    return answer


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
