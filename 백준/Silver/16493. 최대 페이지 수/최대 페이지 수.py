import sys
n, m = map(int, sys.stdin.readline().split())
chapt = [[0,0]]
for i in range(m):
    chapt.append(list(map(int, sys.stdin.readline().split())))
dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
for i in range(1, m+1):
    day = chapt[i][0]
    page = chapt[i][1]
    for j in range(1, n+1):
        if j - day < 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-day] + page)
print(dp[-1][-1])



