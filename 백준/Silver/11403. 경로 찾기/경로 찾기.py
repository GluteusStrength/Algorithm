import sys
from collections import deque
n = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
final = [[0 for _ in range(n)] for _ in range(n)]
graph = [[] for _ in range(n)]
# directional graph
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            graph[i].append(j)
q = deque()
# final process
def bfs(s, i):
    for x in s:
        q.append(x)
    visited = [0 for _ in range(n)]
    while q:
        x = q.popleft()
        if not visited[x]:
            visited[x] = 1
            for a in graph[x]:
                q.append(a)
            final[i][x] = 1
for i in range(n):
    start = graph[i]
    bfs(start, i)
for i in range(n):
    print(*final[i])