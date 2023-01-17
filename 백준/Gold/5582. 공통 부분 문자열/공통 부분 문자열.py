s_1 = input()
s_2 = input()
s_1 = [""] + list(s_1)
s_2 = [""] + list(s_2)
dp = [[0 for _ in range(len(s_1))] for _ in range(len(s_2))]
result = 0
for i in range(1, len(s_2)):
    for j in range(1, len(s_1)):
        if s_2[i] == s_1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
    result = max(max(dp[i]), result)
print(result)
