# 14003 문제, 2565문제 알면 쉽게 해결 가능
import sys
from bisect import bisect_left
from collections import defaultdict
n = int(sys.stdin.readline())
l = [[0,0]]+[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
l.sort()
line = [0]
d = defaultdict(int)
for i in range(1, n+1):
    line.append(l[i][1])
    d[l[i][1]] = l[i][0]
dp = [0]
rec = [0 for _ in range(n+1)] # index 저장용
length = 0
for i in range(1, n+1):
    if dp[-1] < line[i]:
        dp.append(line[i])
        length = len(dp) - 1
        rec[i] = length
    else:
        rec[i] = bisect_left(dp, line[i])
        dp[rec[i]] = line[i]
print(n - length)
for i in range(n, 0, -1):
    if length == -1:
        break
    else:
        if length == rec[i]:
            d.pop(line[i])
            length -= 1
ans = list(d.values())
ans.sort()
for i in ans:
    print(i)


