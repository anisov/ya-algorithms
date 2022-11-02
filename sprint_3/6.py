from typing import List

_ = input()
numbers: List[str] = list(input().split())


def compare(first_value: str, second_value: str) -> bool:
    return int(first_value + second_value) > int(second_value + first_value)


def sort_nums(nums: List[str]):
    for i, v in enumerate(nums):
        j: int = i
        while j > 0 and compare(v, nums[j - 1]):
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = v


sort_nums(nums=numbers)
print(*numbers, sep="")
