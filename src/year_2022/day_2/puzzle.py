import os
from enum import Enum


class Options(Enum):
    ROCK = ("A", "X")
    PAPER = ("B", "Y")
    SCISSORS = ("C", "Z")

    @classmethod
    def get_option_based_on_value(cls, value):
        for option in cls:
            if value in option.value:
                return option
        raise ValueError(f"Invalid value: {value}")

    def play(self, other):

        if self == Options.ROCK:
            self_score = 1
            if other == Options.PAPER:
                return 0 + self_score
            if other == Options.SCISSORS:
                return 6 + self_score
            return 3 + self_score

        if self == Options.PAPER:
            self_score = 2
            if other == Options.SCISSORS:
                return 0 + self_score
            if other == Options.ROCK:
                return 6 + self_score
            return 3 + self_score

        if self == Options.SCISSORS:
            self_score = 3
            if other == Options.ROCK:
                return 0 + self_score
            if other == Options.PAPER:
                return 6 + self_score
            return 3 + self_score

        raise ValueError(f"Invalid comparison: {self} vs {other}")


def main():
    # Input file path
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))

    # Read contents of input (as a file) with a context manager
    with open(file_path, "r") as input_file:
        lines = input_file.read().splitlines()
        rounds = [line.split() for line in lines]

        answer_1 = puzzle_1(rounds)
        print(f"Puzzle 1 -> {answer_1}")

        answer_2 = puzzle_2(rounds)
        print(f"Puzzle 2 -> {answer_2}")

        return answer_1, answer_2


def puzzle_1(rounds):
    total_score = 0
    for round in rounds:
        round_score = Options.get_option_based_on_value(round[1]).play(Options.get_option_based_on_value(round[0]))
        total_score += round_score

    return total_score


def puzzle_2(rounds):
    # X - lose
    # Y - draw
    # Z - win

    # A - rock - 1
    # B - paper - 2
    # C - scissors - 3

    total_score = 0
    scores = {
        "AX": 3,
        "AY": 4,
        "AZ": 8,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 2,
        "CY": 6,
        "CZ": 7,
    }

    for round in rounds:
        round_score = scores[round[0] + round[1]]
        total_score += round_score

    return total_score


if __name__ == "__main__":
    main()
