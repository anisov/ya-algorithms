from math import factorial

n = int(input())
print(factorial(2 * n) // (factorial(n + 1) * factorial(n)))
