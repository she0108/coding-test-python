N, M = map(int, input().split())

res = []
seq = []


def dfs():

    if len(seq) == M:
        res.append(" ".join(list(map(str, seq))))
        return

    for i in range(1, N + 1):
        if i not in seq:
            seq.append(i)
            dfs()
            seq.pop()


dfs()

for r in res:
    print(r)


# 좀 더 깔끔하고 직관적으로
