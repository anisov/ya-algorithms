from typing import List

number: int = int(input())
result: List[str] = []

while number != 1:
    result.append(str(number % 2))
    number = number // 2

result.append(str(1))
result.reverse()

print("".join(result))
