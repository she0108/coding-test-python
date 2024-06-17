import math

M = int(input())
N = int(input())

s = math.ceil(M ** (1 / 2))
e = math.floor(N ** (1 / 2))

res = 0
for i in range(s, e + 1):
    res += i**2

if res == 0:
    print(-1)
else:
    print(res)
    print(s**2)
