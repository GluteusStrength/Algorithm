import sys
from collections import deque
q = deque()
def bfs():
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, 1, -1, -1, 1, -1, 1]
    while q:
        x, y = q.popleft()
        for a in range(8):
            mx = x + dx[a]
            my = y + dy[a]
            if (0 <= mx < h) and (0 <= my < w) and table[mx][my] == 1:
                if not visited[mx][my]:
                    visited[mx][my] = 1
                    q.append((mx, my))
    return 1
while True:
    w, h = map(int, sys.stdin.readline().split())
    visited = [[0]*w for _ in range(h)]
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    if w == 0 and h == 0:
        break
    else:
        cnt = 0
        for i in range(h):
            for j in range(w):
                if not visited[i][j] and table[i][j] == 1:
                    q.append((i, j))
                    visited[i][j] = 1
                    cnt += bfs()
    print(cnt)
