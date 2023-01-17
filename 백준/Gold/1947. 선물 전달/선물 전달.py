n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(2, n+1):
    if i == 2:
        dp[i] = 1
    else:
        dp[i] = (i-1)*(dp[i-1]+dp[i-2]) % 1000000000
print(dp[n] % 1000000000)