import enum
import sys
from typing import (
    List,
    Dict,
    Tuple,
    Iterable,
)


class Colors(enum.Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


def dfs(
    adjacency: Dict[int, List[int]], start_vertex: int
) -> Iterable[Tuple[int, int]]:
    stack: List[int] = []
    colors: List[Colors] = [Colors.WHITE] * len(adjacency)
    stack.append(start_vertex)
    time: int = 0
    entry: List[int] = [0] * len(adjacency)
    leave: List[int] = [0] * len(adjacency)
    while stack:
        v: int = stack.pop()
        v_idx: int = v - 1
        if colors[v_idx] == Colors.WHITE:
            entry[v_idx] = time
            colors[v_idx] = Colors.GRAY
            stack.append(v)
            vs: List[int] = adjacency[v]
            for new_vertex in sorted(vs, reverse=True):
                if colors[new_vertex - 1] == Colors.WHITE:
                    stack.append(new_vertex)
            time += 1
        elif colors[v_idx] == Colors.GRAY:
            leave[v_idx] = time
            colors[v_idx] = Colors.BLACK
            time += 1
    return zip(entry, leave)


def main() -> None:
    m, n = map(int, input().split())
    adjacency: Dict[int, List[int]] = {v: [] for v in range(1, m + 1)}
    for _ in range(n):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        adjacency[v1].append(v2)
    result: Iterable[Tuple[int, int]] = dfs(adjacency, 1)
    for i in result:
        print(*i)


if __name__ == "__main__":
    main()
