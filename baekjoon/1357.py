def rev(num):
    res = 0
    while num != 0:
        res *= 10
        res += num % 10
        num //= 10
    return res


X, Y = map(int, input().split())
print(rev(rev(X) + rev(Y)))
