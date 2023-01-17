import sys
x = " "+sys.stdin.readline().rstrip()
y = " "+sys.stdin.readline().rstrip()
dp = [[0 for _ in range(len(x))] for _ in range(len(y))]
word = [["" for _ in range(len(x))] for _ in range(len(y))]
for i in range(1, len(y)):
    for j in range(1, len(x)):
        if x[j] == y[i]:
            dp[i][j] = dp[i-1][j-1] + 1
            word[i][j] = word[i-1][j-1] + y[i]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if dp[i-1][j] >= dp[i][j-1]:
                word[i][j] = word[i-1][j]
            else:
                word[i][j] = word[i][j-1]
print(word[len(y)-1][len(x)-1])