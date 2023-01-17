import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
dp = [-999999999999]
for i in l:
    if dp[-1] < i:
        dp.append(i)
    else:
        left = 0
        right = len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < i:
                left = mid + 1
            else:
                right = mid
        dp[right] = i
if -999999999999 in dp:
    print(len(dp) - 1)
else:
    print(len(dp))