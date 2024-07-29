from collections import deque

total, current, target, up, down = map(int, input().split())

# visited = [0] * (total + 1)
# cnt = -1

# queue = deque()
# queue.append([current, 0])
# visited[current] = 1

# while queue:
#     prev, c = queue.popleft()

#     if prev == target:
#         cnt = c
#         break

#     if prev + up <= total and visited[prev + up] == 0:
#         queue.append([prev + up, c + 1])
#         visited[prev + up] = 1

#     if prev - down >= 1 and visited[prev - down] == 0:
#         queue.append([prev - down, c + 1])
#         visited[prev - down] = 1

# if cnt == -1:
#     print("use the stairs")
# else:
#     print(cnt)


cnt = [-1] * (total + 1)

queue = deque()
queue.append(current)
cnt[current] = 0

while queue:
    prev = queue.popleft()

    if prev == target:
        break

    if prev + up <= total and cnt[prev + up] == -1:
        queue.append(prev + up)
        cnt[prev + up] = cnt[prev] + 1

    if prev - down >= 1 and cnt[prev - down] == -1:
        queue.append(prev - down)
        cnt[prev - down] = cnt[prev] + 1

if cnt[target] == -1:
    print("use the stairs")
else:
    print(cnt[target])
