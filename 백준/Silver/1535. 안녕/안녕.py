import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(100)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(100):
        if j - l[i-1] < 0:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-l[i-1]] + h[i-1])
print(dp[n][-1])