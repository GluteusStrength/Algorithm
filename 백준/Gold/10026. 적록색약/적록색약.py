import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    cnt += 1
    visited[x][y] = cnt
    while q:
        a, b = q.popleft()
        for i in range(4):
            mx = a + dx[i]
            my = b + dy[i]
            if 0 <= mx < t and 0 <= my < t:
                if graph[x][y] == graph[mx][my] and not visited[mx][my]:
                    visited[mx][my] = cnt
                    q.append((mx, my))
    return visited


t = int(input())
graph = [list(input()) for _ in range(t)]
for i in range(2):
    res = []
    visited = [[0 for _ in range(t)] for _ in range(t)]
    cnt = 0
    if i == 0:
        for j in range(t):
            for k in range(t):
                if not visited[j][k]:
                    bfs(j, k) # 하나씩 진행해준다.
    else:
        for j in range(t):
            for k in range(t):
                if graph[j][k] == "R":
                    graph[j][k] = 'G' # 빨간색과 초록색의 색 차이는 없기 때문이다.
        for j in range(t):
            for k in range(t):
                if not visited[j][k]:
                    bfs(j, k) # 하나씩 진행해준다.
    ans = 0
    for l in visited:
        ans = max(max(l), ans)
    print(ans)