name = input()

alphabets = [0 for _ in range(26)]

for letter in name:
    alphabets[ord(letter) - 65] += 1

left = []
mid = ""
sorry = False

for i in range(26):
    if mid != "" and alphabets[i] % 2 == 1:
        sorry = True
        break
    left.extend([chr(i + 65) for _ in range(alphabets[i] // 2)])
    if alphabets[i] % 2 == 1:
        mid = chr(i + 65)

if sorry:
    print("I'm Sorry Hansoo")
else:
    print("".join(left), mid, "".join(reversed(left)), sep="")
