from typing import List

length: int = int(input())
data: List[str] = input().split(" ")
second_number: int = int(input())
first_number: int = int("".join(data))
result: str = str(first_number + second_number)

print(*result)
