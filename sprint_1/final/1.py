# 67474665
# Временная сложность: 2n

from dataclasses import dataclass
from typing import List


@dataclass
class StreetData:
    length: int
    sites: List[int]


def get_data() -> StreetData:
    length: int = int(input())
    street_sites: List[int] = list(map(int, input().split(" ")))
    return StreetData(length=length, sites=street_sites)


def get_distance(street_data: StreetData) -> List[int]:
    result: List[int] = [0] * street_data.length
    right_zero_find: bool = False
    for i in range(street_data.length):
        if street_data.sites[i] == 0:
            right_zero_find = True
        if street_data.sites[i] and right_zero_find:
            result[i] = result[i - 1] + 1
    left_zero_find: bool = False
    for i in range(street_data.length - 1, -1, -1):
        if street_data.sites[i] == 0:
            left_zero_find = True
        if street_data.sites[i] and left_zero_find:
            if result[i] == 0:
                result[i] = result[i + 1] + 1
            result[i] = min(result[i], result[i + 1] + 1)
    return result


def print_output_data(output_data: List[int]) -> None:
    print(*output_data, sep=" ")


if __name__ == "__main__":
    data: StreetData = get_data()
    distance: List[int] = get_distance(street_data=data)
    print_output_data(output_data=distance)
