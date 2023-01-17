import sys
N = input()
n = int(N)
l = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j]+1)
        else:
            continue
length = max(dp)
k = length
ans = []
for x in range(n-1, -1, -1):
    if dp[x] == k:
        ans.append(l[x])
        k -= 1
    else:
        continue
ans.reverse()
print(length)
for i in range(len(ans)):
    print(ans[i], end = ' ')