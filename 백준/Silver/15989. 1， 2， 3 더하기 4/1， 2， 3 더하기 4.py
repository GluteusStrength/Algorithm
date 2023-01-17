import sys
n = int(sys.stdin.readline())
num = []
base = [1,2,3]
for i in range(n):
    x = int(sys.stdin.readline())
    num.append(x)
for i in num:
    if i >= 4:
        dp = [0 for _ in range(i+1)]
        for j in base:
            if j == 1:
                for k in range(j, i+1):
                    dp[k] = 1
            else:
                if j == 2:
                    dp[j] += 1
                    for k in range(j, i+1):
                        dp[k] += dp[k-j]
                if j == 3:
                    dp[j] += 1
                    for k in range(j, i+1):
                        dp[k] += dp[k-j]
        print(dp[i])
    else:
        if i == 1:
            print(1)
        elif i == 2:
            print(2)
        else:
            print(3)