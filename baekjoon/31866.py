J, I = map(int, input().split())

a = [0, 2, 5]
b = [(0, 2), (2, 5), (5, 0)]

if J == I or (J not in a and I not in a):
    print("=")
elif I not in a or (J, I) in b:
    print(">")
else:
    print("<")
