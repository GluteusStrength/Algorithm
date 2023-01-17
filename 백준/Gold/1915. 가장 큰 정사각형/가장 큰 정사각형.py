import sys
n, m = map(int, sys.stdin.readline().split())
rect = []
for _ in range(n):
    x = sys.stdin.readline().rstrip()
    x = list(x)
    p = []
    for i in x:
        p.append(int(i))
    rect.append(p)
dp = [[0 for _ in range(m)] for _ in range(n)]
length = 0
for i in range(n):
    for j in range(m):
        if i == 0:
            if rect[i][j] == 1:
                dp[i][j] = 1
        else:
            if j == 0:
                if rect[i][j] == 1:
                    dp[i][j] = 1
            else:
                if rect[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    length = max(length, max(dp[i]))
print(length*length)