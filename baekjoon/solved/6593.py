import sys
from collections import deque

input = sys.stdin.readline

dl = [-1, 1, 0, 0, 0, 0]
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, -1, 1]

while True:
    L, R, C = map(int, input().split())

    if L == R == C == 0:
        break

    building = []

    for l in range(L):
        rows = []
        for r in range(R):
            row = list(input().rstrip())
            for c in range(C):
                if row[c] == "S":
                    S = (l, r, c)
            rows.append(row)
        input()
        building.append(rows)

    queue = deque()
    queue.append(S)
    building[S[0]][S[1]][S[2]] = 0

    while queue:
        l, r, c = queue.popleft()

        for i in range(6):
            nl = l + dl[i]
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:

                if building[nl][nr][nc] == "E":
                    building[nl][nr][nc] = building[l][r][c] + 1
                    break

                if building[nl][nr][nc] == ".":
                    queue.append((nl, nr, nc))
                    building[nl][nr][nc] = building[l][r][c] + 1

    if building[E[0]][E[1]][E[2]] == "E":
        print("Trapped!")
    else:
        print(f"Escaped in {building[E[0]][E[1]][E[2]]} minute(s).")
