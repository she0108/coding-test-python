before = input()
after = []

for c in before:
    if c == " ":
        after.append(" ")
    else:
        o = ord(c)
        if 65 <= o and o <= 90:
            no = o + 13
            if no > 90:
                no -= 26
            after.append(chr(no))
        elif 97 <= o and o <= 122:
            no = o + 13
            if no > 122:
                no -= 26
            after.append(chr(no))
        else:
            after.append(c)

print("".join(after))
