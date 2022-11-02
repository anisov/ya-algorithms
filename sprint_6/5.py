import enum
import sys
from typing import (
    List,
    Dict,
)


class Colors(enum.Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


def _sort(
    start_vertex: int,
    adjacency: Dict[int, List[int]],
    colors: List[Colors],
) -> List[int]:
    stack_sort: List[int] = []
    stack = [start_vertex]
    while stack:
        v: int = stack.pop()
        v_idx: int = v - 1
        if colors[v_idx] == Colors.WHITE:
            colors[v_idx] = Colors.GRAY
            stack.append(v)
            vs: List[int] = adjacency[v]
            for new_vertex in sorted(vs, reverse=True):
                if colors[new_vertex - 1] == Colors.WHITE:
                    stack.append(new_vertex)
        elif colors[v_idx] == Colors.GRAY:
            colors[v_idx] = Colors.BLACK
            stack_sort.append(v)
    return stack_sort


def sort(adjacency: Dict[int, List[int]]) -> List[int]:
    result: List[int] = []
    colors: List[Colors] = [Colors.WHITE] * len(adjacency)
    for i in range(1, len(adjacency) + 1):
        result.extend(
            _sort(start_vertex=i, adjacency=adjacency, colors=colors)
        )
    return list(reversed(result))


def main() -> None:
    m, n = map(int, input().split())
    adjacency: Dict[int, List[int]] = {v: [] for v in range(1, m + 1)}
    for _ in range(n):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        adjacency[v1].append(v2)
    result: List[int] = sort(adjacency)
    print(*result)


if __name__ == "__main__":
    main()
