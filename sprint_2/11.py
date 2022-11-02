def factorial(n: int):
    if n in {0, 1}:
        return 1
    return factorial(n - 1) + factorial(n - 2)


number: int = int(input())
print(factorial(number))
