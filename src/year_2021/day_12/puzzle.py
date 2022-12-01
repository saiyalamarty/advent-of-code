import os
from collections import Counter, defaultdict
from copy import deepcopy


def main():

    # Read contents of input (as a file) with a context manager
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "input.data"))

    from_nodes = []
    to_nodes = []
    with open(file_path, "r") as input_file:
        for line in input_file:
            f, t = line.strip().split("-")
            from_nodes.append(f)
            to_nodes.append(t)

    nodes = list(set(from_nodes + to_nodes))
    nodes.sort()

    g = Graph(nodes)

    for f, t in zip(from_nodes, to_nodes):
        g.add_edge(f, t)

    all_paths_no_two_visits = g.find_all_paths("start", "end", False)
    all_paths_with_two_visits = g.find_all_paths("start", "end", True)

    answer_1 = len(all_paths_no_two_visits)
    answer_2 = len(all_paths_with_two_visits)

    print(f"Puzzle 1 -> {answer_1}")
    print(f"Puzzle 2 -> {answer_2}")

    return answer_1, answer_2


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = defaultdict(list)

    def add_edge(self, f, t):
        self.graph[f].append(t)
        self.graph[t].append(f)

    def find_all_paths(self, start, end, allow_two_visits):
        visited = Counter()
        all_paths = []
        current_path = []
        visited_twice = [not allow_two_visits]
        self._find_all_paths(visited, visited_twice, all_paths, current_path, start, end)

        return all_paths

    def _find_all_paths(self, visited, visited_twice, all_paths, current_path, start: str, end: str):
        if start == "start":
            visited.update({start: 1})

        current_path.append(start)

        if start == end:
            all_paths.append(deepcopy(current_path))

        else:
            for each_end in self.graph[start]:
                visit_count = visited.get(each_end, 0)

                if visit_count == 1 and not visited_twice[0] and each_end not in ["start", "end"]:
                    visited_twice[0] = True
                    visited.update({each_end: 1})
                    self._find_all_paths(visited, visited_twice, all_paths, current_path, each_end, end)

                elif visit_count < 1:
                    if each_end.islower():
                        visited.update({each_end: 1})
                    self._find_all_paths(visited, visited_twice, all_paths, current_path, each_end, end)

        current_path.pop()

        vc = visited.get(start, 0)
        if vc > 0:
            if vc == 2:
                visited_twice[0] = False
            visited.update({start: -1})


if __name__ == "__main__":
    main()
