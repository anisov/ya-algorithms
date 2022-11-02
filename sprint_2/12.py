from typing import List

n, k = list(map(int, input().split(" ")))
cached: List[int] = [1, 1]
division_value: int = 10**k
while n > 1:
    n -= 1
    result = (cached[0] + cached[1]) % division_value
    cached[0] = cached[1]
    cached[1] = result
fib = cached[1]
print(fib)
