import sys
from collections import deque
def dfs(v):
    visited_dfs[v] = 1
    print(v, end = " ")
    for i in range(1, n+1):
        if not visited_dfs[i] and graph[v][i] == 1:
            dfs(i) # 재귀를 통해 깊이 우선 탐색 진행.

def bfs(v):
    q = deque()
    q.append(v)
    visited_bfs[v] = 1
    while q:
        x = q.popleft()
        print(x, end = " ")
        for i in range(1, n+1):
            if not visited_bfs[i] and graph[x][i] == 1:
                q.append(i)
                visited_bfs[i] = 1
n, m, v = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1 # 양방향 연결
    graph[b][a] = 1 # 양방향 연결
visited_dfs = [0 for _ in range(n+1)]
visited_bfs = [0 for _ in range(n+1)]
dfs(v)
print()
bfs(v)
