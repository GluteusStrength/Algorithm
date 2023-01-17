import sys
n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(21)] for _ in range(n)]
dp[0][nums[0]] = 1
for i in range(1, n-1):
    num = nums[i]
    check = dp[i-1]
    for j in range(21):
        if check[j] != 0:
            if j - num >= 0:
                dp[i][j - num] += dp[i-1][j]
            if j + num < 21:
                dp[i][j + num] += dp[i-1][j]
print(dp[n-2][nums[-1]])
