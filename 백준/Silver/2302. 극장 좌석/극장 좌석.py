n = int(input())
m = int(input())
fix = [int(input()) for _ in range(m)]
dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
res = 1
if m >= 1: # 칸을 나눈다고 생각한다.
    s = 0
    for i in range(m):
        res *= dp[fix[i] - s - 1]
        s = fix[i]
    res *= dp[n - s]
    print(res)
else:
    print(dp[n])