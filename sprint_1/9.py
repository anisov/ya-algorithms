number: int = int(input())
result: bool = True
while result is True and number != 1:
    remainder: int = number % 4
    if remainder:
        result = False
    else:
        number = int(number / 4)
print(result)
