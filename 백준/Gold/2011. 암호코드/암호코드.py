n = input()
dp = [0 for _ in range(len(n)+1)]
dp[0] = 1
dp[1] = 1
num = "0"+n
if num[1] == "0":
    print(0)
else:
    for i in range(2, len(n)+1):
        if int(num[i]) > 0:
            dp[i] += dp[i-1]
        number = int(num[i-1]) * 10 + int(num[i])
        if number >= 10 and number <= 26:
            dp[i] += dp[i-2]
    print(dp[-1] % 1000000)
