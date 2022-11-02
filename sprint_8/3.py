from typing import (
    List,
    Tuple,
)


def insert_strings(s: str, substrings: List[Tuple[str, int]]) -> str:
    s_list: List[str] = list(s)
    result: List[str] = []
    substrings.sort(key=lambda x: x[1])
    shift: int = 0
    for substring, index in substrings:
        result.extend(s_list[shift:index])
        result.extend(list(substring))
        shift = index
    if shift < len(s):
        result.extend(s[shift:])
    return "".join(result)


def main() -> None:
    s: str = input()
    n: int = int(input())
    substrings: List[Tuple[str, int]] = []
    for i in range(n):
        substring, index = list(input().split())
        substrings.append((substring, int(index)))
    print(insert_strings(s, substrings))


if __name__ == "__main__":
    main()
