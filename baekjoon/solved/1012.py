import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y, visited):
    visited.append((x, y))
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (nx, ny) in B and (nx, ny) not in visited:
            dfs(nx, ny, visited)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    B = [tuple(map(int, input().split())) for _ in range(K)]

    visited = []
    cnt = 0

    for bx, by in B:
        if (bx, by) not in visited:
            dfs(bx, by, visited)
            cnt += 1

    print(cnt)


# import sys
# from collections import deque

# input = sys.stdin.readline

# T = int(input())

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def BFS(x, y):
#     queue = deque([(x, y)])
#     matrix[x][y] = 0

#     while queue:
#         cx, cy = queue.popleft()
#         for i in range(4):
#             nx = cx + dx[i]
#             ny = cy + dy[i]

#             if nx < 0 or nx >= M or ny < 0 or ny >= N:
#                 continue

#             if matrix[nx][ny] == 1:
#                 queue.append((nx, ny))
#                 matrix[nx][ny] = 0


# for _ in range(T):
#     M, N, K = map(int, input().split())
#     matrix = [[0] * N for _ in range(M)]
#     cnt = 0

#     for _ in range(K):
#         x, y = map(int, input().split())
#         matrix[x][y] = 1

#     for x in range(M):
#         for y in range(N):
#             if matrix[x][y] == 1:
#                 BFS(x, y)
#                 cnt += 1

#     print(cnt)
