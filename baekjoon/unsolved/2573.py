import sys
import copy
from collections import deque


input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
ice = []
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(M):
        if row[j] > 0:
            ice.append([i, j])

year = 0

dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]

while True:
    year += 1

    melt = [[0 for _ in range(M)] for _ in range(N)]

    for i, j in ice:

        # 상하좌우 0 개수 세서 melt에 저장
        cnt = 0

        for k in range(4):
            n = i + dn[k]
            m = j + dm[k]

            if 0 <= n < N and 0 <= m < M and graph[n][m] == 0:
                cnt += 1

        melt[i][j] = cnt

    # graph - melt
    for i, j in ice:

        if graph[i][j] == 0:
            continue

        left = graph[i][j] - melt[i][j]
        if left < 0:
            left = 0
        graph[i][j] = left

    # bfs
    queue = deque()
    not_visited = copy.deepcopy(graph)
    cnt = 0

    for i, j in ice:

        if not_visited[i][j]:
            cnt += 1

            # 첫 번째 빙산
            if cnt == 1:

                not_visited[i][j] = 0
                queue.append([i, j])

                while queue:
                    n, m = queue.popleft()

                    for k in range(4):
                        nn = n + dn[k]
                        nm = m + dm[k]

                        if 0 <= nn < N and 0 <= nm < M and not_visited[nn][nm]:
                            not_visited[nn][nm] = 0
                            queue.append([nn, nm])

            else:
                break

    if cnt == 1:
        continue
    elif cnt == 0:
        print(0)
    else:
        print(year)

    break
