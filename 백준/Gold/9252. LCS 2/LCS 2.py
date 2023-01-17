s_1 = input()
s_2 = input()
s_1 = [""]+list(s_1)
s_2 = [""]+list(s_2)
dp = [[0]*len(s_1) for _ in range(len(s_2))]
word = [[""]*len(s_1) for _ in range(len(s_2))]
length = 0
for i in range(1, len(s_2)):
    for j in range(1, len(s_1)):
        if s_2[i] == s_1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            word[i][j] = word[i-1][j-1] + s_2[i]
            length = max(length, dp[i][j])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            length = max(length, dp[i][j])
            if dp[i-1][j] > dp[i][j-1]:
                word[i][j] += word[i-1][j]
            else:
                word[i][j] = word[i][j-1]
cnt = 0
for i in word:
    for j in i:
        if len(j) == length:
            cnt += 1
            print(length)
            print(j)
            break
    if cnt > 0:
        break


