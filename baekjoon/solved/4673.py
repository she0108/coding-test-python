def d(n):
    res = n
    while n != 0:
        res += n % 10
        n //= 10
    return res


nums = [0 for x in range(10001)]
res = []

for n in range(1, 10001):
    if d(n) <= 10000:
        nums[d(n)] = 1
    if nums[n] == 0:
        res.append(n)

for r in res:
    print(r)
