N, B = map(int, input().split())

res = ""

while True:
    r = N % B
    d = N // B
    if r < 10:
        res = str(r) + res
    else:
        res = chr(r + 55) + res
    if d == 0:
        break
    N = d
print(res)

# res를 list로 하고 print(res, end="")
