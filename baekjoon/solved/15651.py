N, M = map(int, input().split())


def dfs(seq):

    if len(seq) == M:
        print(*seq)
        return

    for i in range(1, N + 1):
        dfs(seq + [i])


dfs([])
