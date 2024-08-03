COLOR_TO_VALUE = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

first = input().rstrip()
second = input().rstrip()
third = input().rstrip()

res = (COLOR_TO_VALUE[first] * 10 + COLOR_TO_VALUE[second]) * (
    10 ** COLOR_TO_VALUE[third]
)

print(res)
