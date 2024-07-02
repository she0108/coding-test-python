N = int(input())

msg0 = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
msg1 = '"재귀함수가 뭔가요?"'
msg2 = '''"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'''
msg3 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
msg4 = "라고 답변하였지."


def print_message(i):
    if i < N:
        print("____" * i, msg1, sep="")
        m = msg2.split("\n")
        for l in m:
            print("____" * i, l, sep="")
        print_message(i + 1)
        print("____" * i, msg4, sep="")
    else:
        print("____" * i, msg1, sep="")
        print("____" * i, msg3, sep="")
        print("____" * i, msg4, sep="")


print(msg0)
print_message(0)
