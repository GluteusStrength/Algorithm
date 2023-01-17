from collections import deque
import sys
n = int(input())
k = int(input())
q = deque()
cpu = [0 for _ in range(n+1)]
net = [[] for _ in range(n+1)]
virus = []
visited = [0 for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)
    net[b].append(a)
if net[1]:
    q.append(1)
    visited[1] = 1
    while q:
        x = q.popleft()
        for i in net[x]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
    print(sum(visited) - 1)
else:
    print(0)