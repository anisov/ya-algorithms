from typing import (
    List,
    Dict,
)

number_symbols: Dict[int, str] = {
    2: "abc",
    3: "def",
    4: "ghi",
    5: "jkl",
    6: "mno",
    7: "pqrs",
    8: "tuv",
    9: "wxyz",
}

result = []


def combinations(nums: List[int], s: str = ""):
    if not nums:
        result.append(s)
        return
    symbols = number_symbols[nums[0]]
    for i in symbols:
        combinations(nums=nums[1:], s=s + i)


numbers: List[int] = list(map(int, list(input())))
combinations(nums=numbers)
print(*result, sep=" ")
