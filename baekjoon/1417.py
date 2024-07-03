N = int(input())
dasom = int(input())
votes = [-1, -1]
for _ in range(N - 1):
    votes.append(int(input()))

cnt = 0
while True:
    max_v = max(votes)
    if dasom > max_v:
        break
    for i in range(2, N + 1):
        if votes[i] == max_v:
            votes[i] -= 1
            dasom += 1
            cnt += 1
            if dasom > max(votes):
                break

print(cnt)
