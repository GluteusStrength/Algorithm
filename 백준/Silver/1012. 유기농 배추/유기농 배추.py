import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        a, b = q.popleft()
        for i in range(4):
            mx = a + dx[i]
            my = b + dy[i]
            if 0 <= mx < n and 0 <= my < m:
                if not visited[mx][my] and graph[mx][my] == 1:
                        q.append((mx, my))
                        visited[mx][my] = 1

t = int(input())
for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1
    bug = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1 and not visited[x][y]:
                bfs(x, y)
                bug += 1
    print(bug)