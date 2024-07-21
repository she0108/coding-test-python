import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def get_safe(y, x):

    if matrix[y][x]:
        return 0

    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()

    queue.append((y, x, 0))
    visited[y][x] = 1

    while queue:
        y, x, d = queue.popleft()

        for i in range(8):

            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if visited[ny][nx]:
                continue

            if matrix[ny][nx]:
                return d + 1

            queue.append((ny, nx, d + 1))
            visited[ny][nx] = 1


max_safe = 0

for i in range(N):
    for j in range(M):
        safe = get_safe(i, j)
        if safe > max_safe:
            max_safe = safe

print(max_safe)


# 다른 풀이 도전
