from collections import defaultdict

v, e = map(int, input().split())
edges = []

for i in range(e):
    v1, v2 = map(int, input().split())
    edges.append((v1, v2))

adjacency = defaultdict(list)

for i in edges:
    adjacency[i[0]].append(i[1])

for i in range(1, v + 1):
    if adjacency.get(i):
        data = adjacency[i]
        print(len(data), *sorted(data))
    else:
        print(0)
