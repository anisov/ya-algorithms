from typing import List


def main() -> None:
    m, k = map(int, input().split())
    dp: List[int] = [0] * m
    dp[0] = 1
    mod: int = 10**9 + 7
    for i in range(m):
        for j in range(1, min(k + 1, i + 1)):
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i - j]) % mod
    print(dp[-1])


if __name__ == "__main__":
    main()
