import copy
from collections import deque
from itertools import combinations
import sys, math
n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = math.inf
def bfs(q, cnt):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    time = -1
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for a, b in q: # 우선적으로 q에 있는 것들은 다 1로 처리.
        visited[a][b] = 1
    while q:
        for i in range(len(q)): # 뭉탱이로 처리
            x, y = q.popleft()
            for j in range(4):
                mx = dx[j] + x
                my = dy[j] + y
                if (0 <= mx < n) and (0 <= my < n) and not visited[mx][my]:
                    if table[mx][my] != 1:
                        visited[mx][my] = 1
                        q.append((mx, my))
                        cnt += 1
        time += 1
    return time, cnt
queue = []
q = deque()
w = 0
for i in range(n):
    for j in range(n):
        if table[i][j] == 2:
            queue.append((i, j))
        if table[i][j] == 1:
            w += 1
virus = list(combinations(queue, m))
flag = False
for v in virus:
    for p in v:
        q.append(p)
    res = bfs(q, m)
    if res[1] + w == n ** 2:
        flag = True
        ans = min(ans, res[0])
if flag == True:
    print(ans)
else:
    print(-1)
