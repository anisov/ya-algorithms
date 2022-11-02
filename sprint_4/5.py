from collections import defaultdict
from typing import (
    List,
    Dict,
)


def get_anagrams_index(data: List[str]) -> List[List[int]]:
    table: Dict[str, List[int]] = defaultdict(list)
    for idx, v in enumerate(data):
        key: str = "".join(sorted(list(v)))
        table[key].append(idx)
    return sorted(list(table.values()))


def main():
    _ = input()
    data: List[str] = input().split()
    result: List[List[int]] = get_anagrams_index(data)
    for i in result:
        print(*i, sep=" ")


if __name__ == "__main__":
    main()
