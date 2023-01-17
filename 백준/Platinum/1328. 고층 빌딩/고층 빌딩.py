import sys
n, l, r = map(int, sys.stdin.readline().split())
mod = 1000000007
dp = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)] # 빌딩수, 왼쪽에서 보이는 빌딩 수, 오른쪽에서 보이는 빌딩 수
dp[1][1][1] = 1
for i in range(2, n+1):
    for j in range(1, l+1):
        for k in range(1, r+1):
            dp[i][j][k] = (dp[i-1][j-1][k] + dp[i-1][j][k-1] + dp[i-1][j][k]*(i-2))%mod
print(dp[n][l][r])
