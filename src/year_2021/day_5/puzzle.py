import os
from collections import Counter


def main():

    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))
    with open(file_path, "r") as input_file:
        coordinates = []
        for line in input_file:
            start_end = line.strip().split(" -> ")
            start_end = [each.split(",") for each in start_end]
            start_end = [[int(i) for i in j] for j in start_end]
            coordinates.append(start_end)

    answer_1 = puzzle(coordinates, False)
    print(f"Puzzle 1 -> {answer_1}")

    answer_2 = puzzle(coordinates, True)
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1, answer_2


def puzzle(coordinates, allow_diagonals: bool):

    if not allow_diagonals:
        coordinates = [each for each in coordinates if (each[0][0] == each[1][0] or each[0][1] == each[1][1])]

    points = []
    for start_end in coordinates:
        start = start_end[0]
        end = start_end[1]

        if start[0] == end[0]:
            sign = -int((start[1] - end[1]) / abs(start[1] - end[1]))
            for i in range(start[1], end[1], sign):
                points.append([start[0], i])
            points.append([start[0], end[1]])

        elif start[1] == end[1]:
            sign = -int((start[0] - end[0]) / abs(start[0] - end[0]))
            for i in range(start[0], end[0], sign):
                points.append([i, start[1]])
            points.append([end[0], start[1]])

        else:
            signx = -int((start[0] - end[0]) / abs(start[0] - end[0]))
            signy = -int((start[1] - end[1]) / abs(start[1] - end[1]))

            for x, y in zip(range(start[0], end[0], signx), range(start[1], end[1], signy)):
                points.append([x, y])
            points.append([end[0], end[1]])

    points = [str(point) for point in points]
    return len([count for count in Counter(points).values() if count >= 2])


if __name__ == "__main__":
    main()
