import sys
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(i, n+1):
                if i == 0:
                    dp[i][j] = 1
                    if j == n+1:
                        dp[i][j] = 1
                        dp[i][0] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp[n][n])