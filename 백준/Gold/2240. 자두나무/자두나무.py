import sys
t, w = map(int, sys.stdin.readline().split())
time = [0]
for i in range(t):
    time.append(int(sys.stdin.readline()))
dp = [[0 for _ in range(w+1)] for _ in range(t+1)]
for i in range(1, t+1):
    tree = time[i]
    for j in range(w+1):
        if j == 0:
            if tree == 1:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i-1][j]
        else:
            if j % 2 == 1 and tree == 2:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            elif j % 2 == 0 and tree == 1:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[-1]))