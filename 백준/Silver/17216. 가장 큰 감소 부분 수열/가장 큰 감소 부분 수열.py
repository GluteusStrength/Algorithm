import sys
N = input()
n = int(N)
l = list(map(int, sys.stdin.readline().split()))
dp = [1]*n
dp[0] = l[0]
for i in range(n):
    for j in range(i-1, -1, -1):
        if l[i] < l[j]:
            dp[i] = max(dp[i], dp[j] + l[i])
        else:
            dp[i] = max(dp[i], l[i])
print(max(dp))