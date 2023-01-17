import sys
t = int(sys.stdin.readline())
for i in range(t):
    cnt = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    dp = [0 for _ in range(m+1)]
    for j in coin:
        if j == coin[0]:
            div = m // j
            for k in range(1, div+1):
                dp[j*k] = 1
        else:
            for k in range(j, m+1):
                if k == j:
                    dp[k] += 1
                else:
                    dp[k] += dp[k-j]
    print(dp[m])
