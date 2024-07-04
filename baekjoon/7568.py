N = int(input())
people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

for i in range(N):
    w, h = people[i]
    cnt = 0
    for j in range(N):
        if i != j and w < people[j][0] and h < people[j][1]:
            cnt += 1
    print(cnt + 1, end=" ")
