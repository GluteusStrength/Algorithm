import sys
n = int(input())
l = list(map(int, sys.stdin.readline().split()))
dp = []
dp.append(l[0])
for i in range(n-1):
    dp.append(max(dp[i]+l[i+1],l[i+1]))
print(max(dp))