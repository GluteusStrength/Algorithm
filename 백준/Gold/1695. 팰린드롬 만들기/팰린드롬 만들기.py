import sys
n = int(input())
nums = ["0"] + list(map(str, sys.stdin.readline().split()))
rev = list(reversed(nums))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    flag = rev[i]
    for j in range(1, n+1):
        if nums[j] == flag:
            dp[i+1][j] = dp[i][j-1] + 1
        else:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j-1])
print(n - dp[n][n])