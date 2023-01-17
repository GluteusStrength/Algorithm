import sys
n = int(input())
l = list(map(int, sys.stdin.readline().split()))
m = int(input())
dp = [[0]*n for i in range(n)]
for x in range(n):
    dp[x][x] = 1
for a in range(n-1):
    if l[a] == l[a+1]:
        dp[a][a+1] = 1
for b in range(2,n):
    for c in range(n - b):
        f = c+b
        if l[c] == l[f] and dp[c+1][f-1] == 1:
            dp[c][f] = 1
for j in range(m):
    x,y = map(int,sys.stdin.readline().split())
    print(dp[x-1][y-1])