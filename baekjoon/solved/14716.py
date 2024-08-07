import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(M)]

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

cnt = 0

for i in range(M):
    for j in range(N):
        if banner[i][j] == 1:

            cnt += 1

            queue = deque()
            queue.append((i, j))
            banner[i][j] = 0

            while queue:
                y, x = queue.popleft()

                for k in range(8):
                    ny = y + dy[k]
                    nx = x + dx[k]

                    if 0 <= ny < M and 0 <= nx < N and banner[ny][nx] == 1:
                        queue.append((ny, nx))
                        banner[ny][nx] = 0

print(cnt)
