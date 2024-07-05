N = int(input())
trees = list(map(int, input().split()))

trees.sort(reverse=True)

for i in range(N):
    trees[i] -= N - i - 1

if max(trees) > 0:
    print(1 + N + max(trees))
else:
    print(1 + N)


# N = int(input())
# trees = list(map(int, input().split()))

# trees.sort(reverse=True)

# day = 0
# for i in range(N):
#     t = 1 + i + trees[i]
#     if t > day:
#         day = t

# if max(trees) > 0:
#     print(1 + N + max(trees))
# else:
#     print(1 + N)
