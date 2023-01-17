import sys
n = int(sys.stdin.readline())
board = [[0]*(n+1)]+[[0]+list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
initial = board[1][1]
if initial+1 <= n:
    dp[1][initial+1] = 1
    dp[initial+1][1] = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j]:
            if board[i][j] + j <= n:
                dp[i][j+board[i][j]] += dp[i][j]
            if board[i][j] + i <= n:
                dp[i+board[i][j]][j] += dp[i][j]
        if i == n and j == n-1:
            print(dp[n][n])
            break