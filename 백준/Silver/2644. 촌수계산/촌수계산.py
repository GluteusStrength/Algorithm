import sys
from collections import deque
input = sys.stdin.readline

def bfs(a):
    q = deque()
    q.append(a)
    while q:
        s = q.popleft()
        for i in graph[s]:
            if not r[i]:
                r[i] = r[s] + 1
                q.append(i)

n = int(input())
a, b = list(map(int, input().split()))
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
r = [0 for _ in range(n+1)]
bfs(a)
if not r[b]:
    print(-1)
else:
    print(r[b])
