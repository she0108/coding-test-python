import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
E = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

queue = deque()
visited = [0 for _ in range(N + 1)]

queue.append(1)
visited[1] = 1
cnt = 0

while queue:
    node = queue.popleft()
    for n in E[node]:
        if visited[n] == 0:
            queue.append(n)
            visited[n] = 1
            cnt += 1

print(cnt)
