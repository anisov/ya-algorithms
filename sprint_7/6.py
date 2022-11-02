import sys
from typing import List


def get_max_field_points(n: int, m: int, points: List[List[int]]) -> int:
    dp = [[0] * (m + 1)] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + points[i - 1][j - 1]
    return dp[-1][-1]


def main() -> None:
    n, m = list(map(int, input().split()))
    points: List[List[int, int]] = []
    for i in range(n):
        points.append(list(map(int, list(sys.stdin.readline().strip()))))
    points.reverse()
    print(get_max_field_points(n=n, m=m, points=points))


if __name__ == "__main__":
    main()
