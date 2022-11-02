# 69348107
# Необходимо составить остовное дерево. При составлении оставного дерева
# необходимо брать и сохранять вершину с самым тяжёлым ребром, которое к ней
# ведёт.
# Для реализации данного алгоритма используются функции find_mst и add_vertex.
# При запуске функции find_mst, берётся самая первая вершина и запускается
# функция add_vertex, которая добавляет все рёбра с вершинами у взятой вершины
# в очередь с приоритетом(edges) и удаляет её из множества not_added(т.к.
# данная вершина уже будет добавлена и больше её обрабатывать не нужно). После
# данной операции, в функции find_mst выбирается максимальная вершина из
# очереди с приоритетом, и повторяется весь алгоритм заново, пока все вершины
# с рёбрами не будут добавлены в оставное дерево(пока есть вершины, которые не
# добавленные в остов - not_added и рёбра исходящие из оставного дерева -
# edges).
# Временная сложность: O(E*logV) E — количество рёбер в графе, а V — количество
# вершин. Т.к. используется очередь с приоритетом.
# Пространственная сложность: O(V*E)


import sys
from typing import (
    List,
    Set,
    Tuple,
    Union,
)
from heapq import (
    heappop,
    heappush,
)


def add_vertex(
    v: int,
    adjacency: List[List[Union[float, int]]],
    not_added: Set[int],
    edges: List[Tuple[int, int]],
) -> None:
    not_added.remove(v)
    verticals: List[Union[float, int]] = adjacency[v]
    for i, weight in enumerate(verticals):
        if i in not_added and weight > float("-inf"):
            heappush(edges, (-weight, i))  # type: ignore
    return None


def extract_maximum(edges: List[Tuple[int, int]]) -> Tuple[int, int]:
    return heappop(edges)


def find_mst(
    adjacency: List[List[Union[float, int]]],
    vertices: List[int],
) -> List[Tuple[int, int]]:
    not_added: Set[int] = set()
    not_added.update(vertices)
    edges: List[Tuple[int, int]] = []
    maximum_spanning_tree: List[Tuple[int, int]] = []
    add_vertex(vertices[0], adjacency, not_added, edges)
    while not_added and edges:
        weight, v = extract_maximum(edges)
        if v in not_added:
            maximum_spanning_tree.append((v, abs(weight)))
            add_vertex(v, adjacency, not_added, edges)
    if not_added:
        raise ValueError("Oops! I did it again")
    return maximum_spanning_tree


def main() -> None:
    n, m = list(map(int, input().split()))
    adjacency: List[List[Union[int, float]]] = [
        [float("-inf")] * n for _ in range(n)
    ]
    vertices: List[int] = list(range(n))
    for _ in range(m):
        v1, v2, value = map(int, sys.stdin.readline().rstrip().split())
        v1 -= 1
        v2 -= 1
        adjacency[v1][v2] = max(value, adjacency[v1][v2])
        adjacency[v2][v1] = max(value, adjacency[v2][v1])
    try:
        maximum_spanning_tree: List[Tuple[int, int]] = find_mst(
            adjacency, vertices
        )
        result: int = 0
        for v in maximum_spanning_tree:
            result += v[1]
        print(result)
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()
