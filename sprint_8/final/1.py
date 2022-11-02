# 69500307
# Сначала необходимо распаковать строку, для этого воспользуемся стеком.
# После распаковки будем искать максимальный общий префикс, для этого
# необходимо поочерёдно сравнивать две строки итерируясь по символам, пока не
# будет найдена общая последовательность, каждый раз уменьшая сравниваемою
# строку на один символ, до тех пор, пока она не совпадёт с той строкой с
# которой идёт сравнение.
# Временная сложность: O(n) - распаковка строки.
# Поиск максимального префикса O(n*m), где m длина максимальной строки.
# Пространственная сложность: O(m), где m длина максимальной строки.

import sys
from typing import List


def get_unpack_string(s: str) -> str:
    stack: List[str] = []
    for char in s:
        if char == "]":
            data: List[str] = []
            while True:
                stack_char: str = stack.pop()
                if stack_char == "[":
                    break
                data.append(stack_char)
            data.reverse()
            count: int = int(stack.pop())
            stack.append("".join(data * count))
        else:
            stack.append(char)
    return "".join(stack)


def find_max_prefix(s1: str, s2: str) -> str:
    result: str = s1
    while s2.find(result) != 0:
        result = result[:-1]
    return result


def main() -> None:
    count: int = int(input())
    prefix: str = get_unpack_string(input())
    for i in range(count - 1):
        prefix = find_max_prefix(
            prefix, get_unpack_string(sys.stdin.readline().rstrip())
        )
    print(prefix)


if __name__ == "__main__":
    main()
