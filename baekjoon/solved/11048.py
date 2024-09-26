import sys

input = sys.stdin.readline


N, M = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):

        max_candy = 0

        if j > 0 and i > 0 and dp[i - 1][j - 1] > max_candy:
            max_candy = dp[i - 1][j - 1]

        if j > 0 and dp[i][j - 1] > max_candy:
            max_candy = dp[i][j - 1]

        if i > 0 and dp[i - 1][j] > max_candy:
            max_candy = dp[i - 1][j]

        dp[i][j] = max_candy + maze[i][j]

print(dp[N - 1][M - 1])

# dp 배열이 꼭 필요한가?
