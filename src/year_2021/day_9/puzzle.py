import os


class Location:
    def __init__(self, value, coords):
        self.value = value
        self.coord = coords


def main():

    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))

    numbers = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            num = [99999] + list(map(int, list(line.strip()))) + [99999]
            if not numbers:
                numbers.append([99999] * len(num))

            numbers.append(num)
        numbers.append([99999] * len(num))

    lows = find_lows(numbers)

    answer_1 = sum(low.value for low in lows) + len(lows)

    # Puzzle 2
    basin_sizes = []
    for low in lows:
        basin_coords = find_valid_neighbors(numbers, low.coord, set())
        basin_sizes.append(len(basin_coords))

    basin_sizes = sorted(basin_sizes, reverse=True)[:3]

    answer_2 = 1
    for each in basin_sizes:
        answer_2 *= each

    print(f"Puzzle 1 -> {answer_1}")
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1, answer_2


def find_valid_neighbors(numbers, coords, basin_coords):

    if coords in basin_coords:
        return

    basin_coords.add(coords)
    adj_coords = [
        (coords[0] - 1, coords[1]),
        (coords[0] + 1, coords[1]),
        (coords[0], coords[1] - 1),
        (coords[0], coords[1] + 1),
    ]
    for each in adj_coords:
        if numbers[each[1]][each[0]] < 9:
            find_valid_neighbors(numbers, each, basin_coords)

    return basin_coords


def find_lows(numbers) -> list[Location]:
    lows = []

    for j in range(1, len(numbers) - 1):
        first = numbers[j - 1]
        second = numbers[j]
        third = numbers[j + 1]
        for i in range(1, len(first) - 1):
            if second[i] < min(first[i], second[i - 1], second[i + 1], third[i]):
                lows.append(Location(second[i], (i, j)))

    return lows


if __name__ == "__main__":
    main()
