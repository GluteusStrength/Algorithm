import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    in_degree = [0 for _ in range(n+1)]
    queue = deque()
    graph = [[] for _ in range(n+1)]
    time = [0]+list(map(int, sys.stdin.readline().split()))
    order = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
    dp = [0 for _ in range(n+1)]
    for i in order:
        in_degree[i[1]] += 1
        graph[i[0]].append(i[1])
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = time[i]
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            in_degree[i] -= 1
            dp[i] = max(dp[i], time[i] + dp[cur])
            if in_degree[i] == 0:
                queue.append(i)
    print(dp[int(input())])