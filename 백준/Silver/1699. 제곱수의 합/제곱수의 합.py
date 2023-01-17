n = int(input())
import math
a = int(math.sqrt(n))
if math.sqrt(n) == int(math.sqrt(n)):
    print(1)
else:
    dp = [100000] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[5] = 2
    dp[6] = 3
    dp[7] = 4
    l = []
    for i in range(2, n+1):
        if math.sqrt(i) == int(math.sqrt(i)):
            dp[i] = 1
            dp[i+1] = 2
    for j in range(1 , n+1):
       if dp[j] != 100000:
           continue
       else:
           for k in range(1, int(math.sqrt(j))+1):
               dp[j] = min(dp[j], dp[j - k*k]+1)
    print(dp[n])