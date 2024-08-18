import sys

input = sys.stdin.readline

N, M = map(int, input().split())
res = 0

floor = [input().rstrip() for _ in range(N)]
for row in floor:
    boards = row.split("|")
    while "" in boards:
        boards.remove("")
    res += len(boards)

floor_reverse = [[0 for _ in range(N)] for _ in range(M)]
for i in range(N):
    for j in range(M):
        floor_reverse[j][i] = floor[i][j]

for col in floor_reverse:
    boards = "".join(col).split("-")
    while "" in boards:
        boards.remove("")
    res += len(boards)

print(res)
