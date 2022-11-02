# 67299795
# Временная сложность: 2n

import sys
from collections import defaultdict
from typing import (
    List,
    Dict,
)

click_count: int = int(input()) * 2
line_count: int = 4

data: List[str] = []
for i in range(line_count):
    line: List[str] = list(sys.stdin.readline().rstrip())
    data.extend(line)

number_counts: Dict[str, int] = defaultdict(int)

for i in data:
    if i != ".":
        number_counts[i] += 1

result = 0
for repeat in number_counts.values():
    if repeat <= click_count:
        result += 1

print(result)
