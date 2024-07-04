import sys

N = int(input())
tips = [int(sys.stdin.readline()) for _ in range(N)]

tips.sort(reverse=True)

res = 0
for i in range(N):
    tip = tips[i] - i
    if tip > 0:
        res += tip

print(res)
