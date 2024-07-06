import sys

input = sys.stdin.readline


# T = int(input())
# for _ in range(T):
#     N = int(input())
#     grades = [list(map(int, input().split())) for _ in range(N)]

#     for i in range(N):
#         grades[i].append(grades[i][0] + grades[i][1])

#     grades.sort(key=lambda grade: grade[2])
#     result = []

#     while len(grades) > 0:
#         bound = grades[0]
#         i = 1
#         while i < len(grades):
#             if grades[i][0] > bound[0] and grades[i][1] > bound[1]:
#                 grades.pop(i)
#             else:
#                 i += 1

#         result.append(grades.pop(0))

#     print(len(result))


T = int(input())
for _ in range(T):
    N = int(input())
    grades = [list(map(int, input().split())) for _ in range(N)]

    grades.sort(key=lambda grade: grade[0])

    result = [grades[0]]

    for i in range(1, N):
        passs = True
        for grade in result:
            if grades[i][1] > grade[1]:
                passs = False
                break
        if passs:
            result.append(grades[i])

    print(len(result))
