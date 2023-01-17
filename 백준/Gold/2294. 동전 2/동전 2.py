import sys
n, k = map(int, sys.stdin.readline().split())
l = []
for i in range(n):
    l.append(int(input()))
l = list(set(l))
l.sort()
for i in l:
    if i > k:
        l.remove(i)
dp = [10001 for _ in range(k+1)]
dp[0] = 0
for i in range(len(l)):
    c = l[i]
    for j in range(c, k+1):
        dp[j] = min(dp[j], dp[j-c] + 1)
if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])

