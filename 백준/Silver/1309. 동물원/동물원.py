n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n+1)]
for i in range(3):
    dp[1][i] = 1
for i in range(2, n+1):
    for j in range(3):
        if j == 0:
            dp[i][j] = ((dp[i-1][1]) % 9901 + (dp[i-1][2]) % 9901) % 9901
        elif j == 1:
            dp[i][j] = ((dp[i-1][0]) % 9901 + (dp[i-1][2]) % 9901) % 9901
        else:
            dp[i][j] = (dp[i-1][0] % 9901 + (dp[i-1][1]) % 9901 + (dp[i-1][2]) % 9901) % 9901
print(sum(dp[n]) % 9901)