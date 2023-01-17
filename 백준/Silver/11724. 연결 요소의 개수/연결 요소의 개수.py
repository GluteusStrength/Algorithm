import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)


visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
res = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        res += 1
final = visited[1:]
res += final.count(0) # 아무것도 연결되지 않은 것
print(res)
