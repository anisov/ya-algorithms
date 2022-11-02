import sys
from typing import List


def get_clumbs_segments(data: List[List[int]]):
    data.sort()
    result: List[str] = []
    start: int = data[0][0]
    end: int = data[0][1]
    for i in data[1:]:
        if end < i[0]:
            result.append(f"{start} {end}")
            start = i[0]
            end = i[1]
        elif i[1] > end:
            end = i[1]
    result.append(f"{start} {end}")
    return result


def get_data() -> List[List[int]]:
    count: int = int(input())
    result: List[List[int]] = []
    for _ in range(count):
        data: List[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        result.append(data)
    return result


print(*get_clumbs_segments(get_data()), sep="\n")
