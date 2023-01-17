import sys
while True:
    n, m = map(float, sys.stdin.readline().split())
    n = int(n)
    m = int(m*100+0.5)
    if n == 0:
        break
    else:
        candy = [[0,0]]+[list(map(float, sys.stdin.readline().split())) for _ in range(n)]
        dp = [0 for _ in range(m+1)]
        for i in range(1, n+1):
            c = int(candy[i][0])
            p = int(candy[i][1]*100+0.5)
            for j in range(1, m+1):
                if j - p >= 0:
                    dp[j] = max(dp[j], dp[j-p] + c)
        print(dp[m])





