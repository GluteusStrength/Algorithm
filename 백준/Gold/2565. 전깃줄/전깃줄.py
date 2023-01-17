import sys
n = int(sys.stdin.readline())
line = []
for i in range(n):
    line.append(list(map(int, sys.stdin.readline().split())))
line.sort()
dp = [1 for _ in range(n)]
b_line = []
for i in range(n):
    b_line.append(line[i][1])
for i in range(1, n):
    for j in range(i):
        if b_line[i] > b_line[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))