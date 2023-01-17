n = int(input())
coin = [2, 5]
dp = [100001 for _ in range(n+1)]
dp[0] = 0
for i in coin:
    c = i
    for j in range(c, n+1):
        dp[j] = min(dp[j], dp[j-c] + 1)
if dp[n] == 100001:
    print(-1)
else:
    print(dp[n])
