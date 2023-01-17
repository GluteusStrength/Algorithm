n = "0"+input()
dp = [0 for _ in range(len(n))]
dp[0] = 1
dp[1] = 1
for i in range(2, len(n)):
    if n[i] != "0":
        flag = int(n[i-1]+n[i])
        if n[i-1] != "0":
            if 1 <= flag and flag <= 34:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-2]
print(dp[len(n)-1])
