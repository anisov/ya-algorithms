from typing import List


def main() -> None:
    n: int = int(input())
    cost: List[int] = list(map(int, input().split()))
    result: int = 0
    for i in range(n):
        if i < len(cost) - 1 and cost[i] < cost[i + 1]:
            result += cost[i + 1] - cost[i]
    print(result)


if __name__ == "__main__":
    main()
