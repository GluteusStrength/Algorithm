import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
q = deque()
q.append(1)
res = [0] * (n+1)
while q:
    cur = q.popleft()
    for i in graph[cur]:
        if res[i] == 0:
            res[i] = cur
            q.append(i)
for x in res[2:]:
    print(x)