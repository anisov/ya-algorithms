v, e = map(int, input().split())

adjacency = [[0] * v for _ in range(v)]

for i in range(e):
    v1, v2 = map(int, input().split())
    adjacency[v1 - 1][v2 - 1] = 1

for i in adjacency:
    print(*i)
