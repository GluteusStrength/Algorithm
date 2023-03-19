import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
travel = list(map(int, sys.stdin.readline().split()))
visited = [0 for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            graph[i].append(j)
q = deque()
graphs = []
def bfs(visited):
    gr = []
    gr.append(q[0])
    while q:
        x = q.popleft()
        for k in graph[x]:
            if graph[x]:
                if not visited[k]:
                    gr.append(k)
                    visited[k] = 1
                    q.append(k)
    return gr
for i in range(n):
    if sum(visited) == len(visited):
        break
    if visited[i]:
        continue
    if not visited[i]:
        q.append(i)
        visited[q[0]] = 1
    g = bfs(visited)
    graphs.append(g)
flag = False
for i in graphs:
    x = list(set(travel))
    for a in range(len(x)):
        x[a] -= 1
    cnt = 0
    x.sort()
    for j in x:
        if j in i:
            cnt += 1
    if cnt == len(x):
        flag = True
if flag:
    print("YES")
else:
    print("NO")