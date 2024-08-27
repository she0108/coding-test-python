H, W = map(int, input().split())
sky = [list(input()) for _ in range(H)]


for h in range(H):
    row = []
    last_c = -1

    for w in range(W):

        if sky[h][w] == "c":
            row.append(0)
            last_c = w

        elif last_c < w and last_c > -1:
            row.append(w - last_c)

        else:
            row.append(-1)

    print(*row)
