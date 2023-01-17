import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
in_degree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
queue = deque()
Class = [[0,0]]+[list(map(int, sys.stdin.readline().split())) for _ in range(m)]
for i in range(1, m+1):
    in_degree[Class[i][1]] += 1
    graph[Class[i][0]].append(Class[i][1])
for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)
semester = [1 for _ in range(n+1)]
while queue:
    now = queue.popleft()
    for i in graph[now]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)
            semester[i] = semester[now] + 1
print(*semester[1:])