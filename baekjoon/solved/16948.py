from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

board = [[-1 for _ in range(N)] for _ in range(N)]

queue = deque()
queue.append((r1, c1))
board[r1][c1] = 0

while queue:
    r, c = queue.popleft()

    if (r, c) == (r2, c2):
        break

    for i in range(6):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == -1:
            board[nr][nc] = board[r][c] + 1
            queue.append((nr, nc))

print(board[r2][c2])
