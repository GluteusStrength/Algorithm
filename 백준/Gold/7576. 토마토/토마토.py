import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(q):
    while q:
        a, b = q.popleft()
        for i in range(4):
            mx = a + dx[i]
            my = b + dy[i]
            if 0 <= mx < n and 0 <= my < m:
                if farm[mx][my] == 0:
                    farm[mx][my] = farm[a][b] + 1
                    q.append((mx, my))
    return

m, n = map(int, sys.stdin.readline().split())
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if farm[i][j] == 1:
            q.append((i, j))
bfs(q)
flag = True
for i in farm:
    if 0 in i:
        flag = False
        break
if flag:
    res = 0
    for i in farm:
        res = max(max(i), res)
    print(res - 1)
else:
    print(-1)