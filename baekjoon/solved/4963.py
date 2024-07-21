import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(y, x, graph):

    graph[y][x] = 0

    for i in range(8):

        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue

        if graph[ny][nx]:
            dfs(ny, nx, graph)


while True:

    W, H = map(int, input().split())

    if (W, H) == (0, 0):
        break

    graph = [list(map(int, input().split())) for _ in range(H)]

    cnt = 0

    for i in range(H):
        for j in range(W):
            if graph[i][j]:
                dfs(i, j, graph)
                cnt += 1

    print(cnt)
