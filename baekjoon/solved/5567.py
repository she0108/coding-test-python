import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
friends = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

# visited = [-1 for _ in range(n + 1)]

# queue = deque()

# queue.append(1)
# visited[1] = 0
# cnt = 0

# while queue:
#     num = queue.popleft()

#     if visited[num] == 2:
#         continue

#     for friend in friends[num]:
#         if visited[friend] == -1:
#             queue.append(friend)
#             visited[friend] = visited[num] + 1
#             cnt += 1

# print(cnt)


visited = [0 for _ in range(n + 1)]
visited[1] = 1
cnt = 0

for i in friends[1]:
    visited[i] = 1
    cnt += 1

for i in friends[1]:
    for j in friends[i]:
        if not visited[j]:
            visited[j] = 1
            cnt += 1

print(cnt)
