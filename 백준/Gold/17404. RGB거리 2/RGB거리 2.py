import sys
import math
n = int(input())
c = []
result = math.inf
for i in range(n):
    c.append(list(map(int, sys.stdin.readline().split())))
for i in range(3):
    dp = [[0 for _ in range(3)] for _ in range(n)]
    for j in range(3):
        if i == j:
            dp[0][j] = c[0][j]
        else:
            dp[0][j] = math.inf # 색을 정하고 갈 때 다른 색의 영향을 미치지 않게 하기 위해서
    for k in range(1, n):
        dp[k][0] = c[k][0] + min(dp[k-1][1], dp[k-1][2])
        dp[k][1] = c[k][1] + min(dp[k-1][0], dp[k-1][2])
        dp[k][2] = c[k][2] + min(dp[k-1][1], dp[k-1][0])
    for x in range(3):
        if x != i:
            result = min(result, dp[-1][x])
print(result)




