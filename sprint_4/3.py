import sys
from typing import (
    Dict,
    List,
    Tuple,
)


def get_society_unique_names():
    data: Dict[str, int] = {}
    length: int = int(input())
    for i in range(length):
        v: str = sys.stdin.readline().rstrip()
        if data.get(v) is None:
            data[v] = i
    result: List[Tuple[str, int]] = list(data.items())
    result.sort(key=lambda x: x[1])
    for i in result:
        print(i[0])


get_society_unique_names()
