N = int(input())
P = map(int, input().split())

S = sorted(P, reverse=True)
res = 0

for i, t in enumerate(S):
    res += (i + 1) * t

print(res)
