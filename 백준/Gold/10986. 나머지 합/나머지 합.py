import sys, math
from collections import Counter
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
psum = [0 for _ in range(m+1)]
psum[0] = 1
s = 0
for i in range(1, n+1):
    s += nums[i-1]
    s %= m
    psum[s] += 1
a = Counter(psum)
ans = 0
for i in a:
    if i >= 2:
        ans += a[i]*(sum(range(1, i)))
print(ans)

