import sys
n = int(input())
stu = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n+1)]
for i in range(n):
    ind = stu[i]
    dp[ind] = dp[ind-1] + 1
print(n - max(dp))