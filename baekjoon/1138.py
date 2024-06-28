N = int(input())
nums = list(map(int, input().split()))
line = [0] * N

for i in range(N):
    j = 0
    tall = 0
    while line[j] != 0:
        j += 1
    while tall < nums[i]:
        j += 1
        tall += 1
        while line[j] != 0:
            j += 1
    line[j] = i + 1

for l in line:
    print(l, end=" ")


# TODO: 키가 큰 사람부터 하는 것도 구현해볼 것
