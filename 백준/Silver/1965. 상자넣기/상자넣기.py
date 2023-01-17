import sys
n = int(input())
box = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))