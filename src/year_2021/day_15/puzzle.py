# I may have referred to an online algorith for this one!!

import heapq
import os
from typing import List, TypeVar

import numpy as np

_GridItem = TypeVar("_GridItem")


def tile(h: int, w: int, sub_grids: List[List[List[_GridItem]]]) -> List[List[_GridItem]]:
    tiled_grid: List[List[_GridItem]] = []
    for _ in range(h):
        tile_row = sub_grids[:w]
        sub_grids = sub_grids[w:]
        for i in range(len(tile_row[0])):
            tiled_grid.append([x for sub_grid in tile_row for x in sub_grid[i]])
    return tiled_grid


class Cell:
    numbers = None
    cells = {}

    def __init__(self, x, y, cost=0):
        self.x = x
        self.y = y
        self.value = self.numbers[self.y][self.x]
        self.cost = self.value + cost
        self.visited = False
        self.cells[(self.x, self.y)] = self

    @classmethod
    def reset(cls):
        cls.numbers = None
        cls.cells = {}

    @classmethod
    def get_adj(cls, cell):
        adj = []
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for _x, _y in zip(dx, dy):
            if (x := cell.x + _x) in range(0, len(cls.numbers[0])) and (y := cell.y + _y) in range(0, len(cls.numbers)):
                if (x, y) in cls.cells:
                    if not (c := cls.cells[(x, y)]).visited:
                        adj.append(c)
                else:
                    adj.append(cls(x, y, cell.cost))

        return adj

    def __lt__(self, other):
        return self.cost < other.cost


def increment(item, inc):
    item += inc
    item %= 9

    if item == 0:
        item = 9

    return item


def main():
    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))

    numbers = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            line = list(map(int, line.strip()))
            numbers.append(line)

    all_numbers = dict()
    v_increment = np.vectorize(increment)

    for i in range(9):
        all_numbers[i] = v_increment(numbers, i)

    sub_grids = []
    for i in range(5):
        for j in range(5):
            sub_grids.append(all_numbers[i + j])

    tiled_numbers = tile(5, 5, sub_grids)

    answer_1 = dijkstras(numbers)
    answer_2 = dijkstras(tiled_numbers)

    print(f"Puzzle 1 -> {answer_1}")
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1, answer_2


def dijkstras(numbers):
    Cell.reset()
    Cell.numbers = numbers

    start = Cell(0, 0, -numbers[0][0])
    # end = Cell(len(numbers[0]) - 1, len(numbers) - 1)

    heap = []
    mins = {(0, 0): 0}

    finished = False
    while not finished:
        if not heap:
            heapq.heappush(heap, start)

        c = heapq.heappop(heap)
        c.visited = True

        adj = Cell.get_adj(c)
        for ad in adj:
            if (ad.x, ad.y) not in mins or ad.cost < mins[(ad.x, ad.y)]:
                heapq.heappush(heap, ad)
                mins[(ad.x, ad.y)] = ad.cost

        if heap[0].x == len(numbers[0]) - 1 and heap[0].y == len(numbers) - 1:
            finished = True

    return heap[0].cost


if __name__ == "__main__":
    main()
