import sys

input = sys.stdin.readline

N = int(input())
note = list(map(int, input().split()))
switch = [0 for _ in range(N)]


def toggle(i, arr):
    arr[i] = 1 - arr[i]
    if i + 1 < N:
        arr[i + 1] = 1 - arr[i + 1]
        if i + 2 < N:
            arr[i + 2] = 1 - arr[i + 2]
    return arr


cnt = 0

for i in range(N):
    if switch[i] != note[i]:
        toggle(i, switch)
        cnt += 1

print(cnt)
