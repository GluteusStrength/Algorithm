import sys
from collections import deque
n = int(input())
table = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
q = deque()
q.append((0,0))
visited = [[-1 for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited[0][0] = 0
while True:
    x, y = q.popleft()
    if x == n-1 and y == n-1:
        break
    else:
        for i in range(4):
            mx = dx[i] + x
            my = dy[i] + y
            if (0 <= mx < n) and (0 <= my < n) and visited[mx][my] == -1:
                if table[mx][my] == 1:
                    visited[mx][my] = visited[x][y]
                    q.appendleft((mx, my))
                if table[mx][my] == 0: # 후순위로 밀어버린다
                    visited[mx][my] = visited[x][y] + 1
                    q.append((mx, my))
print(visited[n-1][n-1])