import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

virus_able = []
base_graph = []
min_time = N**2

for x in range(N):
    row = list(map(int, input().split()))
    for y in range(N):
        if row[y] == 2:
            virus_able.append([x, y])
            row[y] = -1
        elif row[y] == 0:
            row[y] = -1
    base_graph.append(row)

combination = list(combinations(virus_able, M))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for combi in combination:

    graph = [row[:] for row in base_graph]
    queue = deque()
    time = 0

    for virus in combi:
        graph[virus[0]][virus[1]] = 0
        queue.append(virus)

    while queue:
        cx, cy = queue.popleft()
        t = graph[cx][cy]

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == -1 or (t + 1) < graph[nx][ny]:
                    graph[nx][ny] = t + 1
                    queue.append([nx, ny])

                    if t + 1 > time:
                        time = t + 1

    for x in range(N):
        for y in range(N):
            if graph[x][y] == -1:
                time = N**2

    if time < min_time:
        min_time = time

if min_time == N**2:
    print(-1)
else:
    print(min_time)
