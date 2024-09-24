import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

partial_sum = [0] * N
partial_sum[0] = A[0]

for i in range(1, N):
    max_partial_sum = 0
    for j in range(0, i):
        if A[j] < A[i] and partial_sum[j] > max_partial_sum:
            max_partial_sum = partial_sum[j]

    partial_sum[i] = max_partial_sum + A[i]

print(max(partial_sum))
