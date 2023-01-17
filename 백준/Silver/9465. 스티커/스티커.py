import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    sticker = []
    for j in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    for x in range(1, n):
        for y in range(2):
            if x == 1:
                if y == 0:
                    dp[y][x] = sticker[y][x] + sticker[y+1][x-1]
                else:
                    dp[y][x] = sticker[y][x] + sticker[y-1][x-1]
            else:
                if y == 0:
                    dp[y][x] = max(sticker[y][x] + dp[y+1][x-1], sticker[y][x] + dp[y+1][x-2])
                else:
                    dp[y][x] = max(sticker[y][x] + dp[y-1][x-1], sticker[y][x] + dp[y-1][x-2])
    print(max(dp[0][n-1], dp[1][n-1]))

