import os
from collections import Counter, defaultdict
from copy import deepcopy

import numpy as np


def main():

    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'input.data')
    )

    board_count = -1
    boards = defaultdict(list)

    # Read contents of input (as a file) with a context manager
    with open(file_path, "r") as input_file:
        for i, line in enumerate(input_file):
            if i == 0:
                input_numbers = line.strip("\n").split(",")
                input_numbers = [int(number) for number in input_numbers]
                continue

            if not line.strip("\n"):
                board_count += 1
                continue

            boards[board_count].append(list(map(int, line.strip("\n").split())))

    boards = dict(boards)
    for key, value in boards.items():
        boards[key] = np.array(value)

    boards1 = deepcopy(boards)
    board, number = get_first_bingo_board_and_number(boards1, input_numbers)
    answer_1 = get_unmarked_sum(board) * number
    print(f"Puzzle 1 -> {answer_1}")

    boards2 = deepcopy(boards)
    board, number = get_last_bingo_board_and_number(boards2, input_numbers)
    answer_2 = get_unmarked_sum(board) * number
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1, answer_2


def get_unmarked_sum(board: np.array) -> int:
    return np.sum(board) + np.count_nonzero(board == -1)


def get_first_bingo_board_and_number(boards: dict, input_numbers: list[int]) -> (np.array, int):
    for number in input_numbers:
        for board in boards.values():
            board = update_board(board, number)
            bingo = check_bingo(board)
            if bingo:
                return board, number


def get_last_bingo_board_and_number(boards: dict, input_numbers: list[int]) -> (np.array, int):
    for number in input_numbers:
        boards_to_delete = []
        for board_number, board in boards.items():
            board = update_board(board, number)
            bingo = check_bingo(board)
            if bingo:
                if len(boards) == 1:
                    return list(boards.values())[0], number

                boards_to_delete.append(board_number)

        [boards.pop(each) for each in boards_to_delete]


def check_bingo(board: np.array) -> bool:
    xy = np.where(board == -1)
    x = Counter(list(xy[0]))
    y = Counter(list(xy[1]))

    if not x:
        return False

    if x.most_common(1)[0][1] == 5 or y.most_common(1)[0][1] == 5:
        return True


def update_board(board: np.array, number: int) -> np.array:
    board[board == number] = -1
    return board


if __name__ == '__main__':
    main()
