board = [input().split() for _ in range(5)]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

res = set()


def dfs(i, j, n):

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if ni < 0 or ni > 4 or nj < 0 or nj > 4:
            continue

        num = n + board[ni][nj]

        if len(num) == 6:
            res.add(num)
        else:
            dfs(ni, nj, num)


for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(res))
