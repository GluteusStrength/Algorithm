import sys
n, t = map(int, sys.stdin.readline().split())
chapter = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chapter.sort(key = lambda x : x[0])
dp = [[0 for _ in range(t+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, t+1):
        if j - chapter[i-1][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-chapter[i-1][0]] + chapter[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][t])