dp = [1 for _ in range(251)]
for i in range(2, 251):
    dp[i] = 2 * dp[i-2] + dp[i-1]
while True:
    try:
        print(dp[int(input())])
    except:
        break
