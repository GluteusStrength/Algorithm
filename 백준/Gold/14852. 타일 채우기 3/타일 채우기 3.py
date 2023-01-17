n = int(input())
mod = 1000000007
dp = [1, 2, 7] + [0 for _ in range(n-1)]
rec = 0
for i in range(3, n+1):
    rec += dp[i-3] # 예외 상황 역시 누적된다. 따라서 이를 누적시킨다.
    dp[i] = (2*dp[i-1] + 3*dp[i-2] + 2*rec) % mod
print(dp[n] % mod)