import sys
n = int(sys.stdin.readline())
d = []
p = []
for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    d.append(x[0])
    p.append(x[1])
dp = [0 for _ in range(n+1)]
for i in range(n):
    if d[i] + i <= n:
        dp[i+d[i]] = max(dp[i+d[i]], dp[i]+p[i])
    dp[i+1] = max(dp[i+1], dp[i])
print(dp[n])