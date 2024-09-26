import math

N = int(input())

dp = [float("inf")] * (N + 1)
dp[0] = 0

square_nums = [i**2 for i in range(1, int(math.sqrt(N)) + 1)]


for n in range(1, N + 1):
    for square in square_nums:
        if square > n:
            break
        dp[n] = min(dp[n], dp[n - square] + 1)

print(dp[N])
