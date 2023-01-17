import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x <= k:
        coin.append(x)
coin = list(set(coin))
coin.sort()
dp = [0 for _ in range(k+1)]
for i in coin:
    if i == coin[0]:
        div = k // i
        for j in range(1, div+1):
            dp[i*j] = 1
    else:
        for k in range(i, k+1):
            if i == k:
                dp[k] += 1
            else:
                dp[k] += dp[k-i]
print(dp[k])

