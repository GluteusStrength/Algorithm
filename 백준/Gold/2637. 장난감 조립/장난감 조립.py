import sys
from collections import deque
n = int(input())
m = int(input())
cor = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
cor.sort(key = lambda x : (x[0],x[1]))
in_degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
queue = deque()
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in cor:
    flag = i[1:]
    in_degree[i[0]] += 1
    graph[flag[0]].append(i[0])
    dp[i[0]][flag[0]] += flag[1]
basic = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)
        basic.append(i)
while queue:
    cur = queue.popleft()
    for x in graph[cur]:
        in_degree[x] -= 1
        if cur not in basic:
            for y in range(1, n+1):
                dp[x][y] += dp[cur][y] * dp[x][cur]
        if in_degree[x] == 0:
            queue.append(x)
for i in basic:
    print(i, dp[n][i])