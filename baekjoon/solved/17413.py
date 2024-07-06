S = input()

word = []
tag_opened = False
res = []

for c in S:
    if c == " ":
        if len(word) > 0:
            word.reverse()
            res.extend(word)
            word = []
        res.append(c)
    elif c == "<":
        if len(word) > 0:
            word.reverse()
            res.extend(word)
            word = []
        res.append(c)
        tag_opened = True
    elif c == ">":
        res.append(c)
        tag_opened = False
    else:
        if tag_opened:
            res.append(c)
        else:
            word.append(c)

if len(word) > 0:
    word.reverse()
    res.extend(word)

print("".join(res))

# print 여러번 하는 것보다 list에 저장한 뒤 join해서 한번에 print하는 게 더 빠름
