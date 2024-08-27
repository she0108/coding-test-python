import sys
from collections import deque


input = sys.stdin.readline

P = int(input())

for _ in range(P):
    I = list(map(int, input().split()))
    T = I[0]
    students = I[1:]

    line = deque([students[0]])
    cnt = 0

    for i in range(1, 20):
        student = students[i]
        line.append(student)

        while i > 0 and student < line[i - 1]:
            line[i] = line[i - 1]
            cnt += 1
            i -= 1
        line[i] = student

    print(T, cnt)
