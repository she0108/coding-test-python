import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]

doyeon = (0, 0)

for i in range(N):
    for j in range(M):
        if campus[i][j] == "I":
            doyeon = (i, j)

# BFS

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

queue = deque()
queue.append(doyeon)
campus[doyeon[0]][doyeon[1]] = "X"

cnt = 0

while queue:
    y, x = queue.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if (not 0 <= ny < N) or (not 0 <= nx < M):
            continue

        if campus[ny][nx] == "X":
            continue

        if campus[ny][nx] == "P":
            cnt += 1

        queue.append((ny, nx))
        campus[ny][nx] = "X"

# DFS


def dfs(y, x, cnt):

    if (not 0 <= y < N) or (not 0 <= x < M):
        return cnt

    if campus[y][x] == "X":
        return cnt

    if campus[y][x] == "P":
        cnt += 1

    campus[y][x] = "X"

    cnt = dfs(y - 1, x, cnt)
    cnt = dfs(y + 1, x, cnt)
    cnt = dfs(y, x - 1, cnt)
    cnt = dfs(y, x + 1, cnt)

    return cnt


cnt = dfs(doyeon[0], doyeon[1], 0)


if cnt == 0:
    print("TT")
else:
    print(cnt)
