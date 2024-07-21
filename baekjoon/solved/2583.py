import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            if graph[y][x] == 0:
                graph[y][x] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = []

for y in range(M):
    for x in range(N):
        if graph[y][x] == 0:

            # cnt = 1
            # queue = deque()
            # queue.append((x, y))
            # graph[y][x] = 1

            # while queue:
            #     cx, cy = queue.popleft()

            #     for i in range(4):
            #         nx, ny = cx + dx[i], cy + dy[i]

            #         if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
            #             queue.append((nx, ny))
            #             graph[ny][nx] = 1
            #             cnt += 1

            cnt = 1
            stack = deque()
            stack.append((x, y))
            graph[y][x] = 1

            while stack:
                cx, cy = stack.pop()

                for i in range(4):
                    nx, ny = cx + dx[i], cy + dy[i]

                    if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                        stack.append((nx, ny))
                        graph[ny][nx] = 1
                        cnt += 1

            res.append(cnt)

res.sort()
print(len(res))
print(" ".join(map(str, res)))
