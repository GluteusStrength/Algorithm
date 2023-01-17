import sys
n, m = map(int, sys.stdin.readline().split())
mem = [0] + list(map(int, sys.stdin.readline().split()))
cost = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(sum(cost)+1)] for _ in range(n+1)]
result = sum(cost)
cnt = 0
for x in range(1, n+1):
    memory = mem[x]
    c = cost[x]
    for y in range(sum(cost)+1):
        if y < c:
            dp[x][y] = dp[x-1][y]
        else:
            dp[x][y] = max(dp[x-1][y], dp[x-1][y-c] + memory)
        if dp[x][y] >= m:
            result = min(result, y)
            cnt += 1
print(result)

