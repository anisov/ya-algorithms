# 69337329
# Сначала необходимо построить граф, для этого используем список смежности.
# В качестве рёбер будем использовать дороги и условия, которые обозначают
# как связаны вершины. Но при наполнении графа, необходимо поменять направление
# одного из типов дорог, что бы получить цикл, так как смена направления
# приведёт к появлению цикла(в случае если присутствуют разные дороги ведущие
# из разных вершин к одной и тоже вершине). Для того что бы определить
# существуют ли циклы в графе, будет использоваться обход в глубину с
# определённым алгоритмом(is_dfs_cycle), который в случае обнаружения цикла
# будет выдавать True. А для того чтобы были точно проверены все вершины,
# запустим алгоритм для каждой из них(is_cycle).
# Временная сложность: O(V+E)
# Пространственная сложность: O(E*V)

import enum
import sys
from typing import (
    Dict,
    List,
)


class Colors(enum.Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class Road:
    B: str = "B"
    R: str = "R"


def is_dfs_cycle(
    adjacency: Dict[int, List[int]], colors: List[Colors], start_vertex: int
) -> bool:
    stack: List[int] = [start_vertex]
    while stack:
        v: int = stack.pop()
        if colors[v] == Colors.WHITE:
            colors[v] = Colors.GRAY
            stack.append(v)
            for i in adjacency[v]:
                if colors[i] == Colors.WHITE:
                    stack.append(i)
                elif colors[i] == Colors.GRAY:
                    return True
        elif colors[v] == Colors.GRAY:
            colors[v] = Colors.BLACK
    return False


def is_cycle(adjacency: Dict[int, List[int]]) -> bool:
    colors: List[Colors] = [Colors.WHITE] * len(adjacency)
    for i in range(len(adjacency)):
        if is_dfs_cycle(adjacency=adjacency, colors=colors, start_vertex=i):
            return True
    return False


def main() -> None:
    vertices: int = int(input())
    adjacency: Dict[int, List[int]] = {i: [] for i in range(vertices)}
    for i in range(vertices - 1):
        for j, road in enumerate(sys.stdin.readline().rstrip()):
            if road == Road.B:
                adjacency[i].append(i + j + 1)
            elif road == Road.R:
                adjacency[i + j + 1].append(i)
    print("YES" if not is_cycle(adjacency=adjacency) else "NO")


if __name__ == "__main__":
    main()
