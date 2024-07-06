num1, num2 = map(int, input().split())

x = max(num1, num2)
y = min(num1, num2)

r = x % y
while r != 0:
    x = y
    y = r
    r = x % y

print(y)
print(int(num1 * num2 / y))
