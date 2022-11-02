from typing import List
import sys

lines: int = int(input())
columns: int = int(input())


def get_matrix(matrix_lines: int) -> List[List[str]]:
    matrix_data: List[List[str]] = []
    for _ in range(matrix_lines):
        line: str = sys.stdin.readline().rstrip()
        data: List[str] = line.split(" ")
        matrix_data.append(data)
    return matrix_data


matrix = get_matrix(matrix_lines=lines)
for i in range(columns):
    print(*[line[i] for line in matrix], sep=" ")
