N, S = map(int, input().split())
num = list(map(int, input().split()))

sum_list = [0 for _ in range(N)]

part_sum = 0
for i in range(N):
    part_sum += num[i]
    sum_list[i] = part_sum

cnt = 0
for start in range(N):
    for end in range(start, N):

        if start == 0:
            seq_sum = sum_list[end]
        else:
            seq_sum = sum_list[end] - sum_list[start - 1]

        if seq_sum == S:
            cnt += 1

print(cnt)

# 문제 잘못 이해해서 틀림
