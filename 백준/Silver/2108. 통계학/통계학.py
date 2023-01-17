import sys
from collections import Counter
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()
d = Counter(nums)
center = nums[n//2]
avg = 0
com = 0
ran = nums[-1] - nums[0]
if n >= 2:
    comm = d.most_common(2)
    if comm[1][1] == comm[0][1]:
        com = comm[1][0]
    else:
        com = comm[0][0]
else:
    com = nums[0]
for i in nums:
    avg += i
avg /= n
avg = int(round(avg, 0))
ans = [avg, center, com, ran]
for i in ans:
    print(i)

