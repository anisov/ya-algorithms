import sys
from typing import List


def get_matrix(matrix_lines: int) -> List[str]:
    matrix: List[str] = []
    for i in range(matrix_lines):
        line: str = sys.stdin.readline().rstrip()
        data: List[str] = line.split(" ")
        matrix.append(data)
    return matrix


matrix_lines: int = int(input())
matrix_columns: int = int(input())
matrix: List[str] = get_matrix(matrix_lines)
line_pos: int = int(input())
column_pos: int = int(input())
neighbours: List[str] = []

if matrix_columns > 1:
    matrix_line: str = matrix[line_pos]
    if column_pos == 0:
        neighbours.append(matrix_line[column_pos + 1])
    elif column_pos == matrix_columns - 1:
        neighbours.append(matrix_line[column_pos - 1])
    else:
        neighbours.append(matrix_line[column_pos + 1])
        neighbours.append(matrix_line[column_pos - 1])

if matrix_lines > 1:
    if line_pos == 0:
        matrix_line = matrix[line_pos + 1]
        neighbours.append(matrix_line[column_pos])
    elif line_pos == matrix_lines - 1:
        matrix_line = matrix[line_pos - 1]
        neighbours.append(matrix_line[column_pos])
    else:
        matrix_line = matrix[line_pos + 1]
        neighbours.append(matrix_line[column_pos])
        matrix_line = matrix[line_pos - 1]
        neighbours.append(matrix_line[column_pos])

neighbours.sort(key=int)
print(" ".join(neighbours))
