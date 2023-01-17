import sys
n = int(sys.stdin.readline())
card = [0]+list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n+1)]
dp[1] = card[1]
for i in range(2, n+1):
    for j in range(i, -1, -1):
        x = j
        y = i-j
        dp[i] = max(dp[i], card[x]+dp[y])
print(max(dp))