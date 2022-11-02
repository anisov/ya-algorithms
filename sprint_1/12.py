from typing import List

a: List[str] = list(input())
b: List[str] = list(input())
a.sort()
b.sort()
result = ""
for i, v in enumerate(a):
    if v != b[i]:
        result = b[i]
        break
if not result:
    result = b[-1]
print(result)
