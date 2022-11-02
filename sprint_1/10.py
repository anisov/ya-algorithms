from typing import List
import math

number = int(input())


def get_prime_value(num: int) -> int:
    if num == 1:
        return num
    for n in range(2, int(math.sqrt(num)) + 1):
        if (num % n) == 0:
            return n
    return num


result: List[str] = []
while True:
    value = get_prime_value(number)
    if value == number:
        result.append(str(value))
        break
    result.append(str(value))
    number = int(number / value)
print(" ".join(result))
