from collections import deque

TRUCK_NUMBER, BRIDGE_LENGTH, MAX_WEIGHT = map(int, input().split())
TRUCK_WEIGHT = list(map(int, input().split()))


bridge = deque(0 for _ in range(BRIDGE_LENGTH))

next_index = 0
t = 0

while True:

    t += 1
    bridge.pop()
    bridge.appendleft(0)

    if next_index == TRUCK_NUMBER and bridge.count(0) == BRIDGE_LENGTH:
        break

    if next_index < TRUCK_NUMBER:
        cur_weight = sum(bridge)
        if cur_weight + TRUCK_WEIGHT[next_index] <= MAX_WEIGHT:
            bridge[0] = TRUCK_WEIGHT[next_index]
            next_index += 1

print(t)
