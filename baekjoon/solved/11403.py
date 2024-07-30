import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

adj_list = [[] for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            adj_list[i].append(j)

for i in range(N):
    visited = [0 for _ in range(N)]

    queue = deque()
    queue.append(i)

    while queue:
        node = queue.popleft()

        for n in adj_list[node]:
            if not visited[n]:
                visited[n] = 1
                queue.append(n)

    print(" ".join(list(map(str, visited))))
