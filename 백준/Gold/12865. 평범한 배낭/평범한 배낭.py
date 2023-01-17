import sys
n, k = map(int, sys.stdin.readline().split())
l = []
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))
w = [0]
v = [0]
for i in range(n):
    w.append(l[i][0])
    v.append(l[i][1])
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for x in range(1, n+1):
    for y in range(1, k+1):
        if w[x] <= y:
            dp[x][y] = max(v[x] + dp[x-1][y-w[x]], dp[x-1][y])
        if w[x] > y:
            dp[x][y] = dp[x-1][y]
print(dp[n][k])
