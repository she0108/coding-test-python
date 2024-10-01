import sys

sys.setrecursionlimit(10**6)

N = int(input())
M = int(input())

graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = graph[b][a] = c


visited = [0] * (N + 1)
total_cost = 0

visited[1] = 1

while len(visited) < N:
    min_node = -1
    min_cost = 10000
    for n in visited:
        for i in range(1, N + 1):
            if 0 < graph[n][i] < min_cost and not visited[i]:
                min_node = i
                min_cost = graph[n][i]
    visited[min_node] = 1
    total_cost += min_cost

print(total_cost)
