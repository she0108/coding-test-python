N = int(input())

song = [
    "baby",
    "sukhwan",
    "tururu",
    "turu",
    "very",
    "cute",
    "tururu",
    "turu",
    "in",
    "bed",
    "tururu",
    "turu",
    "baby",
    "sukhwan",
]

length = len(song)
loop = N // length
left = N % length

if left == 0:
    word = song[length - 1]
else:
    word = song[left - 1]

if word == "tururu":
    if loop >= 3:
        print("tu+ru*", loop + 2, sep="")
    else:
        print("tururu", "ru" * loop, sep="")
elif word == "turu":
    if loop >= 4:
        print("tu+ru*", loop + 1, sep="")
    else:
        print("turu", "ru" * loop, sep="")
else:
    print(word)
