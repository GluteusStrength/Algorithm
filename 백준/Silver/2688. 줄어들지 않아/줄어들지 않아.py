t = int(input())
for i in range(t):
    n = int(input())
    dp = [[0 for _ in range(10)] for _ in range(n+1)]
    for j in range(1, n+1):
        for k in range(10):
            if j == 1:
                if k == 0:
                    dp[j][k] = 1
                else:
                    dp[j][k] = dp[j][k-1] + 1
            else:
                if k == 0:
                    dp[j][k] = dp[j-1][9]
                else:
                    dp[j][k] = dp[j][k-1] + (dp[j-1][9] - dp[j-1][k-1])
    print(dp[n][-1])