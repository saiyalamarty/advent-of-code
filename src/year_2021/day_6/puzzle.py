import os
from collections import Counter


def main():

    answer_1 = puzzle(80)
    print(f"Puzzle 1 -> {answer_1}")

    answer_2 = puzzle(256)
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1, answer_2


def puzzle(days: int) -> int:

    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'input.data')
    )
    with open(file_path, "r") as input_file:
        for line in input_file:
            fish_states = list(map(int, line.strip().split(",")))

    fishes = Counter(fish_states)

    for _ in range(days):
        new_fishes = Counter()
        for key, value in fishes.items():
            new_fishes[key - 1] = value
        fishes = new_fishes

        if -1 in fishes:
            fishes[6] += fishes[-1]
            fishes[8] += fishes[-1]
            del fishes[-1]

    return sum(list(fishes.values()))


if __name__ == '__main__':
    main()
