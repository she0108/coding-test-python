import sys

input = sys.stdin.readline

N, M = map(int, input().split())
price = [tuple(map(int, input().split())) for _ in range(M)]

min_6 = 1000
min_1 = 1000
for p in price:
    if p[0] < min_6:
        min_6 = p[0]
    if p[1] < min_1:
        min_1 = p[1]

if min_6 > min_1 * 6:
    min_6 = min_1 * 6

res1 = min(min_6, min_1 * 6) * (N // 6)
res2 = min((N % 6) * min_1, min_6)

print(res1 + res2)
