import sys
n = int(input())
p = list(map(int, sys.stdin.readline().split()))
dp = [0] + p
for i in range(2, n+1):
    for j in range(i, -1, -1):
        x = j
        y = i - j
        dp[i] = min(dp[i], dp[x] + dp[y])
print(dp[n])