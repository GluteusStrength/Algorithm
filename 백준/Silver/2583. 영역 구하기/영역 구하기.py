import sys
from collections import deque
m, n, k = map(int, sys.stdin.readline().split())
visited = [[0 for _ in range(n)] for _ in range(m)]
co = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
for i in co:
    y_1, x_1 = i[0], i[1]
    y_2, x_2 = i[2], i[3]
    for j in range(x_1, x_2):
        for k in range(y_1, y_2):
            visited[j][k] = 1
q = deque()
def bfs(i,j,area):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q.append((i,j))
    while q:
        x, y = q.popleft()
        for a in range(4):
            mx = dx[a] + x
            my = dy[a] + y
            if (0 <= mx < m) and (0 <= my < n) and visited[mx][my] == 0:
                area += 1
                visited[mx][my] = 1
                q.append((mx, my))
    return area

res = []
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = 1
            res.append(bfs(i,j,1))

print(len(res))
res.sort()
print(*res)