import sys
n = int(sys.stdin.readline())
passenger = [0] + list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())
psum = [0 for _ in range(n+1)]
for i in range(1, n+1):
    psum[i] = passenger[i] + psum[i-1]
dp = [[0 for _ in range(n+1)] for _ in range(4)]
for i in range(1, 4):
    for j in range(i*k, n+1):
        if i == 1:
            dp[i][j] = max(dp[i][j-1], psum[j] - psum[j-k])
        else:
            dp[i][j] = max(dp[i][j-1], psum[j] - psum[j-k] + dp[i-1][j-k])
print(dp[3][n])


