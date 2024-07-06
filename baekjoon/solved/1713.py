import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
votes = list(map(int, input().split()))

pics = []

for vote in votes:
    exist = False
    for i in range(len(pics)):
        if pics[i][0] == vote:
            pics[i][1] += 1
            exist = True
            break
    if not exist:
        if len(pics) < N:
            pics.append([vote, 1])
        else:
            mv = pics[0][1]
            mi = 0
            for i in range(1, N):
                if pics[i][1] < mv:
                    mv = pics[i][1]
                    mi = i
            pics.pop(mi)
            pics.append([vote, 1])

students = [pic[0] for pic in pics]
students.sort()
print(" ".join(map(str, students)))


# students를 str로 변환한 뒤 sort하면 100 < 99 가 돼버림

# defaultdict 이용해 풀어보기
