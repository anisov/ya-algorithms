import sys
from typing import (
    List,
)


class GoldHeap:
    __slots__ = ("cost", "count")

    def __init__(self, cost: int, count: int):
        self.cost: int = cost
        self.count: int = count

    def __gt__(self, other) -> bool:
        return self.cost > other.cost

    def __lt__(self, other) -> bool:
        return not self.__gt__(other)


def main() -> None:
    capacity: int = int(input())
    heaps_count: int = int(input())
    gold_heaps: List[GoldHeap] = []
    for i in range(heaps_count):
        c, m = map(int, sys.stdin.readline().rstrip().split())
        gold_heaps.append(GoldHeap(cost=c, count=m))
    gold_heaps.sort(reverse=True)
    max_cost: int = 0
    for i in gold_heaps:
        if capacity == 0:
            break
        if capacity >= i.count:
            max_cost += i.cost * i.count
            capacity -= i.count
        else:
            max_cost += i.cost * capacity
            capacity = 0

    print(max_cost)


if __name__ == "__main__":
    main()
