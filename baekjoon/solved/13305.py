import sys

input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = 1000000000
d = 0
cost = 0

for i in range(N - 1):
    if price[i] < min_price:
        cost += min_price * d
        min_price = price[i]
        d = distance[i]
    else:
        d += distance[i]

cost += min_price * d

print(cost)


# 변수 d 생략 가능
