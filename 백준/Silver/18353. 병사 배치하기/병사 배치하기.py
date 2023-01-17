import sys
n = int(sys.stdin.readline())
army = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if army[j] > army[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))