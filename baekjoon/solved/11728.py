SIZE_A, SIZE_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b = 0, 0
result = []

while a < SIZE_A and b < SIZE_B:
    if A[a] < B[b]:
        result.append(A[a])
        a += 1
    else:
        result.append(B[b])
        b += 1

while a < SIZE_A:
    result.append(A[a])
    a += 1

while b < SIZE_B:
    result.append(B[b])
    b += 1

print(*result)
