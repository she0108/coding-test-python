n = int(input())

if (n % 5) % 2 == 0:
    cnt = n // 5 + (n % 5) // 2
    print(cnt)
else:
    if n // 5 == 0:
        print(-1)
    else:
        cnt = (n // 5 - 1) + (n % 5 + 5) // 2
        print(cnt)
