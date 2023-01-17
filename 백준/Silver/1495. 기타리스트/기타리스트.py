import sys
n, s, m = map(int, sys.stdin.readline().split())
v = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
flag = 0
result = -1
for i in range(1, n+1):
    volume = v[i]
    if i == 1:
        if s + volume <= m:
            dp[i][s+volume] = 1
        if s - volume >= 0:
            dp[i][s-volume] = 1
    else:
        for j in range(m+1):
            if dp[i-1][j] == 1:
                if j + volume <= m:
                    dp[i][j+volume] = 1
                if j - volume >= 0:
                    dp[i][j-volume] = 1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break
print(result)
