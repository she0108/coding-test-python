N, M = map(int, input().split())
J = int(input())
apples = [int(input()) for _ in range(J)]

left = 1
right = M
d = 0

for apple in apples:
    if left <= apple <= right:
        continue
    if apple < left:
        move = left - apple
        left = apple
        right -= move
    else:
        move = apple - right
        left += move
        right = apple
    d += move

print(d)
