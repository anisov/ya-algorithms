from collections import defaultdict


def dfs(adjacency, start_vertex):
    stack = []
    visited = set()
    stack.append(start_vertex)
    result = []
    while stack:
        v = stack.pop()
        if v not in visited:
            result.append(v)
            visited.add(v)
            vs = adjacency[v]
            for new_vertex in reversed(sorted(vs)):
                stack.append(new_vertex)
    return result


def main():
    v_c, e_c = map(int, input().split())
    edges = []
    for i in range(e_c):
        v1, v2 = map(int, input().split())
        edges.append((v1, v2))
    adjacency = defaultdict(list)
    for i in edges:
        adjacency[i[0]].append(i[1])
        adjacency[i[1]].append(i[0])
    start_vertex = int(input())
    print(*dfs(adjacency, start_vertex))


main()
