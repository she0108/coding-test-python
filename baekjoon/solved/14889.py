import sys

input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

team = [0 for _ in range(N)]
diff = []


def make_team(cnt, start):

    if cnt == N // 2:
        d = calc_spec()
        diff.append(d)
        return

    for i in range(start, N):
        team[i] = 1
        make_team(cnt + 1, i + 1)
        team[i] = 0


def calc_spec():
    start = 0
    link = 0
    for i in range(N):
        for j in range(i + 1, N):
            if team[i] and team[j]:
                start += S[i][j] + S[j][i]
            elif not team[i] and not team[j]:
                link += S[i][j] + S[j][i]
    return abs(start - link)


make_team(0, 0)

print(min(diff))
