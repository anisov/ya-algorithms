from typing import (
    List,
    Set,
)


def find_pattern_indexes(
    measurements: List[int],
    pattern: List[int],
) -> List[int]:
    indexes: List[int] = []
    for i in range(len(pattern) - 1, len(measurements)):
        offset: int = i - (len(pattern) - 1)
        measurements_slice: List[int] = measurements[offset : i + 1]
        diff: Set[int] = set(
            (x - y for x, y in zip(measurements_slice, pattern))
        )
        if len(diff) == 1:
            indexes.append(offset + 1)
    return indexes


def main() -> None:
    _ = int(input())
    measurements: List[int] = list(map(int, input().split()))
    _ = int(input())
    pattern: List[int] = list(map(int, input().split()))
    print(*find_pattern_indexes(measurements, pattern))


if __name__ == "__main__":
    main()
