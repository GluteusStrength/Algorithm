import sys
import math
n = int(input())
building = list(map(int, sys.stdin.readline().split()))
build_l = []
dp = [0 for _ in range(n)]
for i in range(n):
    build_l.append([i, building[i]])
tangent = math.inf
for i in range(n):
    flag = build_l[i]
    for j in range(i-1, -1, -1):
        if j == i-1:
            dp[i] += 1
            tangent = (build_l[j][1] - flag[1]) / (build_l[j][0] - flag[0])
        else:
            tan = (build_l[j][1] - flag[1]) / (build_l[j][0] - flag[0])
            if tan < tangent:
                dp[i] += 1
                tangent = tan
    for k in range(i+1, n):
        if k == i+1:
            dp[i] += 1
            tangent = (build_l[k][1] - flag[1]) / (build_l[k][0] - flag[0])
        else:
            tan = (build_l[k][1] - flag[1]) / (build_l[k][0] - flag[0])
            if tan > tangent:
                dp[i] += 1
                tangent = tan
            else:
                tangent = max(tan, tangent)
print(max(dp))

