import sys
t = int(input())
dp = [[[0 for _ in range(2)] for _ in range(101)] for _ in range(101)]
dp[1][0][0] = 1
dp[1][0][1] = 1
for i in range(2, 101):
    for j in range(i):
        dp[i][j][0] = dp[i-1][j][1] + dp[i-1][j][0]
        dp[i][j][1] = dp[i-1][j-1][1] + dp[i-1][j][0]
for i in range(t):
    n, k = map(int, sys.stdin.readline().split())
    print(sum(dp[n][k]))