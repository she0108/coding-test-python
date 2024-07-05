n = 1
while True:
    L, P, V = map(int, input().split())
    if (L, P, V) == (0, 0, 0):
        break
    res = (V // P) * L + min(V % P, L)
    print(f"Case {n}: {res}")
    n += 1
