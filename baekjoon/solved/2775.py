import sys

input = sys.stdin.readline


apt = [[0 for _ in range(15)] for _ in range(15)]

for i in range(15):
    for j in range(15):
        if i == 0:
            apt[i][j] = j + 1
        elif j == 0:
            apt[i][j] = apt[i - 1][j]
        else:
            apt[i][j] = apt[i - 1][j] + apt[i][j - 1]

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(apt[k][n - 1])


# k의 최댓값이 정해지지 않은 경우 (재귀)

# apt = [[i for i in range(1, 15)]]


# def get_num(k, n):
#     if len(apt) > k:
#         if len(apt[k]) >= n:
#             return apt[k][n - 1]
#         else:
#             num = get_num(k, n - 1) + get_num(k - 1, n)
#             apt[k].append(num)
#             return apt[k][n - 1]
#     else:
#         if n == 1:
#             apt.append([get_num(k - 1, n)])
#             return apt[k][n - 1]
#         else:
#             num = get_num(k, n - 1) + get_num(k - 1, n)
#             apt[k].append(num)
#             return apt[k][n - 1]


# T = int(input())

# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     print(get_num(k, n))
