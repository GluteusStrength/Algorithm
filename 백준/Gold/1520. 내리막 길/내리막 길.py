# dfs는 아직 익숙하지 않다. 공부할 것!
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1 # 재귀의 마지막 지점.
    if visited[x][y] != -1: # 방문했다면
        return visited[x][y]
    visited[x][y] = 0 # 방문했다면 0으로 초기화
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < m and 0 <= my < n:
            if h[x][y] > h[mx][my]:
                visited[x][y] += dfs(mx, my)
    return visited[x][y]

m, n = map(int, sys.stdin.readline().split())
h = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
visited = [[-1 for _ in range(n)] for _ in range(m)]
print(dfs(0, 0))