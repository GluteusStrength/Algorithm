import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(n)] for _ in range(2)]
for i in range(2):
    if i == 0:
        dp[i][0] = nums[0]
        for j in range(1, len(nums)):
            dp[i][j] = max(nums[j], dp[i][j-1] + nums[j])
    else:
        dp[i][0] = nums[0]
        for j in range(1, len(nums)):
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1] + nums[j])
print(max(max(dp[0]), max(dp[1])))