from typing import List

length: int = int(input())
data: List[str] = input().split(" ")

max_length: int = 0
max_length_world: str = ""

for i in data:
    world_length: int = len(i)
    if world_length > max_length:
        max_length = world_length
        max_length_world = i

print(max_length_world, max_length, sep="\n")
