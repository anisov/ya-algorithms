from typing import List


def prefix_function(s: str) -> List[int]:
    result: List[int] = [0] * len(s)
    for i in range(1, len(s)):
        k: int = result[i - 1]
        while k > 0 and s[k] != s[i]:
            k = result[k - 1]
        if s[k] == s[i]:
            k += 1
        result[i] = k
    return result


def main() -> None:
    print(*prefix_function(s=input()))


if __name__ == "__main__":
    main()
