N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

results = []


def dfs(res, cnt):
    if cnt == N:
        results.append(res)
        return

    if ops[0] > 0:
        ops[0] -= 1
        dfs(res + nums[cnt], cnt + 1)
        ops[0] += 1

    if ops[1] > 0:
        ops[1] -= 1
        dfs(res - nums[cnt], cnt + 1)
        ops[1] += 1

    if ops[2] > 0:
        ops[2] -= 1
        dfs(res * nums[cnt], cnt + 1)
        ops[2] += 1

    if ops[3] > 0:
        ops[3] -= 1
        div_res = res // nums[cnt]
        if res < 0 and res % nums[cnt] != 0:
            div_res += 1
        dfs(div_res, cnt + 1)
        ops[3] += 1


dfs(nums[0], 1)

max_res = -(10**10)
min_res = 10**10

for res in results:
    if res > max_res:
        max_res = res
    if res < min_res:
        min_res = res

print(max_res)
print(min_res)
