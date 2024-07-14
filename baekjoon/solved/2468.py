from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

max_height = 1
min_height = 100
for row in data:
    if max(row) > max_height:
        max_height = max(row)
    if min(row) < min_height:
        min_height = min(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_cnt = 1

for rain in range(min_height, max_height):

    graph = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if data[i][j] > rain:
                graph[i][j] = 1

    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j]:

                q = deque()
                q.append((i, j))

                while q:
                    y, x = q.popleft()

                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]

                        if 0 <= ny < N and 0 <= nx < N:
                            if graph[ny][nx]:
                                graph[ny][nx] = 0
                                q.append((ny, nx))

                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)
