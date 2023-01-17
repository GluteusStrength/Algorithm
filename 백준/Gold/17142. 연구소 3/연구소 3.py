from copy import deepcopy
from collections import deque
from itertools import combinations
import sys, math
n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
def bfs(q, w):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    time = 0
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    virus = deepcopy(table)
    cnt = 0
    for x, y in q:
        visited[x][y] = 0 # 일단 활성화된 바이러스는 0으로 초기화.
    while q:
        x, y = q.popleft()
        for k in range(4):
            mx = dx[k] + x
            my = dy[k] + y
            if (0 <= mx < n) and (0 <= my < n):
                if virus[mx][my] == 0 and visited[mx][my] == -1: # 퍼지는 case
                    visited[mx][my] = visited[x][y] + 1
                    q.append((mx, my))
                    virus[mx][my] = 2
                    time = max(time, visited[mx][my])
                if virus[mx][my] == 2 and visited[mx][my] == -1: # 비활성화 바이러스를 활성으로 변환
                    visited[mx][my] = visited[x][y] + 1
                    q.append((mx, my))
    for j in virus:
        cnt += j.count(2)
    if cnt + w != n**2:
        return math.inf
    return time
queue = deque()
w = 0
for i in range(n):
    for j in range(n):
        if table[i][j] == 2:
            queue.append((i, j))
        if table[i][j] == 1:
            w += 1
ans = math.inf
for q in combinations(queue, m):
    ans = min(bfs(deque(q), w), ans)
if ans == math.inf:
    print(-1)
else:
    print(ans)