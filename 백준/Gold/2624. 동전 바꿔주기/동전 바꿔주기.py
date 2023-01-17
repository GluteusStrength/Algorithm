import sys
t = int(sys.stdin.readline())
k = int(sys.stdin.readline())
coin = [[0,0]]
for i in range(k):
    coin.append(list(map(int, sys.stdin.readline().split())))
coin.sort()
dp = [[0 for _ in range(t+1)] for _ in range(k+1)]
dp[0][0] = 1
for i in range(1, k+1):
    value = coin[i][0]
    num = coin[i][1]
    if i == 1:
        for a in range(num+1):
            if value*a <= t:
                dp[i][value*a] += 1
            else:
                break
    else:
        for j in range(t+1):
            dp[i][j] = dp[i-1][j] # 제일 기본으로 해야될 것. 그 전꺼를 가져오기
            for x in range(1, num+1):
                if value * x <= j:
                    dp[i][j] += dp[i-1][j - value*x]
                else:
                    break
print(dp[k][t])
