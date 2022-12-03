import os


def main():
    # Input file path
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))

    # Read contents of input (as a file) with a context manager
    with open(file_path, "r") as input_file:
        lines = [line.strip() for line in input_file.readlines()]

        answer_1 = puzzle_1(lines)
        print(f"Puzzle 1 -> {answer_1}")

        answer_2 = puzzle_2(lines)
        print(f"Puzzle 2 -> {answer_2}")

        return answer_1, answer_2


def get_letter_number(letter):
    if not letter:
        return 0
    if letter.isupper():
        return ord(letter) - 64 + 26
    else:
        return ord(letter) - 96


def puzzle_1(lines):
    scores = [
        get_letter_number(letter)
        for line in lines
        for letter in set(line[: int(len(line) / 2)]).intersection(set(line[int(len(line) / 2) :]))
    ]

    return sum(scores)


def puzzle_2(lines):
    scores = [
        get_letter_number(letter)
        for line_1, line_2, line_3 in zip(lines[::3], lines[1::3], lines[2::3])
        for letter in set(line_1).intersection(set(line_2)).intersection(set(line_3))
    ]

    return sum(scores)


if __name__ == "__main__":
    main()
