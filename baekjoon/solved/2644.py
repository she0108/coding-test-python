from collections import deque

N = int(input())
A, B = map(int, input().split())
M = int(input())
alist = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    alist[x].append(y)
    alist[y].append(x)

queue = deque()
queue.append((A, 0))
visited = [0 for _ in range(N + 1)]
res = -1

while queue:
    num, chon = queue.popleft()
    for n in alist[num]:
        if n == B:
            res = chon + 1
            break

        if not visited[n]:
            visited[n] = 1
            queue.append((n, chon + 1))

print(res)
