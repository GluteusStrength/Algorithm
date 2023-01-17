import sys
from collections import deque
n = int(sys.stdin.readline())
buildings = [[]]
queue = deque()
for _ in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    x.pop()
    buildings.append(x)
in_degree = [0 for _ in range(n+1)]
time = [0]
dp = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    time.append(buildings[i][0])
    if len(buildings[i]) >= 2:
        flag = buildings[i][1:]
        for x in flag:
            in_degree[i] += 1
            graph[x].append(i)
for i in range(1, n+1):
    if in_degree[i] == 0:
        dp[i] = time[i]
        queue.append(i)
while queue:
    cur = queue.popleft()
    for i in graph[cur]:
        in_degree[i] -= 1
        dp[i] = max(dp[i], time[i]+dp[cur])
        if in_degree[i] == 0:
            queue.append(i)
for x in dp[1:]:
    print(x)