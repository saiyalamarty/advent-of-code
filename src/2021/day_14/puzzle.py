import os
from collections import Counter


def main():
    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'input.data')
    )

    insertions = {}
    with open(file_path, "r") as input_file:
        for line in input_file:
            if line == '\n':
                break
            template = line.strip()

        for line in input_file:
            pair, element = line.strip().split(" -> ")
            insertions[pair] = element

    pairs = Counter([i + j for i, j in zip(template, template[1:])])
    letters = Counter(template)

    for _ in range(10):
        build_polymer(pairs, letters, insertions)

    answer_1 = letters.most_common()[0][1] - letters.most_common()[-1][1]

    for _ in range(30):
        build_polymer(pairs, letters, insertions)

    answer_2 = letters.most_common()[0][1] - letters.most_common()[-1][1]

    print(f"Puzzle 1 -> {answer_1}")
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1, answer_2


def build_polymer(pairs, letters, insertions):
    add = Counter()
    remove = Counter()

    for pair, count in pairs.items():
        if ins := insertions.get(pair):
            remove.update({pair: count})
            i, j = list(pair)
            add.update({"".join([i, ins]): count, "".join([ins, j]): count})
            letters.update({ins: count})

    for k, v in remove.items():
        pairs.update({k: -v})
        if pairs.get(k) <= 0:
            pairs.pop(k)

    for k, v in add.items():
        pairs.update({k: v})


if __name__ == '__main__':
    main()
