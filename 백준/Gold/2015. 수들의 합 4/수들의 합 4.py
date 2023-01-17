import sys
from collections import defaultdict
n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
d = defaultdict(int)
s = 0
res = 0
for i in range(n):
    s += nums[i]
    if s-k in d:
        res += d[s-k]
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
if k in d:
    res += d[k]
print(res)

