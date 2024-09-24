N, M = map(int, input().split())
num = list(map(int, input().split()))

summ = num[0]
start, end = 0, 0
cnt = 0

while True:
    if summ < M:
        end += 1
        if end >= N:
            break
        summ += num[end]
    elif summ > M:
        summ -= num[start]
        start += 1
    else:
        cnt += 1
        summ -= num[start]
        start += 1
        # end += 1
        # if end >= N:
        #     break
        # summ += num[end]

print(cnt)
