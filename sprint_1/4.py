from typing import List

length: int = int(input())
data: List[int] = list(map(int, input().split(" ")))


def get_randomness(data: List[int]) -> int:
    if length == 1:
        return 1
    randomness = 0
    for i, v in enumerate(data):
        v: int = int(v)
        if i == 0 and v > data[i + 1]:
            randomness += 1
        elif length - 1 > i > 0 and data[i - 1] < v > data[i + 1]:
            randomness += 1
        elif i == length - 1 and v > data[i - 1]:
            randomness += 1
    return randomness


print(get_randomness(data=data))
