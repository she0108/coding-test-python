N = int(input())
switch = [0] + list(map(int, input().split()))
M = int(input())


def toggle(n, arr):
    arr[n] = 1 - arr[n]
    return


for _ in range(M):
    s, n = map(int, input().split())
    if s == 1:
        k = n
        while k <= N:
            toggle(k, switch)
            k += n
    else:
        toggle(n, switch)
        r = 1
        while True:
            if (n - r) < 1 or (n + r) > N:
                break
            if switch[n - r] != switch[n + r]:
                break
            toggle(n - r, switch)
            toggle(n + r, switch)
            r += 1

for i in range(1, N + 1):
    if i % 20 == 0:
        print(switch[i])
    else:
        print(switch[i], end=" ")
