import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

field = []
sheep = []
wolf = []

cnt_sheep = 0
cnt_wolf = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(R):
    row = list(input().rstrip())
    field.append(row)
    for j in range(C):
        if row[j] == "o":
            sheep.append([i, j])
        elif row[j] == "v":
            wolf.append([i, j])

for oy, ox in sheep:

    if field[oy][ox] != "o":
        continue

    cnt_o = 1
    cnt_v = 0

    queue = deque()
    queue.append([oy, ox])
    field[oy][ox] = "#"

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < R and 0 <= nx < C:
                if field[ny][nx] == "#":
                    continue

                if field[ny][nx] == "o":
                    cnt_o += 1
                elif field[ny][nx] == "v":
                    cnt_v += 1

                field[ny][nx] = "#"
                queue.append([ny, nx])

    if cnt_o > cnt_v:
        cnt_sheep += cnt_o
    else:
        cnt_wolf += cnt_v

for vy, vx in wolf:

    if field[vy][vx] == "v":
        cnt_wolf += 1

print(cnt_sheep, cnt_wolf)
