import sys
from collections import deque

input = sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())

for _ in range(T):
    I = int(input())
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))

    board = [[-1 for _ in range(I)] for _ in range(I)]

    queue = deque()
    res = 0

    board[start[0]][start[1]] = 0
    queue.append(start)

    while queue:
        x, y = queue.popleft()

        if [x, y] == target:
            res = board[x][y]
            break

        cnt = board[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I:
                if board[nx][ny] == -1 or cnt + 1 < board[nx][ny]:
                    board[nx][ny] = cnt + 1
                    queue.append([nx, ny])

    print(res)
