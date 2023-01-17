import sys
n = int(sys.stdin.readline())
group = [0]+list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n+1)]
for i in range(2, n+1):
    if i == 2:
        dp[i] = abs(group[i-1] - group[i])
    else:
        for j in range(i-1, 0, -1):
            dp[i] = max(dp[i], (max(group[j:i+1]) - min(group[j:i+1])) + dp[j-1])
print(dp[-1])