N, M = map(int, input().split())

if N == 1:
    cnt = 1
elif N == 2:
    if M < 3:
        cnt = 1
    elif M < 5:
        cnt = 2
    elif M < 7:
        cnt = 3
    else:
        cnt = 4
else:
    if M < 2:
        cnt = 1
    elif M < 3:
        cnt = 2
    elif M < 4:
        cnt = 3
    elif M < 7:
        cnt = 4
    else:
        cnt = 5
        cur_x = 6
        cnt += M - 1 - cur_x

print(cnt)

# 다른 풀이
