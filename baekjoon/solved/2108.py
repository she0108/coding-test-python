import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

print(round(sum(nums) / N))

nums.sort()
print(nums[N // 2])

# dic = {}
# m = 0
# c = []
# for n in nums:
#     if n in dic.keys():
#         dic[n] += 1
#     else:
#         dic[n] = 1

#     if dic[n] > m:
#         m = dic[n]
#         c = [n]
#     elif dic[n] == m:
#         c.append(n)
# if len(c) > 1:
#     c.sort()
#     print(c[1])
# else:
#     print(c[0])

most = Counter(nums).most_common()
if len(most) > 1 and most[0][1] == most[1][1]:
    print(most[1][0])
else:
    print(most[0][0])


print(nums[-1] - nums[0])
