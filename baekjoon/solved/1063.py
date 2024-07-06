import sys

input = sys.stdin.readline

king, dol, N = input().split()

king = list(king)
king = [ord(king[0]) - 65, int(king[1]) - 1]

dol = list(dol)
dol = [ord(dol[0]) - 65, int(dol[1]) - 1]

N = int(N)

move = {
    "R": (1, 0),
    "L": (-1, 0),
    "B": (0, -1),
    "T": (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1),
}

for _ in range(N):
    direction = input().rstrip()
    kx = king[0] + move[direction][0]
    ky = king[1] + move[direction][1]
    if (not 0 <= kx <= 7) or (not 0 <= ky <= 7):
        continue
    if kx == dol[0] and ky == dol[1]:
        dx = dol[0] + move[direction][0]
        dy = dol[1] + move[direction][1]
        if (not 0 <= dx <= 7) or (not 0 <= dy <= 7):
            continue
        dol = [dx, dy]
    king = [kx, ky]

print(chr(king[0] + 65), king[1] + 1, sep="")
print(chr(dol[0] + 65), dol[1] + 1, sep="")
