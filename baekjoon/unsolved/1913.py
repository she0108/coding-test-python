N = int(input())
K = int(input())

grid = [[0 for _ in range(N)] for _ in range(N)]

i = N // 2
j = N // 2
grid[i][j] = 1
x, y = i + 1, j + 1

num = 2
for n in range(1, N // 2 + 1):
    i -= 1
    grid[i][j] = num
    num += 1
    for _ in range(n * 2 - 1):
        j += 1
        grid[i][j] = num
        if K == num:
            x, y = i + 1, j + 1
        num += 1
    for _ in range(n * 2):
        i += 1
        grid[i][j] = num
        if K == num:
            x, y = i + 1, j + 1
        num += 1
    for _ in range(n * 2):
        j -= 1
        grid[i][j] = num
        if K == num:
            x, y = i + 1, j + 1
        num += 1
    for _ in range(n * 2):
        i -= 1
        grid[i][j] = num
        if K == num:
            x, y = i + 1, j + 1
        num += 1

for i in range(N):
    for j in range(N):
        print(grid[i][j], end=" ")
    print()
print(x, y)
