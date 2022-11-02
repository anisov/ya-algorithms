import sys


def main() -> None:
    n, m = map(int, input().split())
    dist = [[float("inf")] * n for _ in range(n)]

    for _ in range(m):
        v1, v2, value = map(int, sys.stdin.readline().rstrip().split())
        dist[v1 - 1][v2 - 1] = min(value, dist[v1 - 1][v2 - 1])
        dist[v2 - 1][v1 - 1] = min(value, dist[v2 - 1][v1 - 1])

    for i in range(n):
        dist[i][i] = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

    for row in dist:
        for i in row:
            print(i if i != float("inf") else -1, end=" ")
        print()


if __name__ == "__main__":
    main()
