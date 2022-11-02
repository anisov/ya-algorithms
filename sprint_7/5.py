from typing import List


def get_money_combinations(target_sum: int, coins: List[int]) -> int:
    combinations = [0 for _ in range(target_sum + 1)]
    combinations[0] = 1
    for coin in coins:
        for j in range(len(combinations)):
            if j >= coin:
                combinations[j] += combinations[j - coin]
    return combinations[target_sum]


def main() -> None:
    target_sum: int = int(input())
    _: int = int(input())
    coins: List[int] = list(map(int, input().split()))
    print(get_money_combinations(target_sum, coins))


if __name__ == "__main__":
    main()
