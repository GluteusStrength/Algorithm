n = int(input())
dp = [n+1] * (n+1)
dp[0] = 0
c = [7, 5, 2, 1]
for i in range(1, n+1):
    for j in c:
        if j <= i and dp[i-j]+1 < dp[i]:
            dp[i] = dp[i-j]+1
print(dp[n])
