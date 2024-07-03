T = int(input())

if T % 10 == 0:
    a = T // (60 * 5)
    T %= 60 * 5
    b = T // 60
    T %= 60
    c = T // 10
    print(a, b, c)
else:
    print(-1)
