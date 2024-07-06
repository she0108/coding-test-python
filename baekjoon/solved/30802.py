N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

shirts = 0
for s in size:
    if s % T > 0:
        shirts += s // T + 1
    else:
        shirts += s // T

pens = (N // P, N % P)

print(shirts)
print(pens[0], pens[1])
