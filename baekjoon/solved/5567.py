n = int(input())
m = int(input())
friends = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [0 for _ in range(n + 1)]

visited[1] = 1


def dfs(num, depth):

    if depth == 2:
        return 0

    count = 0

    for friend in friends[num]:
        if not visited[friend]:
            visited[friend] = 1
            count += dfs(friend, depth + 1)

    return count


print(dfs(1, 0))
