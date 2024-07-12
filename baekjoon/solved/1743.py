import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M, K = map(int, input().split())
foods = [tuple(map(int, input().split())) for _ in range(K)]

floor = [[0 for _ in range(M)] for _ in range(N)]

for food in foods:
    floor[food[0] - 1][food[1] - 1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_size = 0


def dfs(y, x, cnt):
    floor[y][x] = 0
    cnt += 1

    for i in range(4):

        ny, nx = y + dy[i], x + dx[i]

        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue

        if floor[ny][nx]:
            cnt = dfs(ny, nx, cnt)

    return cnt


for food in foods:
    if floor[food[0] - 1][food[1] - 1]:
        size = dfs(food[0] - 1, food[1] - 1, 0)
        if size > max_size:
            max_size = size

print(max_size)
