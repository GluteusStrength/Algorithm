import sys
n, k = map(int, sys.stdin.readline().split())
sub = [[0,0]]+[list(map(int, sys.stdin.readline().split())) for _ in range(k)]
dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
for i in range(1, k+1):
    for j in range(1, n+1):
        if j - sub[i][1] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-sub[i][1]] + sub[i][0])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[k][n])

