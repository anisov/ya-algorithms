from typing import List

first_number = input()
second_number = input()


def sum_binary(a: str, b: str) -> str:
    num1: List[int] = list(map(int, a))[::-1]
    num2: List[int] = list(map(int, b))[::-1]
    size: int = max(len(num1), len(num2))
    num1 += [0] * (size - len(num1))
    num2 += [0] * (size - len(num2))
    result: List[str] = []
    remainder: int = 0
    for i in range(len(num1)):
        value = num1[i] + num2[i] + remainder
        remainder = value // 2
        result.append(str(value % 2))
    if remainder == 1:
        result += "1"
    return "".join(result[::-1])


print(sum_binary(first_number, second_number))
