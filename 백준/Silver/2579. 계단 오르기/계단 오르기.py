n = int(input())
s = [0]
for i in range(n):
    s.append(int(input()))
dp = [0]
if n == 1:
    print(s[1])
else:
    dp.append(s[1])
    dp.append(s[1]+s[2])
    if n == 2:
        print(s[1]+s[2])
    else:
        for i in range(3, n+1):
            if i < n:
                case_1 = dp[i-2] + s[i]
                case_2 = dp[i-3] + s[i-1] + s[i]
                dp.append(max(case_1, case_2))
            if i == n:
                case_1 = dp[i-2] + s[i]
                case_2 = dp[i-3] + s[i-1] + s[i]
                dp.append(max(case_1, case_2))
        print(dp[n])


