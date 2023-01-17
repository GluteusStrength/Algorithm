s_1 = input()
s_2 = input()
s_3 = input()
s_1 = [""]+list(s_1)
s_2 = [""]+list(s_2)
s_3 = [""]+list(s_3)
dp = [[[0]*len(s_1) for _ in range(len(s_2))] for _ in range(len(s_3))]
length = 0
for i in range(1, len(s_3)):
    for j in range(1, len(s_2)):
        for k in range(1, len(s_1)):
            if s_1[k] == s_2[j] == s_3[i]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                length = max(dp[i][j][k], length)
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
                length = max(dp[i][j][k], length)
print(length)

