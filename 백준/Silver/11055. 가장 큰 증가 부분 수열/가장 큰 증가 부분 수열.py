import sys
N = input()
n = int(N)
l = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
dp[0] = l[0]
if n == 1:
    print(l[0])
else:
    for k in range(1, n):
        for j in range(k):
            if l[k] > l[j]:
                dp[k] = max(dp[k], l[k]+dp[j])
            else:
                dp[k] = max(dp[k], l[k])
    print(max(dp))