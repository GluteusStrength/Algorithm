n = int(input())
dp = [0 for _ in range(n+1)]
dp[0] = 1
for i in range(2, n+1, 2):
    dp[i] = dp[i-2] * 3 # dp[2] = 3이고 새로운 모양이 더 안 나오는 기본
    for j in range(0, i-2, 2):
        dp[i] += dp[j] * 2
print(dp[n])
