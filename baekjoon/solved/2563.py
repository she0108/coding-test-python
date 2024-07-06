N = int(input())

pla = [0 for x in range(10)]

while N != 0:
    pla[N % 10] += 1
    N = N // 10

most = pla.index(max(pla))
if most == 6 and pla[6] > pla[9] + 1:
    diff = pla[6] - pla[9]
    pla[6] -= diff // 2
    pla[9] += diff // 2
elif most == 9 and pla[9] > pla[6] + 1:
    diff = pla[9] - pla[6]
    pla[9] -= diff // 2
    pla[6] += diff // 2

print(max(pla))
