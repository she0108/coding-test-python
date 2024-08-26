board = [list(map(int, input().split())) for _ in range(5)]
nums = []
for _ in range(5):
    nums.extend(list(map(int, input().split())))


def check_num(board, num):
    found = False
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0
                found = True
                break
        if found:
            break


def count_line(board):
    cnt = 0

    for i in range(5):
        if not (
            board[i][0] or board[i][1] or board[i][2] or board[i][3] or board[i][4]
        ):
            cnt += 1
        if not (
            board[0][i] or board[1][i] or board[2][i] or board[3][i] or board[4][i]
        ):
            cnt += 1

    if not (board[0][0] or board[1][1] or board[2][2] or board[3][3] or board[4][4]):
        cnt += 1

    if not (board[0][4] or board[1][3] or board[2][2] or board[3][1] or board[4][0]):
        cnt += 1

    return cnt


for i in range(25):
    check_num(board, nums[i])
    line = count_line(board)
    if line >= 3:
        print(i + 1)
        break
