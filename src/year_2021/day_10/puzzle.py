import os


def main():

    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))

    lines = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            lines.append(list(line.strip()))

    mapping = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }

    puzzle_1_score = {")": 3, "]": 57, "}": 1197, ">": 25137}

    puzzle_2_score = {")": 1, "]": 2, "}": 3, ">": 4}

    illegal_brackets = []
    completions_scores = []
    for line in lines:

        opened_brackets = []
        is_corrupt = False

        for bracket in line:

            if bracket in "([{<":
                opened_brackets.append(bracket)
                continue

            if bracket in ")]}>":
                if not opened_brackets or mapping[bracket] != opened_brackets[-1]:
                    illegal_brackets.append(bracket)
                    is_corrupt = True
                    break

                else:
                    opened_brackets.pop()
                    continue

        if is_corrupt:
            continue

        brackets_needed = reversed([mapping[bracket] for bracket in opened_brackets])
        start_score = 0
        for bracket in brackets_needed:
            start_score = (start_score * 5) + puzzle_2_score[bracket]
        completions_scores.append(start_score)

    answer_1 = sum(puzzle_1_score[bracket] for bracket in illegal_brackets)
    answer_2 = sorted(completions_scores)[len(completions_scores) // 2]

    print(f"Puzzle 1 -> {answer_1}")
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1, answer_2


if __name__ == "__main__":
    main()
