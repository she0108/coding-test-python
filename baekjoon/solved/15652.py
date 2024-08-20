N, M = map(int, input().split())


def dfs(seq, start):

    if len(seq) == M:
        print(*seq)
        return

    for i in range(start, N + 1):
        dfs(seq + [i], i)


dfs([], 1)
