import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
r = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
# 버리는 걸로 생각? 역dp
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if l[i] > r[j]:
            dp[i][j] = max(dp[i][j+1] + r[j], dp[i+1][j], dp[i+1][j+1])
        else:
            dp[i][j] = max(dp[i+1][j+1], dp[i+1][j])
print(dp[0][0])