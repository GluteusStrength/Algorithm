import sys
from bisect import bisect_left
n = int(input())
line = [0]+list(map(int, sys.stdin.readline().split()))
dp = [0]
length = 0
rec = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if dp[-1] < line[i]:
        dp.append(line[i])
        rec[i] = len(dp) - 1
        length = rec[i]
    else:
        rec[i] = bisect_left(dp, line[i])
        dp[rec[i]] = line[i]
print(length)


