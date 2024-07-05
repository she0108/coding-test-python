N = int(input())
score = []
for _ in range(N):
    score.append(int(input()))

cnt = 0
for i in range(N - 1, 0, -1):
    if score[i - 1] >= score[i]:
        cnt += score[i - 1] - score[i] + 1
        score[i - 1] = score[i] - 1

print(cnt)
