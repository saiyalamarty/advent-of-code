import os
from collections import Counter
from copy import deepcopy


def main():
    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))

    dots = Counter()
    axis = []
    index = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            if line == "\n":
                break

            dots[tuple(map(int, line.strip().split(",")))] = 1

        for line in input_file:
            ax, idx = line.strip().lstrip("fold along ").split("=")
            axis.append(ax)
            index.append(int(idx))

    i = 0
    answer_1 = 0
    for ax, idx in zip(axis, index):
        if ax == "x":
            item = 0
        else:
            item = 1

        dts = deepcopy(list(dots.keys()))
        for dot in dts:
            if dot[item] > idx:
                dots.pop(dot)
                new_dot = list(dot)
                new_dot[item] = idx - (dot[item] - idx)
                dots.update({tuple(new_dot): 1})

        if i == 0:
            i += 1
            answer_1 = len(dots)

    x = [dot[0] for dot in dots.keys()]
    y = [dot[1] for dot in dots.keys()]

    answer_2 = "\n" + "\n".join(
        "".join(f"{chr(9608)}{chr(9608)}{chr(9608)}" if (x, y) in dots else "   " for x in range(max(x) + 1))
        for y in range(max(y) + 1)
    )

    print(f"Puzzle 1 -> {answer_1}")
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1


if __name__ == "__main__":
    main()
