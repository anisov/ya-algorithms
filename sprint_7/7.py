import sys
from typing import (
    List,
    Tuple,
)


def get_max_subsequence(
    s1: List[int], s2: List[int]
) -> Tuple[int, List[int], List[int]]:
    dp: List[List[int]] = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    s1_indexes: List[int] = []
    s2_indexes: List[int] = []
    i = len(s1)
    j = len(s2)
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            s1_indexes.append(i)
            s2_indexes.append(j)
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            else:
                j -= 1
    s1_indexes.reverse()
    s2_indexes.reverse()
    return dp[-1][-1], s1_indexes, s2_indexes


def main() -> None:
    _ = int(input())
    s1 = list(map(int, sys.stdin.readline().strip().split()))
    _ = int(input())
    s2 = list(map(int, sys.stdin.readline().strip().split()))
    count, s1_indexes, s2_indexes = get_max_subsequence(s1=s1, s2=s2)
    print(count)
    if count:
        print(*s1_indexes)
        print(*s2_indexes)


if __name__ == "__main__":
    main()
