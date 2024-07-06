N, L = map(int, input().split())
leaks = list(map(int, input().split()))

leaks.sort()
start = 0
end = 0
cnt = 0

for leak in leaks:
    if end < leak:
        start = leak
        end = leak + L - 1
        cnt += 1

print(cnt)
