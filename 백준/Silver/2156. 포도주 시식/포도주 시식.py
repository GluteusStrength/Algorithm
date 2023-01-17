N = input()
n = int(N)
wine_l = []
cnt_1 = 0
dp=[0]
for i in range(n):
    wine_l.append(int(input()))
if n == 1:
    dp.append(wine_l[0])
    print(dp[1])
else:
    dp.append(wine_l[0])
    dp.append(wine_l[0]+wine_l[1])
    if n == 2:
        print(dp[2])
    else:
        for j in range(3, n+1):
            case_1 = dp[j-1]
            case_2 = dp[j-3] + wine_l[j-2] + wine_l[j-1]
            case_3 = dp[j-2] + wine_l[j-1]
            max_dp = max(case_1, case_2, case_3)
            dp.append(max_dp)
        print(dp[n])

