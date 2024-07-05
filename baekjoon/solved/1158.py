N, K = map(int, input().split())

num = [x for x in range(1, N + 1)]
res = []

i = K - 1
while True:
    res.append(num.pop(i))
    l = len(num)
    if l == 0:
        break
    i = (i + K - 1) % l

print("<", end="")
print(str(res)[1:-1], end="")
print(">")
