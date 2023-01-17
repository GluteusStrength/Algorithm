import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
res = []
for i in range(1, n+1):
    visited = [-1] * (n+1)
    visited[i] = 0
    q = deque()
    q.append(i)
    while q:
        x = q.popleft()
        for j in graph[x]:
            if visited[j] == -1:
                visited[j] = visited[x] + 1
                q.append(j)
    res.append(sum(visited[1:]))
ans = min(res)
for i in range(len(res)):
    if res[i] == ans:
        print(i+1)
        break