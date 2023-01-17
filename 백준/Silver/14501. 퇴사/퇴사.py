import sys
n = int(sys.stdin.readline())
c = []
dp = []
for i in range(n):
    c.append(list(map(int, sys.stdin.readline().split())))
    dp.append(c[i][1])
dp.append(0)
for i in range(n-1, -1, -1):
    d = c[i][0]
    if i + d <= n:
        dp[i] = max(dp[i+1], dp[i] + dp[i+d])
    else:
        dp[i] = dp[i+1]
print(dp[0])