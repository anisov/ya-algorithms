# 67909500
# Реализовано через стек(используется стандартный список Python, т.к. он
# подходит для решения). Для получения нужной операции создан словарь
# соответствий action, а для определения является ли строка числом используется
# стандартный метод isnumeric()
# Временная сложность: 0(1)
# Пространственная сложность: 0(n)

import math
from typing import (
    List,
    Callable,
    Dict,
)


def calculate(data: List[str]) -> int:
    stack: List[int] = []
    action: Dict[str, Callable[[int, int], int]] = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: math.floor(a / b),  # or //
        "*": lambda a, b: a * b,
    }
    for i in data:
        if i.lstrip("-").isnumeric():
            stack.append(int(i))
        else:
            second, first = stack.pop(), stack.pop()
            result: int = action[i](first, second)
            stack.append(result)
    return stack.pop()


def get_data() -> List[str]:
    return input().split()


def main():
    result: int = calculate(data=get_data())
    print(result)


if __name__ == "__main__":
    main()
