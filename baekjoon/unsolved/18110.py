import sys

input = sys.stdin.readline


n = int(input())
ops = [int(input()) for _ in range(n)]

if n == 0:
    print(0)
else:
    ops.sort()
    exc = round(n * 15 / 100)
    s = 0
    for i in range(exc, n - exc):
        s += ops[i]
    print(round(s / (n - exc * 2)))
