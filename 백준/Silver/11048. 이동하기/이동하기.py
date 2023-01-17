import sys
n, m = map(int, sys.stdin.readline().split())
candy = [[0 for _ in range(m+1)]]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    candy.append([0]+list(map(int, sys.stdin.readline().split())))
for i in range(1, n+1):
    for j in range(1, m+1):
        if j == 1:
            dp[i][j] += candy[i][j] + dp[i-1][j]
        else:
            if i == 1:
                dp[i][j] += candy[i][j] + dp[i][j-1]
            else:
                case_1 = candy[i][j] + dp[i-1][j-1]
                case_2 = candy[i][j] + dp[i-1][j]
                case_3 = candy[i][j] + dp[i][j-1]
                dp[i][j] = max(case_1, case_2, case_3)
print(dp[n][m])